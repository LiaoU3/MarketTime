import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent.resolve()

PACKAGE_NAME = "MarketTime"
AUTHOR = "VincentLiao"
AUTHOR_EMAIL = "vincent932693@gmail.com"
URL = "https://github.com/Liaou3/MarketTime"
DOWNLOAD_URL = ""

LICENSE = "GPLv3"
VERSION = "1.1.2"
DESCRIPTION = "This is a tool to check the time in the market"
LONG_DESCRIPTION = (HERE/"README.md").read_text(encoding="utf8")
LONG_DESC_TYPE = "text/markdown"
INSTALL_REQUIRES = ["datetime"]
EXTRAS_REQUIRE = {}
CLASSIFIERS = []
PYTHON_REQUIRES = ">=3.10"

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    license=LICENSE,
    author_email=AUTHOR_EMAIL,
    url=URL,
    download_url=DOWNLOAD_URL,
    python_requires=PYTHON_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    packages=find_packages(),
    classifiers=CLASSIFIERS,
)
