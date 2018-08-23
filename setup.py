# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='norbert',
    version='0.1.0',
    description='Spectrogram Models',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sigsep/norbert',
    author='Fabian-Robert Stoeter, Antoine Liutkus',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='wiener filter',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[
        'pillow',
        'piexif',
        'soundfile',
        'scipy'
    ],

    extras_require={  # Optional
        'dev': ['check-manifest'],
        'tests': ['pytest', 'coverage', 'pytest-cov', 'pytest-pep8'],
    },

    # entry_points={
    #     'console_scripts': [
    #         'norbert=norbert:quantize',
    #     ],
    # },

    project_urls={  # Optional
        'Bug Reports': 'https://github.com/sigsep/norbert/issues',
    },
)
