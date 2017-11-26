from codecs import open
from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='centerline',
    version='0.3',
    description='Calculate the centerline of a polygon',
    long_description=long_description,
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: GIS',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    url='https://github.com/fitodic/centerline.git',
    author='Filip Todic',
    author_email='todic.filip@gmail.com',
    license='MIT',
    packages=['centerline'],
    install_requires=[
        'GDAL>=2.0.1',
        'Fiona>=1.7.0',
        'Shapely>=1.5.13',
        'numpy>=1.10.4',
        'scipy>=0.16.1',
    ],
    extras_require={
        'dev': [
            'pylama'
            'ipdb',
            'ipython[all]',
            'notebook',
            'jupyter',
            'isort'
        ],
        'test': [
            'coverage',
            'pytest>=3.0.0',
            'pytest-cov',
            'pytest-sugar',
            'pytest-runner'
        ],
    },
    scripts=[
        'bin/create_centerlines',
    ],
    include_package_data=True,
    zip_safe=False,
)
