# coding: utf-8
from setuptools import setup, find_packages  # noqa: H301

NAME = "oddsapi"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="The Odds API",
    author_email="",
    url="",
    keywords=["The Odds API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    To access the API, get a free API key from https://the-odds-api.com  # noqa: E501
    """
)
