# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'NetDRIVE Dash4Action'
copyright = '2026, spcs-computing'
author = 'spcs-computing'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
#html_logo = '_static/Dash4ActionWhite.svg'
html_logo = '_static/NetDRIVE-Dash4Action.png'

html_theme_options = {
    'logo_only': True,  # Hides the text project name, shows only the logo image
#    'display_version': False, # Optional: also hides the version number if desired
}
