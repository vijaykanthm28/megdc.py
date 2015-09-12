#! /usr/bin/python
import getopt
import sys
import textwrap
from help_text import __help__
from install_method import *

dedented_text = textwrap.dedent(__help__).strip()

options, remainder = getopt.getopt(sys.argv[2:], 'install:uninstall',['all','help','megamnilavu','megamcommon','megamd','megamgulpd','megamgateway'])

#argDict = dict(package)
for opt, arg in options:
    if opt in ('--help','-h'):
        print dedented_text
    elif opt in ('-a', '--all'):
        install_megam()
    elif opt in ('--megamnilavu','megamnilav'):
        install_nilavu()
    elif opt in ('--megamgcommon','megamcommon'):
        install_common()
    elif opt in ('--megamd','megamd'):
        install_megamd()
    elif opt in ('--megamgulpd','megamgulpd'):
        install_gulpd()
    elif opt in ('--megamgateway','megamgateway'):
        install_gateway()
    else :
	print "unable to Locate the package"
	print dedented_text        





