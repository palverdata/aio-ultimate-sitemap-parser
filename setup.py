#!/usr/bin/env python

from setuptools import find_packages, setup

# Version should be updated to match the new version
__version__ = "0.1"


def __readme():
    with open("README.rst", mode="r", encoding="utf-8") as f:
        return f.read()


setup(
    name="ultimate-sitemap-parser",
    version=__version__,
    description="Ultimate Sitemap Parser",
    long_description=__readme(),
    long_description_content_type="text/x-rst",  # Assuming README.rst is reStructuredText
    author="Linas Valiukas, Hal Roberts",
    author_email="linas@media.mit.edu, hroberts@cyber.law.harvard.edu",
    url="https://github.com/palverdata/aio-ultimate-sitemap-parser",
    license="GPLv3+",
    keywords=["sitemap", "sitemap-xml", "parser"],
    packages=find_packages(exclude=["tests"]),
    zip_safe=True,
    python_requires=">=3.11",  # Updated to require Python 3.11 or newer
    install_requires=[
        "requests>=2.31.0",
        "python-dateutil>=2.1,<3.0.0",
        "aiohttp>=3.9.3",  # Assuming "^3.9.3" means "3.9.3 or newer"
        "fake-useragent>=1.4.0",
        "charset-normalizer>=3.3.2",
    ],
    setup_requires=[
        "pytest-runner>=4.2,<5.0",
    ],
    tests_require=[
        "requests_mock>=1.6.0,<2.0",
        "pytest>=2.8",
    ],
    extras_require={
        "test": [
            "requests_mock>=1.6.0,<2.0",
            "pytest>=2.8",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
        "Topic :: Text Processing :: Indexing",
        "Topic :: Text Processing :: Markup :: XML",
    ],
)
