# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import pydata_sphinx_theme

project = 'ibl-docs-ce'
copyright = '2023, IBL'
author = 'IBL'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

source_dir = 'docs'


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "github_url": "https://github.com/ibleducation/ibl-docs-ce",
    "use_edit_page_button": True,
}
html_context = {
    "github_user": "bnsoni",
    "github_repo": "ibl-docs-ce",
    "github_version": "master",
}
# html_static_path = ['_static']
