import os
import sys

sys.path.insert(0, os.path.abspath("."))

from setuptools import setup, find_packages
from radar.version import VERSION

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="radar-python",
    version=VERSION,
    description="Python bindings for the Radar API",
    author="Radar",
    author_email="support@radar.io",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["tests",]),
    python_requires=">=3.4",
    install_requires=["requests >= 2.20"],
    tests_require=["pytest >= 4.6.2"],
    url="https://github.com/radarlabs/radar-python",
    license="MIT",
    project_urls={
        "Documentation": "https://radar.io/documentation/api",
        "Source Code": "https://github.com/radarlabs/radar-python",
    },
)
