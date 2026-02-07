"""
Testing script for convertNumbers.py 
"""
import convertNumbers


def test_pos_bin():
    """
    Test case definition for positive decimal to binary conversion
    """
    assert convertNumbers.convert2bin(7116776) == "11011001001011111101000"
    assert convertNumbers.convert2bin(9764122) == "100101001111110100011010"
    assert convertNumbers.convert2bin(0) == "0"
    assert convertNumbers.convert2bin(26) == "11010"

def test_pos_hex():
    """
    Test case definition for positive decimal to hexadecimal conversion
    """
    assert convertNumbers.convert2hex(7116776) == "6C97E8"
    assert convertNumbers.convert2hex(39) == "27"
    assert convertNumbers.convert2hex(45) == "2D"
    assert convertNumbers.convert2hex(0) == "0"

def test_neg_bin():
    """
    Test case definition for negative decimal to binary conversion
    """
    assert convertNumbers.convert2bin(-39) == "1111011001"
    assert convertNumbers.convert2bin(-6) == "1111111010"
    assert convertNumbers.convert2bin(-16) == "1111110000"
    assert convertNumbers.convert2bin(-50) == "1111001110"

def test_neg_hex():
    """
    Test case definition for negative decimal to hexadecimal conversion
    """
    assert convertNumbers.convert2hex(-39) == "FFFFFFFFD9"
    assert convertNumbers.convert2hex(-6) == "FFFFFFFFFA"
    assert convertNumbers.convert2hex(-16) == "FFFFFFFFF0"
    assert convertNumbers.convert2hex(-50) == "FFFFFFFFCE"
