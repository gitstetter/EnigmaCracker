import sys
sys.path.append('.')



from enigma.reflector import *

def test_reflectorA_encipherZ():
    x = REFLECTOR_A.encipher(key="z")
    assert x == 'D'

def test_reflectorB_encipherZ():
    x = REFLECTOR_B.encipher(key="z")
    assert x == 'T'

def test_reflectorC_encipherZ():
    x = REFLECTOR_C.encipher(key="z")
    assert x == 'L'
