from enigma.rotor import *
import pytest


def test_ROTORI_encipher_forward():
    ROTOR_I.rotor_position = 1
    assert ROTOR_I.encipher_forward('B')=='K'

def test_ROTORI_encipher_backwards():
    ROTOR_I.rotor_position = 1
    assert ROTOR_I.encipher_backwards('K')=='B' 

def test_ROTORI_encipher_int():
    with pytest.raises(AssertionError):
        ROTOR_I.encipher_forward(9)

def test_ROTORI_encipher_two_str():
    with pytest.raises(AssertionError):
        ROTOR_I.encipher_forward('AA')

def test_ROTORI_encipher_back_int():
    with pytest.raises(AssertionError):
        ROTOR_I.encipher_backwards(9)

def test_ROTORI_encipher_back_two_str():
    with pytest.raises(AssertionError):
        ROTOR_I.encipher_backwards('AA')

def test_ROTORI_notch():
    ROTOR_I.rotor_position = 1
    ROTOR_I.notch()
    assert ROTOR_I.rotor_position == 2
    ROTOR_I.notch()
    assert ROTOR_I.rotor_position == 3

def test_ROTORI_notch_over():
    ROTOR_I.rotor_position = 25
    ROTOR_I.notch()
    assert ROTOR_I.rotor_position == 26
    ROTOR_I.notch()
    assert ROTOR_I.rotor_position == 1
    ROTOR_I.notch()
    assert ROTOR_I.rotor_position == 2


def test_ROTORI_ringsetting_encipher_forward():
    ROTOR_I.rotor_position = 1
    ROTOR_I.set_ring_position(2)
    assert ROTOR_I.encipher_forward('K')=='A'
    ROTOR_I.rotor_position = 1
    ROTOR_I.set_ring_position(26)
    assert ROTOR_I.encipher_forward('Z')=='D'


def test_ROTORI_is_at_notch():
    ROTOR_I.rotor_position = ord(ROTOR_I.notch_position)-ord("A")
    assert ROTOR_I.is_in_turnover_pos()