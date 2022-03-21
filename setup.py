from unicodedata import name
from nbformat import read
from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="0.1",
    packages=find_packages(exclude=["tests*"]),
    license="MIT",
    description="EDSA example python package",
    long_description=open('Readme.md').read(),
    install_requires=["numpy"],
    url="",
    author="Dewald",
    author_email="Your email",
)
