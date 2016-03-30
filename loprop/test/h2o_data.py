from ..daltools.util.full import init

Z = [8., 1., 1.]
Rc = init([0.00000000,  0.00000000,  0.48860959])
Dtot = [0, 0, -0.76539388]
Daa = init([
    [ 0.00000000, 0.00000000, -0.28357300],
    [ 0.15342658, 0.00000000,  0.12734703],
    [-0.15342658, 0.00000000,  0.12734703],
])
QUc = init([-7.31176220, 0., 0., -5.43243232, 0., -6.36258665])
QUN = init([4.38968295, 0., 0., 0., 0., 1.75400326])
QUaa = init([
    [-3.29253618, 0.00000000, 0.00000000, -4.54316657, 0.00000000, -4.00465380],
    [-0.13213704, 0.00000000, 0.24980518, -0.44463288, 0.00000000, -0.26059139],
    [-0.13213704, 0.00000000,-0.24980518, -0.44463288, 0.00000000, -0.26059139]
])
Fab = init([
    [-0.11E-03,  0.55E-04,  0.55E-04],
    [ 0.55E-04, -0.55E-04,  0.16E-30],
    [ 0.55E-04,  0.16E-30, -0.55E-04]
    ])
Lab = init([
    [0.11E-03, 0.28E-03, 0.28E-03],
    [0.28E-03, 0.17E-03, 0.22E-03],
    [0.28E-03, 0.22E-03, 0.17E-03]
    ])
la = init([
[0.0392366,-27.2474016 , 27.2081650],
[0.0358964, 27.2214515 ,-27.2573479],
[0.01211180, -0.04775576,  0.03564396],
[0.01210615, -0.00594030, -0.00616584],
[10.69975088, -5.34987556, -5.34987532],
[-10.6565582,  5.3282791 ,  5.3282791]
])

O = [
0.76145382,
-0.00001648, 1.75278523,
-0.00007538, 0.00035773, 1.39756345
]

H1O = [
3.11619527,
0.00019911, 1.25132346,
2.11363325, 0.00111442, 2.12790474
]

H1 = [
0.57935224,
0.00018083, 0.43312326,
0.11495546, 0.00004222, 0.45770123
]

H2O = [
3.11568759,
0.00019821,  1.25132443,
-2.11327482, -0.00142746, 2.12790473
]
H2H1 = [
0.04078206,
-0.00008380, -0.01712262,
-0.00000098,  0.00000084, -0.00200285
]
H2 = [
0.57930522,
0.00018221,  0.43312149,
-0.11493635, -0.00016407,  0.45770123
]

Aab = init([O, H1O, H1, H2O, H2H1, H2])
Aa = init([
    [ 3.87739525, 0.00018217, 3.00410918, 0.00010384, 0.00020122, 3.52546819 ],
    [ 2.15784091, 0.00023848, 1.05022368, 1.17177159, 0.00059985, 1.52065218 ],
    [ 2.15754005, 0.00023941,  1.05022240, -1.17157425, -0.00087738,  1.52065217 ]
])

ff = 0.001
rMP = init([
#O
    [
    [-8.70343886, 0.00000000,  0.00000000, -0.39827574, -3.68114747,  0.00000000,  0.00000000, -4.58632761,  0.00000000, -4.24741556],
    [-8.70343235, 0.00076124,  0.00000000, -0.39827535, -3.68114147,  0.00000000,  0.00193493, -4.58631888,  0.00000000, -4.24741290],
    [-8.70343291,-0.00076166,  0.00000000, -0.39827505, -3.68114128,  0.00000000, -0.00193603, -4.58631789,  0.00000000, -4.24741229],
    [-8.70343685,-0.00000006,  0.00175241, -0.39827457, -3.68114516,  0.00000000,  0.00000161, -4.58632717,  0.00053363, -4.24741642],
    [-8.70343685, 0.00000000, -0.00175316, -0.39827456, -3.68114514,  0.00000000,  0.00000000, -4.58632711, -0.00053592, -4.24741639],
    [-8.70166502, 0.00000000,  0.00000144, -0.39688042, -3.67884999,  0.00000000,  0.00000000, -4.58395384,  0.00000080, -4.24349307],
    [-8.70520554, 0.00000000,  0.00000000, -0.39967554, -3.68344246,  0.00000000,  0.00000000, -4.58868836,  0.00000000, -4.25134640],
    ],
#H1O                                                                                                                    
    [
    [ 0.00000000, 0.10023328,  0.00000000,  0.11470275,  0.53710687,  0.00000000,  0.43066796,  0.04316104,  0.00000000,  0.36285790],
    [ 0.00150789, 0.10111974,  0.00000000,  0.11541803,  0.53753360,  0.00000000,  0.43120945,  0.04333774,  0.00000000,  0.36314215],
    [-0.00150230, 0.09934695,  0.00000000,  0.11398581,  0.53667861,  0.00000000,  0.43012612,  0.04298361,  0.00000000,  0.36257249],
    [ 0.00000331, 0.10023328,  0.00125017,  0.11470067,  0.53710812, -0.00006107,  0.43066944,  0.04316020,  0.00015952,  0.36285848],
    [ 0.00000100, 0.10023249, -0.00125247,  0.11470042,  0.53710716,  0.00006135,  0.43066837,  0.04316018, -0.00015966,  0.36285788],
    [ 0.00088692, 0.10059268, -0.00000064,  0.11590322,  0.53754715, -0.00000006,  0.43071206,  0.04334198, -0.00000015,  0.36330053],
    [-0.00088334, 0.09987383,  0.00000000,  0.11350091,  0.53666602,  0.00000000,  0.43062352,  0.04297910,  0.00000000,  0.36241326],
    ],
#H1                                                                                                                     
    [
    [-0.64828057, 0.10330994,  0.00000000,  0.07188960, -0.47568174,  0.00000000, -0.03144252, -0.46920879,  0.00000000, -0.50818752],
    [-0.64978846, 0.10389186,  0.00000000,  0.07204462, -0.47729337,  0.00000000, -0.03154159, -0.47074619,  0.00000000, -0.50963693],
    [-0.64677827, 0.10273316,  0.00000000,  0.07173584, -0.47408263,  0.00000000, -0.03134407, -0.46768337,  0.00000000, -0.50674873],
    [-0.64828388, 0.10331167,  0.00043314,  0.07189029, -0.47568875, -0.00023642, -0.03144270, -0.46921635, -0.00021728, -0.50819386],
    [-0.64828157, 0.10331095, -0.00043311,  0.07188988, -0.47568608,  0.00023641, -0.03144256, -0.46921346,  0.00021729, -0.50819095],
    [-0.64916749, 0.10338629, -0.00000024,  0.07234862, -0.47634698,  0.00000013, -0.03159569, -0.47003679,  0.00000011, -0.50936853],
    [-0.64739723, 0.10323524,  0.00000000,  0.07143322, -0.47502412,  0.00000000, -0.03129003, -0.46838912,  0.00000000, -0.50701656],
    ],
#H2O                                                                                                                    
    [
    [ 0.00000000,-0.10023328,  0.00000000,  0.11470275,  0.53710687,  0.00000000, -0.43066796,  0.04316104,  0.00000000,  0.36285790],
    [-0.00150139,-0.09934749,  0.00000000,  0.11398482,  0.53667874,  0.00000000, -0.43012670,  0.04298387,  0.00000000,  0.36257240],
    [ 0.00150826,-0.10112008,  0.00000000,  0.11541676,  0.53753350,  0.00000000, -0.43120982,  0.04333795,  0.00000000,  0.36314186],
    [-0.00000130,-0.10023170,  0.00125018,  0.11470018,  0.53710620,  0.00006107, -0.43066732,  0.04316017,  0.00015952,  0.36285728],
    [ 0.00000101,-0.10023249, -0.00125247,  0.11470042,  0.53710716, -0.00006135, -0.43066838,  0.04316018, -0.00015966,  0.36285788],
    [ 0.00088692,-0.10059268, -0.00000064,  0.11590322,  0.53754715,  0.00000006, -0.43071206,  0.04334198, -0.00000015,  0.36330053],
    [-0.00088334,-0.09987383,  0.00000000,  0.11350091,  0.53666602,  0.00000000, -0.43062352,  0.04297910,  0.00000000,  0.36241326],
    ],
#H2H1                                                                                                                   
    [
    [ 0.00000000, 0.00000000,  0.00000000, -0.00378789,  0.00148694,  0.00000000,  0.00000000,  0.00599079,  0.00000000,  0.01223822],
    [ 0.00000000, 0.00004089,  0.00000000, -0.00378786,  0.00148338,  0.00000000, -0.00004858,  0.00599281,  0.00000000,  0.01224094],
    [ 0.00000000,-0.00004067,  0.00000000, -0.00378785,  0.00148341,  0.00000000,  0.00004861,  0.00599277,  0.00000000,  0.01224093],
    [ 0.00000000,-0.00000033, -0.00001707, -0.00378763,  0.00149017,  0.00000000,  0.00000001,  0.00599114, -0.00001229,  0.01223979],
    [ 0.00000000, 0.00000000,  0.00001717, -0.00378763,  0.00149019,  0.00000000,  0.00000000,  0.00599114,  0.00001242,  0.01223980],
    [ 0.00000000, 0.00000000,  0.00000000, -0.00378978,  0.00141897,  0.00000000,  0.00000000,  0.00590445,  0.00000002,  0.01210376],
    [ 0.00000000, 0.00000000,  0.00000000, -0.00378577,  0.00155694,  0.00000000,  0.00000000,  0.00607799,  0.00000000,  0.01237393],
    ],
#H2
    [
    [-0.64828057,-0.10330994,  0.00000000,  0.07188960, -0.47568174,  0.00000000,  0.03144252, -0.46920879,  0.00000000, -0.50818752],
    [-0.64677918,-0.10273369,  0.00000000,  0.07173576, -0.47408411,  0.00000000,  0.03134408, -0.46768486,  0.00000000, -0.50674986],
    [-0.64978883,-0.10389230,  0.00000000,  0.07204446, -0.47729439,  0.00000000,  0.03154159, -0.47074717,  0.00000000, -0.50963754],
    [-0.64827927,-0.10331022,  0.00043313,  0.07188947, -0.47568340,  0.00023642,  0.03144242, -0.46921057, -0.00021727, -0.50818804],
    [-0.64828158,-0.10331095, -0.00043311,  0.07188988, -0.47568609, -0.00023641,  0.03144256, -0.46921348,  0.00021729, -0.50819097],
    [-0.64916749,-0.10338629, -0.00000024,  0.07234862, -0.47634698, -0.00000013,  0.03159569, -0.47003679,  0.00000011, -0.50936853],
    [-0.64739723,-0.10323524,  0.00000000,  0.07143322, -0.47502412,  0.00000000,  0.03129003, -0.46838912,  0.00000000, -0.50701656]
    ]
    ])

Am = init([
     [8.186766009140, 0., 0.], 
     [0., 5.102747935447, 0.], 
     [0., 0., 6.565131856389]
     ])

Amw = init([
     [11.98694996213, 0., 0.], 
     [0., 4.403583657738, 0.], 
     [0., 0., 2.835142058626]
     ])

R = [
        [ 0.00000,   0.00000,  0.69801],
        [-1.48150,   0.00000, -0.34901],
        [ 1.48150,   0.00000, -0.34901]
        ]
Qtot = -10.0
Q = rMP[0, 0, (0, 2, 5)]
D = rMP[1:4, 0, :]
QU = rMP[4:, 0, :]
dQa = rMP[0, :, (0,2,5)]
dQab = rMP[0, :, (1, 3, 4)]

#These are string data for testing potential file
PAn0 = """AU
3 -1 0 1
1     0.000     0.000     0.698
1    -1.481     0.000    -0.349
1     1.481     0.000    -0.349
"""
POTFILE_BY_ATOM_n0_ANGSTROM = """AA
3 -1 0 1
1     0.000     0.000     0.369
1    -0.784     0.000    -0.185
1     0.784     0.000    -0.185
"""
PAn0b = """AU
5 -1 0 1
1     0.000     0.000     0.698
1    -0.741     0.000     0.175
1    -1.481     0.000    -0.349
1     0.741     0.000     0.175
1     1.481     0.000    -0.349
"""
PA00 = """AU
3 0 0 1
1     0.000     0.000     0.698    -0.703
1    -1.481     0.000    -0.349     0.352
1     1.481     0.000    -0.349     0.352
"""
PA00b = """AU
5 0 0 1
1     0.000     0.000     0.698    -0.703
1    -0.741     0.000     0.175     0.000
1    -1.481     0.000    -0.349     0.352
1     0.741     0.000     0.175     0.000
1     1.481     0.000    -0.349     0.352
"""
PA10 = """AU
3 1 0 1
1     0.000     0.000     0.698    -0.703    -0.000     0.000    -0.284
1    -1.481     0.000    -0.349     0.352     0.153     0.000     0.127
1     1.481     0.000    -0.349     0.352    -0.153     0.000     0.127
"""
PA10b = """AU
5 1 0 1
1     0.000     0.000     0.698    -0.703    -0.000     0.000    -0.398
1    -0.741     0.000     0.175     0.000     0.100     0.000     0.115
1    -1.481     0.000    -0.349     0.352     0.103     0.000     0.070
1     0.741     0.000     0.175     0.000    -0.100     0.000     0.115
1     1.481     0.000    -0.349     0.352    -0.103     0.000     0.070
"""
PA01b = """AU
5 0 1 1
1     0.000     0.000     0.698    -0.703     1.302
1    -0.741     0.000     0.175     0.000     2.165
1    -1.481     0.000    -0.349     0.352     0.494
1     0.741     0.000     0.175     0.000     2.165
1     1.481     0.000    -0.349     0.352     0.494
"""
PA02 = """AU
3 0 2 1
1     0.000     0.000     0.698    -0.703     3.875    -0.000    -0.000     3.000    -0.000     3.524
1    -1.481     0.000    -0.349     0.352     2.156    -0.000     1.106     1.051    -0.000     1.520
1     1.481     0.000    -0.349     0.352     2.156    -0.000    -1.106     1.051    -0.000     1.520
"""
PA02b = """AU
5 0 2 1
1     0.000     0.000     0.698    -0.703     0.761     0.000     0.000     1.748     0.000     1.397
1    -0.741     0.000     0.175     0.000     3.114    -0.000     1.981     1.252    -0.000     2.127
1    -1.481     0.000    -0.349     0.352     0.599    -0.000     0.115     0.425    -0.000     0.457
1     0.741     0.000     0.175     0.000     3.114    -0.000    -1.981     1.252    -0.000     2.127
1     1.481     0.000    -0.349     0.352     0.599    -0.000    -0.115     0.425    -0.000     0.457
"""
PA20 = """AU
3 2 0 1
1     0.000     0.000     0.698    -0.703    -0.000     0.000    -0.284    -3.293     0.000    -0.000    -4.543    -0.000    -4.005
1    -1.481     0.000    -0.349     0.352     0.153     0.000     0.127    -0.132     0.000     0.250    -0.445     0.000    -0.261
1     1.481     0.000    -0.349     0.352    -0.153     0.000     0.127    -0.132    -0.000    -0.250    -0.445     0.000    -0.261
"""
PA21 = """AU
3 2 1 1
1     0.000     0.000     0.698    -0.703    -0.000     0.000    -0.284    -3.293     0.000    -0.000    -4.543    -0.000    -4.005     3.466
1    -1.481     0.000    -0.349     0.352     0.153     0.000     0.127    -0.132     0.000     0.250    -0.445     0.000    -0.261     1.576
1     1.481     0.000    -0.349     0.352    -0.153     0.000     0.127    -0.132    -0.000    -0.250    -0.445     0.000    -0.261     1.576
"""
PA22 = """AU
3 2 2 1
1     0.000     0.000     0.698    -0.703    -0.000     0.000    -0.284    -3.293     0.000    -0.000    -4.543    -0.000    -4.005     3.875    -0.000    -0.000     3.000    -0.000     3.524
1    -1.481     0.000    -0.349     0.352     0.153     0.000     0.127    -0.132     0.000     0.250    -0.445     0.000    -0.261     2.156    -0.000     1.106     1.051    -0.000     1.520
1     1.481     0.000    -0.349     0.352    -0.153     0.000     0.127    -0.132    -0.000    -0.250    -0.445     0.000    -0.261     2.156    -0.000    -1.106     1.051    -0.000     1.520
"""

OUTPUT_n0_1 = """\
---------------
Atomic domain 1
---------------
Domain center:         0.00000  0.00000  0.69801
"""

OUTPUT_n0_1_ANGSTROM = """\
---------------
Atomic domain 1
---------------
Domain center:         0.00000  0.00000  0.36937
"""

OUTPUT_00_1 = OUTPUT_n0_1 + """\
Nuclear charge:        8.00000
Electronic charge:    -8.70344
Total charge:         -0.70344
"""

OUTPUT_10_1 = OUTPUT_00_1 + """\
Electronic dipole     -0.00000  0.00000 -0.28357
"""

OUTPUT_20_1 = OUTPUT_10_1 + """\
Electronic quadrupole -3.29254  0.00000 -0.00000 -4.54317  0.00000 -4.00466
"""

OUTPUT_01_1 = OUTPUT_00_1 + """\
Isotropic polarizablity (w=0)  3.46639
"""

OUTPUT_02_1 = OUTPUT_00_1 + """\
Electronic polarizability (w=0)  3.87468 -0.00000  3.00027 -0.00000 -0.00000  3.52422
"""

OUTPUT_BY_ATOM_n0 = """\
---------------
Atomic domain 1
---------------
Domain center:            0.00000     0.00000     0.69801
Nuclear charge:           8.00000

---------------
Atomic domain 2
---------------
Domain center:           -1.48150     0.00000    -0.34901
Nuclear charge:           1.00000

---------------
Atomic domain 3
---------------
Domain center:            1.48150     0.00000    -0.34901
Nuclear charge:           1.00000

---------
Molecular
---------
Domain center:            0.00000     0.00000     0.48861
Nuclear charge:          10.00000"""

OUTPUT_BY_ATOM_n0_ANGSTROM = """\
---------------
Atomic domain 1
---------------
Domain center:            0.00000     0.00000     0.36937
Nuclear charge:           8.00000

---------------
Atomic domain 2
---------------
Domain center:           -0.78398     0.00000    -0.18469
Nuclear charge:           1.00000

---------------
Atomic domain 3
---------------
Domain center:            0.78398     0.00000    -0.18469
Nuclear charge:           1.00000

---------
Molecular
---------
Domain center:            0.00000     0.00000     0.25856
Nuclear charge:          10.00000"""


OUTPUT_BY_ATOM_00 = """\
---------------
Atomic domain 1
---------------
Domain center:            0.00000     0.00000     0.69801
Nuclear charge:           8.00000
Electronic charge:       -8.70344
Total charge:            -0.70344

---------------
Atomic domain 2
---------------
Domain center:           -1.48150     0.00000    -0.34901
Nuclear charge:           1.00000
Electronic charge:       -0.64828
Total charge:             0.35172

---------------
Atomic domain 3
---------------
Domain center:            1.48150     0.00000    -0.34901
Nuclear charge:           1.00000
Electronic charge:       -0.64828
Total charge:             0.35172

---------
Molecular
---------
Domain center:            0.00000     0.00000     0.48861
Nuclear charge:          10.00000
Electronic charge:      -10.00000
Total charge:             0.00000"""

OUTPUT_BY_ATOM_10 = """\
---------------
Atomic domain 1
---------------
Domain center:            0.00000     0.00000     0.69801
Nuclear charge:           8.00000
Electronic charge:       -8.70344
Total charge:            -0.70344
Electronic dipole        -0.00000     0.00000    -0.28357
Electronic dipole norm     0.28357

---------------
Atomic domain 2
---------------
Domain center:           -1.48150     0.00000    -0.34901
Nuclear charge:           1.00000
Electronic charge:       -0.64828
Total charge:             0.35172
Electronic dipole         0.15343     0.00000     0.12735
Electronic dipole norm     0.19939

---------------
Atomic domain 3
---------------
Domain center:            1.48150     0.00000    -0.34901
Nuclear charge:           1.00000
Electronic charge:       -0.64828
Total charge:             0.35172
Electronic dipole        -0.15343     0.00000     0.12735
Electronic dipole norm     0.19939

---------
Molecular
---------
Domain center:            0.00000     0.00000     0.48861
Nuclear charge:          10.00000
Electronic charge:      -10.00000
Total charge:             0.00000
Electronic dipole        -0.00000     0.00000    -0.02888
Gauge   dipole            0.00000    -0.00000    -0.73651
Total   dipole           -0.00000     0.00000    -0.76539"""


OUTPUT_BY_ATOM_20 = """\
---------------
Atomic domain 1
---------------
Domain center:            0.00000     0.00000     0.69801
Nuclear charge:           8.00000
Electronic charge:       -8.70344
Total charge:            -0.70344
Electronic dipole        -0.00000     0.00000    -0.28357
Electronic dipole norm     0.28357
Electronic quadrupole    -3.29254    -0.00000    -0.00000    -4.54317    -0.00000    -4.00466

---------------
Atomic domain 2
---------------
Domain center:           -1.48150     0.00000    -0.34901
Nuclear charge:           1.00000
Electronic charge:       -0.64828
Total charge:             0.35172
Electronic dipole         0.15343     0.00000     0.12735
Electronic dipole norm     0.19939
Electronic quadrupole    -0.13214     0.00000     0.24981    -0.44463     0.00000    -0.26059

---------------
Atomic domain 3
---------------
Domain center:            1.48150     0.00000    -0.34901
Nuclear charge:           1.00000
Electronic charge:       -0.64828
Total charge:             0.35172
Electronic dipole        -0.15343     0.00000     0.12735
Electronic dipole norm     0.19939
Electronic quadrupole    -0.13214    -0.00000    -0.24981    -0.44463     0.00000    -0.26059

---------
Molecular
---------
Domain center:            0.00000     0.00000     0.48861
Nuclear charge:          10.00000
Electronic charge:      -10.00000
Total charge:             0.00000
Electronic dipole        -0.00000     0.00000    -0.02888
Gauge   dipole            0.00000    -0.00000    -0.73651
Total   dipole           -0.00000     0.00000    -0.76539
Electronic quadrupole    -7.31176    -0.00000    -0.00000    -5.43243    -0.00000    -6.36259
Nuclear    quadrupole     4.38968     0.00000     0.00000     0.00000     0.00000     1.75400
Total      quadrupole    -2.92208    -0.00000    -0.00000    -5.43243    -0.00000    -4.60859"""


OUTPUT_BY_ATOM_01 = """\
---------------
Atomic domain 1
---------------
Domain center:            0.00000     0.00000     0.69801
Nuclear charge:           8.00000
Electronic charge:       -8.70344
Total charge:            -0.70344
Isotropic polarizablity (w=0)     3.46639
Electronic polarizability (w=0)     3.87468    -0.00000     3.00027    -0.00000    -0.00000     3.52422

---------------
Atomic domain 2
---------------
Domain center:           -1.48150     0.00000    -0.34901
Nuclear charge:           1.00000
Electronic charge:       -0.64828
Total charge:             0.35172
Isotropic polarizablity (w=0)     1.57591
Electronic polarizability (w=0)     2.15604    -0.00000     1.05124     1.10564    -0.00000     1.52045

---------------
Atomic domain 3
---------------
Domain center:            1.48150     0.00000    -0.34901
Nuclear charge:           1.00000
Electronic charge:       -0.64828
Total charge:             0.35172
Isotropic polarizablity (w=0)     1.57591
Electronic polarizability (w=0)     2.15604    -0.00000     1.05124    -1.10564    -0.00000     1.52045

---------
Molecular
---------
Domain center:            0.00000     0.00000     0.48861
Nuclear charge:          10.00000
Electronic charge:      -10.00000
Total charge:             0.00000
Polarizability av (0)        6.61822
Polarizability (0)           8.18677    -0.00000     5.10275    -0.00000    -0.00000     6.56513"""

OUTPUT_BY_BOND_n0 = """\
---------
Atom    1
---------
Atom center:            0.00000     0.00000     0.69801
Nuclear charge:         8.00000

-----------
Bond    2 1
-----------
Bond center:           -0.74075     0.00000     0.17450

---------
Atom    2
---------
Atom center:           -1.48150     0.00000    -0.34901
Nuclear charge:         1.00000

-----------
Bond    3 1
-----------
Bond center:            0.74075     0.00000     0.17450

-----------
Bond    3 2
-----------
Bond center:            0.00000     0.00000    -0.34901

---------
Atom    3
---------
Atom center:            1.48150     0.00000    -0.34901
Nuclear charge:         1.00000

---------
Molecular
---------
Domain center:            0.00000     0.00000     0.48861
Nuclear charge:          10.00000"""

OUTPUT_BY_BOND_00 = """\
---------
Atom    1
---------
Atom center:            0.00000     0.00000     0.69801
Nuclear charge:         8.00000
Electronic charge:       -8.70344
Total charge:            -0.70344

-----------
Bond    2 1
-----------
Bond center:           -0.74075     0.00000     0.17450
Electronic charge:        0.00000
Total charge:             0.00000

---------
Atom    2
---------
Atom center:           -1.48150     0.00000    -0.34901
Nuclear charge:         1.00000
Electronic charge:       -0.64828
Total charge:             0.35172

-----------
Bond    3 1
-----------
Bond center:            0.74075     0.00000     0.17450
Electronic charge:        0.00000
Total charge:             0.00000

-----------
Bond    3 2
-----------
Bond center:            0.00000     0.00000    -0.34901
Electronic charge:        0.00000
Total charge:             0.00000

---------
Atom    3
---------
Atom center:            1.48150     0.00000    -0.34901
Nuclear charge:         1.00000
Electronic charge:       -0.64828
Total charge:             0.35172

---------
Molecular
---------
Domain center:            0.00000     0.00000     0.48861
Nuclear charge:          10.00000
Electronic charge:      -10.00000
Total charge:            -0.00000"""

OUTPUT_BY_BOND_10 = """\
---------
Atom    1
---------
Atom center:            0.00000     0.00000     0.69801
Nuclear charge:         8.00000
Electronic charge:       -8.70344
Total charge:            -0.70344
Electronic dipole        -0.00000    -0.00000    -0.39828
Electronic dipole norm     0.39828

-----------
Bond    2 1
-----------
Bond center:           -0.74075     0.00000     0.17450
Electronic charge:        0.00000
Total charge:             0.00000
Electronic dipole         0.10023    -0.00000     0.11470
Electronic dipole norm     0.15233

---------
Atom    2
---------
Atom center:           -1.48150     0.00000    -0.34901
Nuclear charge:         1.00000
Electronic charge:       -0.64828
Total charge:             0.35172
Electronic dipole         0.10331     0.00000     0.07189
Electronic dipole norm     0.12586

-----------
Bond    3 1
-----------
Bond center:            0.74075     0.00000     0.17450
Electronic charge:        0.00000
Total charge:             0.00000
Electronic dipole        -0.10023    -0.00000     0.11470
Electronic dipole norm     0.15233

-----------
Bond    3 2
-----------
Bond center:            0.00000     0.00000    -0.34901
Electronic charge:        0.00000
Total charge:             0.00000
Electronic dipole        -0.00000    -0.00000    -0.00379
Electronic dipole norm     0.00379

---------
Atom    3
---------
Atom center:            1.48150     0.00000    -0.34901
Nuclear charge:         1.00000
Electronic charge:       -0.64828
Total charge:             0.35172
Electronic dipole        -0.10331    -0.00000     0.07189
Electronic dipole norm     0.12586

---------
Molecular
---------
Domain center:            0.00000     0.00000     0.48861
Nuclear charge:          10.00000
Electronic charge:      -10.00000
Total charge:            -0.00000
Electronic dipole        -0.00000    -0.00000    -0.02888
Gauge   dipole            0.00000    -0.00000    -0.73651
Total   dipole           -0.00000    -0.00000    -0.76539"""

OUTPUT_BY_BOND_n1 = """\
---------
Atom    1
---------
Atom center:            0.00000     0.00000     0.69801
Nuclear charge:         8.00000
Isotropic polarizability (0)     1.30184

-----------
Bond    2 1
-----------
Bond center:           -0.74075     0.00000     0.17450
Isotropic polarizability (0)     2.16455

---------
Atom    2
---------
Atom center:           -1.48150     0.00000    -0.34901
Nuclear charge:         1.00000
Isotropic polarizability (0)     0.48998

-----------
Bond    3 1
-----------
Bond center:            0.74075     0.00000     0.17450
Isotropic polarizability (0)     2.16455

-----------
Bond    3 2
-----------
Bond center:            0.00000     0.00000    -0.34901
Isotropic polarizability (0)     0.00732

---------
Atom    3
---------
Atom center:            1.48150     0.00000    -0.34901
Nuclear charge:         1.00000
Isotropic polarizability (0)     0.48998

---------
Molecular
---------
Domain center:            0.00000     0.00000     0.48861
Nuclear charge:          10.00000
Polarizability av (0)        6.61822
Polarizability (0)           8.18677    -0.00000     5.10275    -0.00000    -0.00000     6.56513"""

OUTPUT_BY_BOND_n2 = """\
---------
Atom    1
---------
Atom center:            0.00000     0.00000     0.69801
Nuclear charge:         8.00000
Isotropic polarizability (0)     1.30184
Polarizability (0)            0.76086     0.00000     1.74791     0.00000     0.00000     1.39676

-----------
Bond    2 1
-----------
Bond center:           -0.74075     0.00000     0.17450
Isotropic polarizability (0)     2.16455
Polarizability (0)      
     3.11382    -0.00000     1.25236     1.98132    -0.00000     2.12747

---------
Atom    2
---------
Atom center:           -1.48150     0.00000    -0.34901
Nuclear charge:         1.00000
Isotropic polarizability (0)     0.48998
Polarizability (0)            0.57859    -0.00000     0.43361     0.11498    -0.00000     0.45773

-----------
Bond    3 1
-----------
Bond center:            0.74075     0.00000     0.17450
Isotropic polarizability (0)     2.16455
Polarizability (0)      
     3.11382    -0.00000     1.25236    -1.98132    -0.00000     2.12747

-----------
Bond    3 2
-----------
Bond center:            0.00000     0.00000    -0.34901
Isotropic polarizability (0)     0.00732
Polarizability (0)      
     0.04109     0.00000    -0.01709     0.00000     0.00000    -0.00202

---------
Atom    3
---------
Atom center:            1.48150     0.00000    -0.34901
Nuclear charge:         1.00000
Isotropic polarizability (0)     0.48998
Polarizability (0)            0.57859    -0.00000     0.43361    -0.11498    -0.00000     0.45773

---------
Molecular
---------
Domain center:            0.00000     0.00000     0.48861
Nuclear charge:          10.00000
Polarizability av (0)        6.61822
Polarizability (0)           8.18677    -0.00000     5.10275    -0.00000    -0.00000     6.56513"""

import numpy
T1 = numpy.loadtxt('T1')
