"""Install setup.py for resizeright."""
from setuptools import setup, find_packages


REQUIREMENTS = ['torch']


setup(
    name='resizeright',
    version=0.1,
    description='Resizing Right for Pytorch Tensors',
    author='na',
    author_email='na',
    url='na',
    long_description=open('README.md').read(),
    packages=find_packages(),
    install_requires=REQUIREMENTS
)