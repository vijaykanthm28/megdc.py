from setuptools import setup, find_packages
import os
import sys
import megdc


def read(fname):
  path = os.path.join(os.path.dirname(__file__), fname)
  f = open(path)
  return f.read()

install_requires = []
pyversion = sys.version_info[:2]
if pyversion < (2, 7) or (3, 0) <= pyversion <= (3, 1):
  install_requires.append('argparse')


setup(
    name='megdc',
    version=megdc.__version__,
    packages=find_packages(),

    author='Megam Systems',
    author_email='mvijaykanth@megam.io',
    description='Deploy a hyper converged datacenter using OpenNebula, Megam, Ceph, Docker in your own infrastructure',
    long_description=read('README.rst'),
    license='ApacheV2',
    keywords='megam data center',
    url="https://github.com/megamsys/megdc",

    install_requires=[
        'setuptools',
    ] + install_requires,

    tests_require=[
        'pytest >=2.1.3',
        'mock >=1.0b1',
    ],

    entry_points={

        'console_scripts': [
            'megdc = megdc.cli:main',
        ],

        'megdc.cli': [
            'new = megdc.new:make',
            'megam = megdc.megam:make',
            'one = megdc.one:make',
            'ceph = megdc.ceph:make',
        ],

    },
)
