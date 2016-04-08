#!/usr/bin/env python
from distutils.core import setup
#from setuptools import setup, find_packages
from glob import glob

setup(
    name="aws-cf-tools",
    version="0.3",
    author="Mike Dixon, Matthew Brettan",
    author_email='mikedix@amazon.com',
    license='TBD',
    description='Extra CLI tools to validate and deploy CloudFormation templates',
    packages=['cfsecuritycheck','cfdeploy'],
    include_package_data=True,
    package_data={'cfsecuritycheck': ['data/UnitTests/*','data/compliance/*']},
    install_requires=['pyyaml', 'boto' ],
    scripts=['cfsecuritycheck/cfsecuritycheck','cfdeploy/cfdeploy'],
)
