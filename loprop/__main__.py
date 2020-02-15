#!/usr/bin/env python
import sys
import os
import argparse
import tempfile


try:
    from loprop import MolFragDalton, timing, penalty_function, shift_function
except ImportError:
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    from loprop import MolFrag, timing, penalty_function

implementations = {
    'dalton': MolFragDalton,
}


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
          '-v', '--verbose',
          dest='verbose', action='store_true', default=False,
          help='print(details [False]'
          )
    parser.add_argument(
          '-t','--tmpdir',
          dest='tmpdir', default=None,
          help='scratch directory'
          )
    parser.add_argument(
          '-f','--daltgz',
          dest='daltgz', default=None,
          help='Dalton restart tar ball [None]'
          )
    parser.add_argument(
          '-p', '--potfile',
          dest='potfile', default='LOPROP.POT',
          help='Potential input file [LOPROP.POT]'
          )
    parser.add_argument(
          '-b','--bond',
          dest='bc', action='store_true',default=False,
          help='include bond centers [False]'
          )
    parser.add_argument(
          '-g','--gauge-center',
          dest='gc', default=None,
          help='gauge center'
          )

    parser.add_argument(
          '-l', '--angular-momentum',
          dest='max_l', type=int, default=2,
          help='Max angular momentum [2]'
          )

    parser.add_argument(
          '-A', '--Anstrom',
          dest='angstrom', action='store_true', default=False,
          help="Output in Angstrom"
          )

    parser.add_argument(
          '-w','--frequencies',
          dest='freqs', default=None,
          help='Dynamic polarizabilities (0.)'
          )

    parser.add_argument(
          '-a','--polarizabilities',
          dest='pol', type=int, default=0,
          help='Localized polarizabilities (1=isotropic, 2=full)'
          )

    parser.add_argument(
          '-B','--hyperpolarizabilities',
          dest='beta', type=int, default=0,
          help='Localized hyperpolarizabilities (1=isotropic, 2=full)'
          )

    parser.add_argument(
          '-s','--screening (alpha)',
          dest='alpha', type=float, default=2.0,
          help='Screening parameter for penalty function'
          )
    
    parser.add_argument(
          '--template',
          action = 'store_true',
          default= False,
          help='Write atomic properties in templated format',
          )
 
    parser.add_argument(
          '--template_full',
          action = 'store_true',
          default= False,
          help='Write atomic properties in templated format, centered on first atom',
          )

    parser.add_argument(
          '--decimal',
          default= 3,
          type = int,
          help='Significant digits for template output.',
          )
    parser.add_argument(
          '--full_loc',
          default= 0,
          type = int,
          help='Significant digits for template output.',
          )

    parser.add_argument(
          '--damping',
          default= None,
          choices = ['real', 'imag'],
          help='Complex polarizabilities (damping); response vectors from ABSVECS',
          )

    parser.add_argument(
          '--driver',
          default= 'dalton',
          choices = ['dalton'],
          help='Quantum Chemistry interface software'
          )

    args = parser.parse_args()

    #
    # Check consistency: present Dalton files
    #
    if args.tmpdir is None:
        tmpdir = tempfile.TemporaryDirectory()
        args.tmpdir = tmpdir.name
    if not os.path.isdir(args.tmpdir):
        print("%s: Directory not found: %s" % (sys.argv[0], args.tmpdir))
        raise SystemExit

    import tarfile
    if args.daltgz:
        tgz = tarfile.open(args.daltgz, 'r:gz')
        tgz.extractall(path=args.tmpdir)
    
    if args.freqs:
        freqs = map(float, args.freqs.split())
    else:
        freqs = (0.0, )
        
    needed_files = ["AOONEINT", "DALTON.BAS", "SIRIFC", "AOPROPER"]
    if args.damping:
        needed_files.append("ABSVECS")
    elif args.pol:
        needed_files.append("RSPVEC")

    for file_ in needed_files:
        df = os.path.join(args.tmpdir, file_)
        if not os.path.isfile(df):
            print("%s: %s does not exists" % (sys.argv[0], df))
            print("Needed Dalton files to run loprop.py:")
            print("\n".join(needed_files))
            raise SystemExit

    if args.gc is not None: 
        #Gauge center
        try:
            #gc = map(float, args.gc.split())
            gc = [float(i) for i in args.gc.split()]
        except(ValueError):
            sys.stderr.write("Gauge center incorrect:%s\n" % args.gc)
            sys.exit(1)
    else:
        gc = None



    t = timing.timing('Loprop')
    #molfrag = implementations[args.driver](
    molfrag = MolFragDalton(
        args.tmpdir, max_l=args.max_l, pf=penalty_function(args.alpha), gc=gc, freqs=freqs,
        damping=args.damping, real_pol=(args.damping == 'real'), imag_pol=(args.damping == 'imag')
        )
    print(molfrag.output_potential_file(
        args.max_l, args.pol, args.beta, args.bc, args.angstrom, decimal = args.decimal
        ))
    if args.template:
        print(molfrag.output_template(
            args.max_l, args.pol, args.beta,
            template_full = args.template_full,
            decimal = args.decimal,
            freqs = freqs,
            full_loc = args.full_loc,
            ))
        
    if args.verbose:
        molfrag.output_by_atom(fmt="%12.5f", max_l=args.max_l, pol=args.pol, hyperpol=args.beta, bond_centers=args.bc, angstrom=args.angstrom)

    print(t)
     
if __name__ == "__main__":
    sys.exit(main())