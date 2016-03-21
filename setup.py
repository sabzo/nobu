# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
setup(
    name='nobu',
    version='1.0.4',
    description='A Library for turning a raspberry pi into a Server/Access Point',
    long_description=long_description,
    url='https://github.com/sabzo/nobu',
    author='@sabzo',
    author_email='sabelo@sabelo.io',
    license='MIT',
    keywords='raspberypi accesspoint wifi',
    packages=['nobu'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
