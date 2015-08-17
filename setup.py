"""A Library for accessing the Science Logic EM7.
"""

from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sample',
    version='0.0.dev1',
    description='Library for accessing the Science Logic EM7',
    long_description=long_description,
    url='https://github.com/the-kid89/pyem7',
    author='Emett Speer',
    author_email='pyem7@emettspeer.com',
    license='BSD-3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: BSD-3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='Libraries REST ScienceLogic EM7',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=['requests==2.7.0'],
    extras_require={
        'dev': ['requests_mock'],
        'test': ['requests_mock'],
    },
)
