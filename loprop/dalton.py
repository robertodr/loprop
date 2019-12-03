import os

from daltools import one, mol, dens, prop, lr, qr, sirifc
from util import full

from .core import MolFrag


class MolFragDalton(MolFrag):

    def __init__(self, tmpdir, **kwargs):
        super().__init__(tmpdir, **kwargs)
        #
        # Dalton files
        #
        self.aooneint = os.path.join(tmpdir, "AOONEINT")
        self.dalton_bas = os.path.join(tmpdir, "DALTON.BAS")
        self.sirifc = os.path.join(tmpdir, "SIRIFC")
        assert sirifc.sirifc(name=self.sirifc).nsym == 1
        self.get_basis_info()
        self.get_isordk()

    def get_basis_info(self):
        """ Obtain basis set info from DALTON.BAS """
        molecule = mol.readin(self.dalton_bas)
        self.cpa = mol.contracted_per_atom(molecule)
        self.cpa_l = mol.contracted_per_atom_l(molecule)
        self.opa = mol.occupied_per_atom(molecule)
        self.noa = len(self.opa)
        #
        # Total number of basis functions and occupied orbitals
        #
        self.nbf = sum(self.cpa)
        self.noc = 0
        for o in self.opa:
            self.noc += len(o)

    def get_isordk(self):
        """
        Get overlap, nuclear charges and coordinates from AOONEINT
        """
        #
        # Data from the ISORDK section in AOONEINT
        #
        isordk = one.readisordk(filename=self.aooneint)
        #
        # Number of nuclei
        #
        N = isordk["nucdep"]
        #
        # MXCENT , Fix dimension defined in nuclei.h
        #
        mxcent = len(isordk["chrn"])
        #
        # Nuclear charges
        #
        self.Z = full.matrix((N,))
        self.Z[:] = isordk["chrn"][:N]
        #
        # Nuclear coordinates
        #
        R = full.matrix((mxcent * 3,))
        R[:] = isordk["cooo"][:]
        self.R = R.reshape((mxcent, 3), order="F")[:N, :]
        #
        # Bond center matrix and half bond vector
        #
        noa = self.noa
        self.Rab = full.matrix((noa, noa, 3))
        self.dRab = full.matrix((noa, noa, 3))
        for a in range(noa):
            for b in range(noa):
                self.Rab[a, b, :] = (self.R[a, :] + self.R[b, :]) / 2
                self.dRab[a, b, :] = (self.R[a, :] - self.R[b, :]) / 2

    def S(self):
        """
        Get overlap, nuclear charges and coordinates from AOONEINT
        """
        S = one.read("OVERLAP", self.aooneint)
        return S.unpack().unblock()

    @property
    def D(self):
        """
        Density from SIRIFC in blocked loprop basis
        """
        if self._D is not None:
            return self._D

        D = sum(dens.Dab(filename=self.sirifc))
        Ti = self.T.I
        self._D = (Ti * D * Ti.T).subblocked(self.cpa, self.cpa)
        return self._D

    def getprop(self, *args):
        """Read general property matrices to blocked loprop basis"""

        T = self.T
        cpa = self.cpa
        prp = os.path.join(self.tmpdir, "AOPROPER")

        return [
            (T.T * p * T).subblocked(cpa, cpa)
            for p in prop.read(*args, filename=prp, unpack=True)
        ]

    @property
    def Dk(self):
        """Read perturbed densities"""

        if self._Dk is not None:
            return self._Dk

        lab = ["XDIPLEN", "YDIPLEN", "ZDIPLEN"]
        prp = os.path.join(self.tmpdir, "AOPROPER")
        T = self.T
        cpa = self.cpa

        Dkao = lr.Dk(
            *lab,
            freqs=self.freqs,
            tmpdir=self.tmpdir,
            absorption=self.damping,
            lr_vecs=True
        )
        if self.damping:
            Re_Dkao, Im_Dkao = Dkao
            if self.real_pol:
                _Dk = {
                    lw: (T.I * Re_Dkao[lw] * T.I.T).subblocked(cpa, cpa)
                    for lw in Re_Dkao
                }
            elif self.imag_pol:
                _Dk = {
                    lw: (T.I * Im_Dkao[lw] * T.I.T).subblocked(cpa, cpa)
                    for lw in Im_Dkao
                }
            else:
                raise ValueError
        else:
            _Dk = {lw: (T.I * Dkao[lw] * T.I.T).subblocked(cpa, cpa) for lw in Dkao}

        self._Dk = _Dk
        return self._Dk

    @property
    def D2k(self):
        """Read perturbed densities"""

        if self._D2k is not None:
            return self._D2k

        lab = ["XDIPLEN ", "YDIPLEN ", "ZDIPLEN "]
        qrlab = [lab[j] + lab[i] for i in range(3) for j in range(i, 3)]
        prp = os.path.join(self.tmpdir, "AOPROPER")
        T = self.T
        cpa = self.cpa

        Dkao = qr.D2k(*qrlab, freqs=self.freqs, tmpdir=self.tmpdir)
        # print("Dkao.keys", Dkao.keys())
        _D2k = {lw: (T.I * Dkao[lw] * T.I.T).subblocked(cpa, cpa) for lw in Dkao}

        self._D2k = _D2k
        return self._D2k
