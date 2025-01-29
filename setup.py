# coding: utf-8

from setuptools import setup, find_packages  # noqa: H301

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "universal-ddi-python-client"
VERSION = "0.1.0"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python-dateutil",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]



setup(
    name=NAME,
    version=VERSION,
    description="Python client for the Universal DDI APIs",
    author="Infoblox",
    url="https://github.com/infobloxopen/universal-ddi-python-client",
    keywords = ["Infoblox", "Universal", "DDI", "OpenAPI-Generator"],
    install_requires=REQUIRES,
    packages=find_packages('src', exclude=["test", "tests"]),
    package_dir={'': 'src'},
    include_package_data=True,
    long_description=long_description,
    long_description_content_type='text/markdown',
    package_data={
        "*": ["py.typed"]
    },
)

