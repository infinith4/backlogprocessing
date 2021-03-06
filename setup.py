# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path
# io.open is needed for projects that support Python 2.7
# It ensures open() defaults to text mode with universal newlines,
# and accepts an argument to specify the text encoding
# Python 3 only projects can skip this import
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    description = f.read()

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

requires = [
        'certifi==2018.10.15',
        'chardet==3.0.4',
        'python-dateutil==2.8.1',
        'idna==2.7',
        'jmespath==0.9.3',
        'pybacklog==0.1.7',
        'pytz==2018.7',
        'ruamel.appconfig==0.5.4',
        'ruamel.std.argparse==0.8.1',
        'urllib3==1.24.2',
        'zope.interface==4.6.0',
        'PyYAML==5.1.2'
    ]

setup(
    name='backlogprocessing',
    version='0.0.27',
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/tys-hiroshi/backlogprocessing',
    author='tys-hiroshi',
    author_email='tashiro.hiroshi@toyoko-sys.co.jp',
    license='MIT',
    keywords='backlog pybacklog processing',
    packages=find_packages('backlogprocessing'),  # Required
    package_dir = {'': 'backlogprocessing'},
    install_requires=requires,
    classifiers=[
        'Programming Language :: Python :: 3.7',
    ],
)
