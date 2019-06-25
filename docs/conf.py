# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import os
import codecs
import re


def find_version(*file_paths):
    """
    Build a path from *file_paths* and search for a ``__version__``
    string inside.
    """
    version_file = read(*file_paths)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M
    )
    if version_match:
        return version_match.group(1)

    raise RuntimeError("Unable to find version string.")


def read(*parts):
    """
    Build an absolute path from *parts* and and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    """
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, *parts), "rb", "utf-8") as f:
        return f.read()


# -- Project information -----------------------------------------------------

project = "centerline"
copyright = "2014, Filip Todić"
author = "Filip Todić"

# The full version, including alpha/beta/rc tags
release = find_version("../src/centerline/__init__.py")


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_theme_options = {
    "description": "Calculate the polygon's centerline.",
    "github_user": "fitodic",
    "github_repo": "centerline",
    "github_banner": True,
    "github_button": True,
    "fixed_sidebar": True,
    "show_related": True,
}

# The GDAL package first has to be installed system-wide which breaks
# the documentation build on readthedocs.io. Therefore, the `osgeo`
# module is mocked using `autodoc_mock_imports`
autodoc_mock_imports = ["osgeo", "gdal", "ogr"]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "fiona": ("https://fiona.readthedocs.io/en/latest/", None),
    "shapely": ("https://shapely.readthedocs.io/en/latest/", None),
}
intersphinx_timeout = 30
