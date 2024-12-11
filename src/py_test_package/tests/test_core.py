"""Test the core package"""
from py_test_package import describe


def test_describe():
    out = describe()
    assert isinstance(out, str)
