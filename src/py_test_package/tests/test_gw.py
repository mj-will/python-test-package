"""Test gw packages"""

def test_bilby_import():
    """Testing importing bilby"""
    import bilby
    assert bilby.__version__ is not None

