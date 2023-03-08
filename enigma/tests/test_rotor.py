from enigma.rotor import *
import pytest


def test_ROTORI_encipher_left_right():
    assert ROTOR_I.encipher_backwards('K')=='B'
    assert ROTOR_I.encipher_forward('B')=='K'

def test_reflector_encipherInt():
    with pytest.raises(AssertionError):
        ROTOR_I.encipher_forward(9)

def test_reflector_encipherTwoStr():
    with pytest.raises(AssertionError):
        ROTOR_I.encipher_forward('AA')

def test_reflector_encipher_back_Int():
    with pytest.raises(AssertionError):
        ROTOR_I.encipher_backwards(9)

def test_reflector_encipher_back_TwoStr():
    with pytest.raises(AssertionError):
        ROTOR_I.encipher_backwards('AA')
