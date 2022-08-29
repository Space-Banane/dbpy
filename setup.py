from setuptools import setup
setup(
    name="DbPy",
    version="1.5",
    url="https://github.com/Space-Banane/dbpy",
    author="Space-Banane#5444",
    description="QSL Connection for your script",
    requires=["pymysql"]
)


from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.0'
DESCRIPTION = 'QSL Connection for your script'

# Setting up
setup(
    name="DbPy",
    version=VERSION,
    author="Paul",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["pymysql"],
    keywords=["Database","qsl"],
    classifiers=[
        "Programming Language :: Python :: 3"
    ]
)