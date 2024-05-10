# coding: utf-8

from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "bloxone-python-client"
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
    description="Python client for the BloxOne API",
    author="Infoblox",
    url="https://github.com/infobloxopen/bloxone-python-client",
    keywords=["Infoblox", "BloxOne", "OpenAPI-Generator"],
    install_requires=REQUIRES,
    packages=find_packages('src', exclude=["test", "tests"]),
    package_dir={'': 'src'},
    include_package_data=True,
    package_data={
        "*": ["py.typed"]
    },
)

