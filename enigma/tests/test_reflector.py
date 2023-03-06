
import sys
#sys.path.append('.')
from enigma.reflector import *
import pytest

def test_reflectorA_encipherZ():
    x = REFLECTOR_A.encipher(key="z")
    assert x == 'D'

def test_reflectorB_encipherZ():
    x = REFLECTOR_B.encipher(key="z")
    assert x == 'T'

def test_reflectorC_encipherZ():
    x = REFLECTOR_C.encipher(key="z")
    assert x == 'L'

def test_reflector_encipherInt():
    with pytest.raises(AssertionError):
        REFLECTOR_A.encipher(9)

def test_reflector_encipherTwoStr():
    with pytest.raises(AssertionError):
        REFLECTOR_A.encipher('AA')
    
