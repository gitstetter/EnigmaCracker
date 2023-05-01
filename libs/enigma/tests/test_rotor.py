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


def test_ROTORI_ringsetting_1():
    ROTOR_I.rotor_position = 'A'
    ROTOR_I.handle_ring_settings()
    assert ROTOR_I.rotor_position == 'A'

def test_ROTORI_ringsetting_2():
    ROTOR_I.ring_position = 2
    ROTOR_I.rotor_position = 'A'
    ROTOR_I.handle_ring_settings()
    assert ROTOR_I.rotor_position == 'B'

def test_ROTORI_ringsetting_26():
    ROTOR_I.ring_position = 26
    ROTOR_I.rotor_position = 'A'
    ROTOR_I.handle_ring_settings()
    assert ROTOR_I.rotor_position == 'Z'

def test_ROTORI_ringsetting_notch_over():
    ROTOR_I.ring_position = 3
    ROTOR_I.rotor_position = 'Y'
    ROTOR_I.handle_ring_settings()
    assert ROTOR_I.rotor_position == 'A'

def test_ROTORI_ringsetting_invalid():
    with pytest.raises(AssertionError):
        ROTOR_I.ring_position = 27
        ROTOR_I.rotor_position = 'Y'
        ROTOR_I.handle_ring_settings()
        assert ROTOR_I.rotor_position == 'A'

def test_ROTORI_ringsetting_invalid_type():
    with pytest.raises(AssertionError):
        ROTOR_I.ring_position = 'A'
        ROTOR_I.rotor_position = 'Y'
        ROTOR_I.handle_ring_settings()
        assert ROTOR_I.rotor_position == 'A'