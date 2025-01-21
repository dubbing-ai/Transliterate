"""
Test suite for the transliterate package.
This makes the tests directory a Python package and allows for proper import resolution.
"""
import os
import sys

# Add the project root directory to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)