"""A Library for accessing the Science Logic EM7.
"""

from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyem7',
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
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords=['library', 'rest', 'sciencelogic', 'em7'],
    packages=find_packages(exclude=['contrib', 'docs', 'tests*', 'dist', 'data', 'build',
                                    '.tox', '*.egg-info']),
    install_requires=['requests==2.7.0'],
    extras_require={
        'dev': ['requests_mock',
                'nose'],
        'test': ['requests_mock',
                 'nose'],
    },
)
