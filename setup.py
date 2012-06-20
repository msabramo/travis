# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='travis',
    version='0.0.1',
    description='Travis-CI service api wrapper for python',
    long_description=readme,
    author='Pedro Rodrigues',
    author_email='medecau@gmail.com',
    url='https://github.com/medecau/travis',
    license=license,
    packages=find_packages(exclude=('tests')),
    install_requires=['requests'],
    test_suite='tests',
)

