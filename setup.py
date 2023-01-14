from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='library_management',
    version=version,
    description='Library Manegement System',
    author='Alok Shukla',
    author_email='alok@hybrowlabs.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
