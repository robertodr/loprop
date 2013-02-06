import os 
import numpy as np
import loprop
from util import full

tmpdir=os.path.join('h2o_rot', 'tmp')

# modify Gagliardi penalty function to include unit conversion bug
from loprop import penalty_function, xtang
mcpf = lambda *args : penalty_function(*args, alpha=2/xtang**2)
mcsf = lambda Fab : 2*np.max(np.abs(Fab))

def assert_(ref, this, atol=1e-5, text=None):
    if text: print text,
    print ref, this
    print "Max deviation", np.amax(ref - this)
    assert np.allclose(ref, this, atol=atol)

def pairs(n):
    li = []
    mn = 0
    for m in range(n):
        for n in range(m+1):
            li.append((mn, m, n))
            mn += 1
    return li

from h2o_rot_data import Aref, ff, rMP

def test_nuclear_charge():
    m = loprop.MolFrag(tmpdir)
    Z = m.Z
    Zref = [8., 1., 1.]
    assert_(Zref, Z)

def test_coordinates_au():
    m = loprop.MolFrag(tmpdir)
    R = m.R
    Rref = [
        [-0.27439,  0.48018, -0.35773],
        [-0.43275, -0.82090,  0.88874],
        [ 0.98152, -0.13965, -1.50233]
        ]
    assert_(Rref, R)

def test_default_gauge():
    m = loprop.MolFrag(tmpdir)
    Rcref = full.init([-0.16463294,   0.28808875,  -0.34753953])
    assert_(Rcref, m.Rc)

def test_total_charge():
    m = loprop.MolFrag(tmpdir, maxl=0)
    assert_(m.Qab.sum(), -10.0)

def test_charge():
    M = loprop.MolFrag(tmpdir, maxl=0)
    Qref = rMP[0, 0, (0, 2, 5)]
    Qaa = M.Qab.diagonal()
    print Qref, Qaa
    assert np.allclose(Qref, Qaa)

def test_total_dipole():
    m = loprop.MolFrag(tmpdir)
    Dref = [0.40095611, -0.70174560, 0.03721264]
    # molecular dipole moment wrt gauge center gc
    Dtot = m.Dab.sum(axis=2).sum(axis=1).view(full.matrix)
    Qa = m.Qab.diagonal()
    Q = Qa.sum()
    Dtot += Qa*m.R - Q*m.Rc
    assert_(Dtot, Dref)

def test_dipole_allbonds():
    m = loprop.MolFrag(tmpdir)
    Dref = rMP[1:4, 0, :]
    D = full.matrix(Dref.shape)
    Dab = m.Dab
    print Dab
    for ab, a, b in pairs(m.noa):
        D[:, ab] += Dab[:, a, b ] 
        if a != b: D[:, ab] += Dab[:, b, a] 
    assert_(Dref, D)

def test_dipole_nobonds():
    m = loprop.MolFrag(tmpdir, maxl = 1) 
    O =  [ 0.16803109,  -0.29408639,   0.01559623 ]
    H1 = [ 0.01993698,   0.15310511,  -0.14837852 ]
    H2 = [-0.14852716,   0.07195449,   0.13644124 ]

    Dref = full.init([O, H1, H2])
    Daa = m.Dab.sum(axis=2).view(full.matrix)
    assert_(Dref, Daa)

def test_quadrupole_total():
    QUref = full.init([-5.97224464, 0.24966841, 0.77110470, -6.17226877, 0.42783060,-6.57765870] )
    m = loprop.MolFrag(tmpdir)
    rrab=full.matrix((6, m.noa, m.noa))
    rRab=full.matrix((6, m.noa, m.noa))
    RRab=full.matrix((6, m.noa, m.noa))
    Rabc = 1.0*m.Rab
    for a in range(m.noa):
        for b in range(m.noa):
            Rabc[a,b,:] -= m.Rc
    for a in range(m.noa):
        for b in range(m.noa):
            ij = 0
            for i in range(3):
                for j in range(i,3):
                    rRab[ij, a, b] = m.Dab[i, a, b]*Rabc[a, b, j]\
                                   + m.Dab[j, a, b]*Rabc[a, b, i]
                    RRab[ij, a, b] = m.Qab[a, b]*(m.R[a, i] - m.Rc[i])*(m.R[b, j] - m.Rc[j])
                    ij += 1
    QUcab = m.QUab + rRab + RRab
    QUc = QUcab.sum(axis=2).sum(axis=1).view(full.matrix)
    print "QUc", QUc, QUref
    assert np.allclose(QUref, QUc)
    


def test_quadrupole_allbonds():
    m = loprop.MolFrag(tmpdir)
    QUref = rMP[4:, 0, :]
    QU = full.matrix(QUref.shape)
    QUab = m.QUab
    for ab, a, b in pairs(m.noa):
        QU[:, ab] += QUab[:, a, b ] 
        if a != b: QU[:, ab] += QUab[:, b, a] 
    assert_(QUref, QU)

def test_quadrupole_nobonds():
    M = loprop.MolFrag(tmpdir)
    O =  [-3.94201869,  -0.09440612,  -0.46008896,  -3.88662892,  -0.24872405, -3.55263150 ]
    H1 = [-0.44344604,   0.03059799,  -0.01783139,  -0.13501155,  -0.28237140, -0.18945131 ]
    H2 = [-0.16524860,  -0.14585061,  -0.24009742,  -0.36955871,   0.13544768, -0.23311075 ]

    QUref = full.init([O, H1, H2])
    QUaa = (M.QUab + M.dQUab).sum(axis=2).view(full.matrix)
    assert_(QUref, QUaa)


def test_Fab():
    Fabref = full.init([
        [-0.12E-03,  0.58E-04, 0.58E-04],
        [ 0.58E-04, -0.58E-04, 0.19E-28],
        [ 0.58E-04,  0.19E-28,-0.58E-04]
        ])

    m = loprop.MolFrag(tmpdir, pf=mcpf)
    Fab = m.Fab

    assert_(Fabref, Fab)

def test_molcas_shift():
    Labref = full.init([
        [0.12E-03, 0.29E-03, 0.29E-03],
        [0.29E-03, 0.17E-03, 0.23E-03],
        [0.29E-03, 0.23E-03, 0.17E-03]
        ])

    m = loprop.MolFrag(tmpdir, pf=mcpf, sf=mcsf)
    Fab = m.Fab
    Lab = Fab + m.sf(Fab)

    print Labref, Lab
    assert np.allclose(Labref, Lab, atol=1e-5, rtol=1e-2)

def test_total_charge_shift():
    m = loprop.MolFrag(tmpdir)
    dQ = m.dQa.sum(axis=0).view(full.matrix)
    dQref = [0., 0., 0.]
    assert_(dQref, dQ)

def test_atomic_charge_shift():
    m = loprop.MolFrag(tmpdir)
    dQa = m.dQa
    dQaorig = rMP[0, :, (0,2,5)]
    dQaref = dQaorig[:, 1::2]
    dQaref -= dQaorig[:, 2::2]
    dQaref /= 2*ff

    assert_(dQaref, dQa, 0.006)

def test_lagrangian():
# values per "perturbation" as in atomic_charge_shift below
    laorig = full.init([
    [-5.10951420, -10.14238550,  15.25189980],
    [ 5.15832880,  10.18998130, -15.3483100],
    [ 8.97693540, -10.67897570,   1.7020403],
    [-8.92856407,  10.55769081,  -1.6291267],
    [-0.42410210,  21.68234150, -21.2582394],
    [ 0.54318080, -21.75839020,  21.2152094],
    ])

    laref = laorig[:,0:6:2]
    laref -= laorig[:,1:6:2]
    laref /= 2*ff
#...>
    m = loprop.MolFrag(tmpdir, pf=mcpf, sf=mcsf)
    la = m.la

    print laref, la
# The sign difference is because mocas sets up rhs with opposite sign
    assert np.allclose(-laref, la, atol=100)

def test_bond_charge_shift():
    m = loprop.MolFrag(tmpdir, pf=mcpf, sf=mcsf)
    dQab = m.dQab
    noa = m.noa

    dQaborig = rMP[0, :, (1, 3, 4)]

    dQabref = dQaborig[:, 1:7:2]
    dQabref -= dQaborig[:, 2:7:2]
    dQabref /= (2*ff)
    
    dQabcmp = full.matrix((3, 3))
    ab = 0
    for a in range(noa):
        for b in range(a):
            dQabcmp[ab, :] = dQab[a, b, :]
            ab += 1

    assert_(-dQabref, dQabcmp, 0.006)

def test_bond_charge_shift_sum():
    m = loprop.MolFrag(tmpdir, pf=mcpf, sf=mcsf)
    dQaref = m.dQa
    dQa  = m.dQab.sum(axis=1).view(full.matrix)
    print dQaref, dQa
    assert np.allclose(dQaref, dQa)


def test_polarizability_total():
    Aref = full.init([
         [ 4.49289385,  -0.42772271, -1.56180915],
         [-0.42772271,   4.80103940, -0.85729045],
         [-1.56180915,  -0.85729045,  5.75132939]
        ])

    m = loprop.MolFrag(tmpdir, pf=mcpf, sf=mcsf)
    dQa = m.dQa
    Rab = m.Rab
    Aab = m.Aab
    noa = m.noa
    
    Am = Aab.sum(axis=3).sum(axis=2).view(full.matrix)
    for i in range(3):
        for j in range(3):
            for a in range(noa):
                Am[i, j] += Rab[a, a, i]*dQa[a, j]

    assert_(Am, Aref, 0.015)
        
def notest_polarizability_allbonds_molcas_internal():
    m = loprop.MolFrag(tmpdir, pf=mcpf, sf=mcsf)
    ff = .001

# polarizabilities
    RO, RH1, RH2 = m.R

    ihff = 1/(2*ff)

    Oxx = ihff*(rMP[1, 1, 0] - rMP[1, 2, 0])
    Oyx = ihff*(rMP[2, 1, 0] - rMP[2, 2, 0]
        +       rMP[1, 3, 0] - rMP[1, 4, 0])/2
    Oyy = ihff*(rMP[2, 3, 0] - rMP[2, 4, 0])
    Ozx = ihff*(rMP[3, 1, 0] - rMP[3, 2, 0]
        +       rMP[1, 5, 0] - rMP[1, 6, 0])/2
    Ozy = ihff*(rMP[3, 3, 0] - rMP[3, 4, 0]
        +       rMP[2, 5, 0] - rMP[2, 6, 0])/2
    Ozz = ihff*(rMP[3, 5, 0] - rMP[3, 6, 0])
    H1Oxx = ihff*(rMP[1, 1, 1] - rMP[1, 2, 1] \
          - (rMP[0, 1, 1] - rMP[0, 2, 1])*(RH1[0]-RO[0]))
    H1Oyx = ihff*(
        (rMP[2, 1, 1] - rMP[2, 2, 1] 
       + rMP[1, 3, 1] - rMP[1, 4, 1])/2
       - (rMP[0, 1, 1] - rMP[0, 2, 1])*(RH1[1]-RO[1])
#      - (rMP[0, 3, 1] - rMP[0, 4, 1])*(RH1[0]-RO[0]) THIS IS REALLY... A BUG?
       )
    H1Oyy = ihff*(rMP[2, 3, 1] - rMP[2, 4, 1] - (rMP[0, 3, 1] - rMP[0, 4, 1])*(RH1[1]-RO[1]))
    H1Ozx = ihff*(
        (rMP[3, 1, 1] - rMP[3, 2, 1]
       + rMP[1, 5, 1] - rMP[1, 6, 1])/2
      - (rMP[0, 1, 1] - rMP[0, 2, 1])*(RH1[2]-RO[2])
#             - (rMP[0, 5, 1] - rMP[0, 6, 1])*(RH1[0]-RO[0]) #THIS IS REALLY... A BUG?
            )
    H1Ozy = ihff*(
        (rMP[3, 3, 1] - rMP[3, 4, 1]
       + rMP[2, 5, 1] - rMP[2, 6, 1])/2
      - (rMP[0, 3, 1] - rMP[0, 4, 1])*(RH1[2]-RO[2])
#     - (rMP[0, 5, 1] - rMP[0, 6, 1])*(RH1[1]-RO[1]) THIS IS REALLY... A BUG?
        )
    H1Ozz = ihff*(rMP[3, 5, 1] - rMP[3, 6, 1] - (rMP[0, 5, 1] - rMP[0, 6, 1])*(RH1[2]-RO[2]))
    H1xx = ihff*(rMP[1, 1, 2] - rMP[1, 2, 2])
    H1yx = (ihff*(rMP[2, 1, 2] - rMP[2, 2, 2])
         +  ihff*(rMP[1, 3, 2] - rMP[1, 4, 2]))/2
    H1yy = ihff*(rMP[2, 3, 2] - rMP[2, 4, 2])
    H1zx = (ihff*(rMP[3, 1, 2] - rMP[3, 2, 2])
         +  ihff*(rMP[1, 5, 2] - rMP[1, 6, 2]))/2
    H1zy = (ihff*(rMP[3, 3, 2] - rMP[3, 4, 2])
         +  ihff*(rMP[2, 5, 2] - rMP[2, 6, 2]))/2
    H1zz = ihff*(rMP[3, 5, 2] - rMP[3, 6, 2])
    H2Oxx = ihff*(rMP[1, 1, 3] - rMP[1, 2, 3] - (rMP[0, 1, 3] - rMP[0, 2, 3])*(RH2[0]-RO[0]))
    H2Oyx = ihff*(
        (rMP[2, 1, 3] - rMP[2, 2, 3] 
       + rMP[1, 3, 3] - rMP[1, 4, 3])/2
       - (rMP[0, 1, 3] - rMP[0, 2, 3])*(RH1[1]-RO[1])
#      - (rMP[0, 3, 1] - rMP[0, 4, 1])*(RH1[0]-RO[0]) THIS IS REALLY... A BUG?
       )
    H2Oyy = ihff*(rMP[2, 3, 3] - rMP[2, 4, 3] - (rMP[0, 3, 3] - rMP[0, 4, 3])*(RH2[1]-RO[1]))
    H2Ozx = ihff*(
        (rMP[3, 1, 3] - rMP[3, 2, 3]
       + rMP[1, 5, 3] - rMP[1, 6, 3])/2
      - (rMP[0, 1, 3] - rMP[0, 2, 3])*(RH1[2]-RO[2])
#             - (rMP[0, 5, 1] - rMP[0, 6, 1])*(RH1[0]-RO[0]) #THIS IS REALLY... A BUG?
            )
    H2Ozy = ihff*(
        (rMP[3, 3, 3] - rMP[3, 4, 3]
       + rMP[2, 5, 3] - rMP[2, 6, 3])/2
      - (rMP[0, 3, 3] - rMP[0, 4, 3])*(RH1[2]-RO[2])
#     - (rMP[0, 5, 3] - rMP[0, 6, 3])*(RH1[1]-RO[1]) THIS IS REALLY... A BUG?
        )
    H2Ozz = ihff*(rMP[3, 5, 3] - rMP[3, 6, 3] - (rMP[0, 5, 3] - rMP[0, 6, 3])*(RH2[2]-RO[2]))
    H2H1xx = ihff*(rMP[1, 1, 4] - rMP[1, 2, 4] - (rMP[0, 1, 4] - rMP[0, 2, 4])*(RH2[0]-RH1[0]))
    H2H1yx = ihff*(
        (rMP[2, 1, 4] - rMP[2, 2, 4] 
       + rMP[1, 3, 4] - rMP[1, 4, 4])/2
       - (rMP[0, 1, 4] - rMP[0, 2, 4])*(RH1[1]-RO[1])
#      - (rMP[0, 3, 4] - rMP[0, 4, 4])*(RH1[0]-RO[0]) THIS IS REALLY... A BUG?
       )
    H2H1yy = ihff*(rMP[2, 3, 4] - rMP[2, 4, 4] - (rMP[0, 3, 4] - rMP[0, 4, 4])*(RH2[1]-RH1[1]))
    H2H1zx = ihff*(
        (rMP[3, 1, 4] - rMP[3, 2, 4]
       + rMP[1, 5, 4] - rMP[1, 6, 4])/2
      - (rMP[0, 1, 4] - rMP[0, 2, 4])*(RH1[2]-RO[2])
#     - (rMP[0, 5, 4] - rMP[0, 6, 4])*(RH1[0]-RO[0]) #THIS IS REALLY... A BUG?
            )
    H2H1zy = ihff*(
        (rMP[3, 3, 4] - rMP[3, 4, 4]
       + rMP[2, 5, 4] - rMP[2, 6, 4])/2
      - (rMP[0, 3, 4] - rMP[0, 4, 4])*(RH1[2]-RO[2])
#     - (rMP[0, 5, 4] - rMP[0, 6, 4])*(RH1[1]-RO[1]) THIS IS REALLY... A BUG?
        )
    H2H1zz = ihff*(rMP[3, 5, 4] - rMP[3, 6, 4] - (rMP[0, 5, 4] - rMP[0, 6, 4])*(RH2[2]-RH1[2]))
    H2xx = ihff*(rMP[1, 1, 5] - rMP[1, 2, 5])
    H2yx = (ihff*(rMP[2, 1, 5] - rMP[2, 2, 5])
         +  ihff*(rMP[1, 3, 5] - rMP[1, 4, 5]))/2
    H2yy = ihff*(rMP[2, 3, 5] - rMP[2, 4, 5])
    H2zx = (ihff*(rMP[3, 1, 5] - rMP[3, 2, 5])
         +  ihff*(rMP[1, 5, 5] - rMP[1, 6, 5]))/2
    H2zy = (ihff*(rMP[3, 3, 5] - rMP[3, 4, 5])
         +  ihff*(rMP[2, 5, 5] - rMP[2, 6, 5]))/2
    H2zz = ihff*(rMP[3, 5, 5] - rMP[3, 6, 5])

    comp = ("XX", "yx", "yy", "zx", "zy", "zz")
    bond = ("O", "H1O", "H1", "H2O", "H2H1", "H2")

    assert_(O[0], Oxx, text="Oxx")
    assert_(O[1], Oyx, text="Oyx")
    assert_(O[2], Oyy, text="Oyy")
    assert_(O[3], Ozx, text="Ozx")
    assert_(O[4], Ozy, text="Ozy")
    assert_(O[5], Ozz, text="Ozz")
    assert_(H1O[0], H1Oxx, text="H1Oxx")
    assert_(H1O[1], H1Oyx, text="H1Oyx")
    assert_(H1O[2], H1Oyy, text="H1Oyy")
    assert_(H1O[3], H1Ozx, text="H1Ozx")
    assert_(H1O[4], H1Ozy, text="H1Ozy")
    assert_(H1O[5], H1Ozz, text="H1Ozz")
    assert_(H1[0], H1xx, text="H1xx")
    assert_(H1[1], H1yx, text="H1yx")
    assert_(H1[2], H1yy, text="H1yy")
    assert_(H1[3], H1zx, text="H1zx")
    assert_(H1[4], H1zy, text="H1zy")
    assert_(H1[5], H1zz, text="H1zz")
    assert_(H2O[0], H2Oxx, text="H2Oxx")
    assert_(H2O[1], H2Oyx, text="H2Oyx")
    assert_(H2O[2], H2Oyy, text="H2Oyy")
    assert_(H2O[3], H2Ozx, text="H2Ozx")
    assert_(H2O[4], H2Ozy, text="H2Ozy")
    assert_(H2O[5], H2Ozz, text="H2Ozz")
    assert_(H2H1[0], H2H1xx, text="H2H1xx")
    assert_(H2H1[1], H2H1yx, text="H2H1yx")
    assert_(H2H1[2], H2H1yy, text="H2H1yy")
    assert_(H2H1[3], H2H1zx, text="H2H1zx")
    assert_(H2H1[4], H2H1zy, text="H2H1zy")
    assert_(H2H1[5], H2H1zz, text="H2H1zz")
    assert_(H2[0], H2xx, text="H2xx")
    assert_(H2[1], H2yx, text="H2yx")
    assert_(H2[2], H2yy, text="H2yy")
    assert_(H2[3], H2zx, text="H2zx")
    assert_(H2[4], H2zy, text="H2zy")
    assert_(H2[5], H2zz, text="H2zz")

def test_altint():
    m = loprop.MolFrag(tmpdir, pf=mcpf, sf=mcsf)
    R = m.R
    diff = [(1, 2), (3, 4), (5, 6)]
    atoms = (0, 2, 5) 
    bonds = (1, 3, 4)
    ablab = ("O", "H1O", "H1", "H2O", "H2H1", "H2")
    ijlab = ("xx", "yx", "yy", "zx", "zy", "zz")

    pol = np.zeros((6, m.noa*(m.noa+1)//2))
    for ab, a, b in pairs(m.noa):
        for ij, i, j in pairs(3):
            #from pdb import set_trace; set_trace()
            i1, i2 = diff[i]
            j1, j2 = diff[j]
            pol[ij, ab] += (rMP[i+1, j1, ab] - rMP[i+1, j2, ab]
                        +   rMP[j+1, i1, ab] - rMP[j+1, i2, ab])/(4*ff)
            if ab in bonds:
                pol[ij, ab] -= (R[a][i]-R[b][i])*(rMP[0, j1, ab] - rMP[0, j2, ab])/(2*ff)
            assert_(Aref[ij, ab], pol[ij, ab], text="%s%s"%(ablab[ab], ijlab[ij]))

def test_polarizability_allbonds_atoms():
    m = loprop.MolFrag(tmpdir, pf=mcpf, sf=mcsf)

    Aab = m.Aab + m.dAab
    noa = m.noa

    Acmp=full.matrix(Aref.shape)
    
    ab = 0
    for a in range(3):
        for b in range(a):
            Acmp[:, ab] = (Aab[:, :, a, b] + Aab[:, :, b, a]).pack()
            ab += 1
        Acmp[:, ab] = Aab[:, :, a, a].pack()
        ab += 1
    # atoms
    assert_(Aref[:, 0], Acmp[:, 0], .005)
    assert_(Aref[:, 2], Acmp[:, 2], .005)
    assert_(Aref[:, 5], Acmp[:, 5], .005)

def test_polarizability_allbonds_bonds():
    m = loprop.MolFrag(tmpdir, pf=mcpf, sf=mcsf)

    Aab = m.Aab + m.dAab/2
    noa = m.noa

    Acmp=full.matrix(Aref.shape)
    
    ab = 0
    for a in range(3):
        for b in range(a):
            Acmp[:, ab] = (Aab[:, :, a, b] + Aab[:, :, b, a]).pack()
            ab += 1
        Acmp[:, ab] = Aab[:, :, a, a].pack()
        ab += 1
    # atoms
    assert_(Aref[:, 1], Acmp[:, 1], .150, 'H1O')
    assert_(Aref[:, 3], Acmp[:, 3], .150, 'H2O')
    assert_(Aref[:, 4], Acmp[:, 4], .005, 'H2H1')
    

def nozest_polarizability_nobonds():
    M = loprop.MolFrag(tmpdir, pol=True)
    O = [
    3.87739525,
    0.00018217, 3.00410918,
    0.00010384, 0.00020122, 3.52546819
    ]

    H1 = [
    2.15784091,
    0.00023848, 1.05022368,
    1.17177159, 0.00059985, 1.52065218
    ]

    H2 = [
    2.15754005,
    0.00023941,  1.05022240,
   -1.17157425, -0.00087738,  1.52065217
    ]

    Aref = full.init([O, H1, H2])

    Asym = full.matrix(Aref.shape)
    #a > b, i>j
    Aa = M.Aab.sum(axis=2).view(full.matrix)
    for a in range(3):
        Asym[:, a] = Aa[:,:,a].pack()
    print Aref, Asym, Aref - Asym
    assert np.allclose(Aref, Asym, atol=1e-5)

    print M.Aab
    Aaa = M.Aab.sum(axis=2).view(full.matrix)
    #symmetry packed
    Asp = full.matrix((6, 3))
    for a in range(3):
        Asp[:, a] = Aaa[a].pack()

    print Aref, Asp, Aref-Asp
    #assert np.allclose(Aref, Asp, atol=1e-5)
    assert True


if __name__ == "__main__":
    test_default_gauge()