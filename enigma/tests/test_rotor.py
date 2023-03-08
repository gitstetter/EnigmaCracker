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
    ROTOR_I.rotor_position = 0
    ROTOR_I.notch()
    assert ROTOR_I.rotor_position == 1
    ROTOR_I.notch()
    assert ROTOR_I.rotor_position == 2

def test_ROTORI_notch_over():
    ROTOR_I.rotor_position = 25
    ROTOR_I.notch()
    assert ROTOR_I.rotor_position == 26
    ROTOR_I.notch()
    assert ROTOR_I.rotor_position == 0
    ROTOR_I.notch()
    assert ROTOR_I.rotor_position == 1
