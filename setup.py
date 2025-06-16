#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from pathlib import Path

version_path = Path(__file__).parent / "karton/%CLASS%/__version__.py"
version_info = {}
exec(version_path.read_text(), version_info)

setup(
    name="karton-%CLASS%",
    version=version_info["__version__"],
    url="https://github.com/cocoapuck/karton-%CLASS%/",
    description="Runs %CLASS% scan on files with Karton",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    namespace_packages=["karton"],
    packages=["karton.%CLASS%"],
    install_requires=open("requirements.txt").read().splitlines(),
    entry_points={
        'console_scripts': [
            'karton-%CLASS%=karton.%CLASS%:%UCASE_CLASS%.main'
        ],
    },
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: OS Independent",
    ],
)