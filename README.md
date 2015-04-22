# Loprop for Dalton


This code is an implementation of the LoProp algorithm based on Gagliardi et al., JCP **121**, 4494 (2004) for postprocessing calculation with Dalton (http://daltonprogram.org)

## Requirements

A python installation with `numpy` and `scipy` libraries

## Installation

To install the latest version

```
$ git clone https://github.com/vahtras/loprop.git
$ cd loprop
$ git submodule init
$ git submodule update
$ cd daltools
$ git submodule init
$ git submodule update
```

There are two levels of git submodules (daltools, daltools/util) which require these steps.


## Test

With `nose` installed one can travers all tests which should give

```
$ nosetests
............................................................................................................................................................................................................................................................................................................
----------------------------------------------------------------------
Ran 300 tests in 1.139s
```

## Basic usage

To setup a Dalton calculation for postprocessing with loprop, a typical input file is as follows

```
**DALTON INPUT
.RUN RESP
*END OF GENERAL
**WAVE FUNCTION
.INTERFACE
.HF
**INTEGRAL
.NOSUP
.DIPLEN
.SECMOM
**RESPONSE
*LINEAR
.DIPLEN
*END OF
```

This is required for calculating atomic dipoles, quadrupoles and polarizabilities
One-electron integral files are required that are not normally saved after a Dalton calculation. The dalton program should be executed with the following options

```
$ dalton -get "AOONEINT AOPROPER" hf h2o
```

A sample run with charges and isotropic polarizabilities is
```
$ loprop.py -f hf_h2o.tar.gz -l 0 -a 1
loprop.py -t tmp -l 0 -a 1
AU
3 0 1 1
1     0.000     0.000     0.698    -0.703     3.466
1    -1.481     0.000    -0.349     0.352     1.576
1     1.481     0.000    -0.349     0.352     1.576
```
generating a potential file, with local coordinates, charge and polarizability for each atom.
