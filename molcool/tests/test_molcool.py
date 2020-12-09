"""
Unit and regression test for the molcool package.
"""

# Import package, test suite, and other packages as needed
import molcool
import pytest
import sys

def test_molcool_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "molcool" in sys.modules
