"""Setup configuration and dependencies for the TartarSauce library."""

import os
import setuptools

COMMANDS = []

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
PACKAGES = setuptools.find_packages(ROOT_DIR, include=['tartar_sauce*'], exclude=['*test', '*benchmarks'])

# Additional configuration and data files installed with the package
PACKAGE_DATA = {
    'tartar_sauce/test': ['*.json', '*.tar.gz'],
}

# Files external to the package to install on the system.
DATA_FILES = []

REQUIREMENTS_DIR = os.path.dirname(__file__)
REQUIREMENTS_FILE = os.path.join(REQUIREMENTS_DIR, 'requirements.txt')
with open(REQUIREMENTS_FILE, 'rt') as requirements_file:
    REQUIREMENTS = [requirement.strip() for requirement in requirements_file.readlines()]

# pylint: disable=bad-whitespace
setuptools.setup(
    name              = 'tartar_sauce',
    version           = '0.0.0.1',
    description       = 'Tarfile archive helpers',
    maintainer        = 'richimuks123',
    maintainer_email  = '',
    url               = 'https://github.com/richimus123/tartar_sauce',
    packages          = PACKAGES,
    package_data      = PACKAGE_DATA,
    data_files        = DATA_FILES,
    python_requires   = '>=3.0.0',
    entry_points      = { 'console_scripts': COMMANDS },
    install_requires  = REQUIREMENTS,
)
