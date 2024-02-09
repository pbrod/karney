# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import importlib
import os
import sys
import inspect
import re
import glob
from datetime import datetime

CURRENT_YEAR = datetime.now().year
START_YEAR = 2021
DEV_YEARS = '{}'.format(START_YEAR) if START_YEAR == CURRENT_YEAR else '{}-{}'.format(START_YEAR, CURRENT_YEAR)

__location__ = os.path.abspath(os.path.dirname(__file__))
SOURCE_PATH = os.path.join(os.path.dirname(__location__), 'src')
sys.path.insert(0, SOURCE_PATH)


# -- Project information -----------------------------------------------------

project = u"Karney"

PACKAGE_NAME = project.lower()
author = 'Per A. Brodtkorb'
copyright = ', '.join((DEV_YEARS, author))


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_nb",
    "autoapi.extension",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.doctest",
]
source_suffix = {
    '.rst': 'restructuredtext',
    '.ipynb': 'myst-nb',
    '.myst': 'myst-nb',
}
autoapi_dirs = ["../src"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"



# -- Doctest configuration ----------------------------------------

import doctest

doctest_default_flags = (0
    | doctest.DONT_ACCEPT_TRUE_FOR_1
    | doctest.ELLIPSIS
    | doctest.IGNORE_EXCEPTION_DETAIL
    | doctest.NORMALIZE_WHITESPACE
)

