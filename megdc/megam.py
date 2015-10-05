import os
import sys
import argparse


def install(args):
    print "install called"

def sample():
    print "hello world"

def make(parser):
    """ Installing Megam Packages on remote host"""
    
    sample()
    version = parser.add_mutually_exclusive_group()
    
    version.add_argument(
        '--stable',
        nargs='?',
        action=StoreVersion,
        metavar='CODENAME',
        help='[DEPRECATED] install a release known as CODENAME\
                (done by default) (default: %(default)s)',
    )

    version.set_defaults(
        stable=None,  
        version_kind='stable',
    )

    parser.add_argument(
        '--megamcommon',
        dest='install_common',
        action='store_true',
        help='install the megam common package only',
    )

    parser.add_argument(
        '--megamnilavu',
        dest='install_nilavu',
        action='store_true',
        help='install the megamnilavu package (megamnilavu includes megam common) only',
    )


    parser.set_defaults(
        func=install,
    )
