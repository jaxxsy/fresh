#!/usr/bin/env python
from __future__ import (absolute_import, division, print_function, unicode_literals)

import sys
import argparse
import os
import subprocess


def run(package):
    os.system('pip uninstall {}'.format(package))
    os.system('pip install .')

def prepare_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('package', action='append')
    parser.add_argument('--version', action='version', version='%(prog)s ' + VERSION)
    return parser


def main():
    parser = prepare_parser()
    args = parser.parse_args()

    if not os.path.isfile(os.getcwd() + '/setup.py'):
        print ("Error -- fresh should only be used when testing out versions of a local package, and hence NEEDS")
        print ("to be run from a `pip install .`-able location" )
    else:
        run(args.package[0])
    
