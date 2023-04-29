from enigma.rotor import *
import pytest


def test_ROTORI_encipher_left_right():
    assert ROTOR_I.encipher_backwards('K')=='B'
    assert ROTOR_I.encipher_forward('B')=='K'

def test_ROTORI_encipherInt():
    with pytest.raises(AssertionError):
        ROTOR_I.encipher_forward(9)

def test_ROTORI_encipherTwoStr():
    with pytest.raises(AssertionError):
        ROTOR_I.encipher_forward('AA')

def test_ROTORI_encipher_back_Int():
    with pytest.raises(AssertionError):
        ROTOR_I.encipher_backwards(9)

def test_ROTORI_encipher_back_TwoStr():
    with pytest.raises(AssertionError):
        ROTOR_I.encipher_backwards('AA')

def test_ROTORI_notch():
    ROTOR_I.rotor_position = 'A'
    ROTOR_I.notch()
    assert ROTOR_I.rotor_position == 'B'
    ROTOR_I.notch()
    assert ROTOR_I.rotor_position == 'C'

def test_ROTORI_notch_over():
    ROTOR_I.rotor_position = 'Y'
    ROTOR_I.notch()
    assert ROTOR_I.rotor_position == 'Z'
    ROTOR_I.notch()
    assert ROTOR_I.rotor_position == 'A'
    ROTOR_I.notch()
    assert ROTOR_I.rotor_position == 'B'
