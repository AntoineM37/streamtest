from setuptools import setup
from setuptools import find_packages


DISTNAME = "teststream"

MAJOR = 0
MINOR = 4
MICRO = 1
ISRELEASED = False
VERSION = f"{MAJOR}.{MINOR}.{MICRO}"


setup(name=DISTNAME, version=VERSION, packages=find_packages(), zip_safe=False)