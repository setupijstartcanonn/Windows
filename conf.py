# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# Add any module paths here if needed
# Example: sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Brother Printer Drivers'
copyright = '2025, Brother'
author = 'Brother Support Team'
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = []
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# Theme options
html_theme = 'sphinx_rtd_theme'  # Recommended for clean documentation style
html_theme_options = {
    'collapse_navigation': False,
    'navigation_depth': 3,
    'style_external_links': True,
    'display_version': False,
    'prev_next_buttons_location': 'bottom',
    'style_nav_header_background': '#0066cc',  # Optional: Blue header
    'show_powered_by': False,
}

# Page titles
html_title = "Brother Printer Drivers – Download & Install via Setup.Brother.com"
html_short_title = "Setup.Brother.com Driver Guide"

# Static & branding assets
html_favicon = 'favicon.ico'
# html_logo = '_static/logo.png'  # Optional: Add logo here
# html_static_path = ['_static']  # Uncomment if using custom styles or JS

# Other settings
html_show_sourcelink = False
html_allow_unsafe = True
