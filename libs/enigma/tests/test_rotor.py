from enigma.rotor import *
import pytest


def test_ROTORI_encipher_forward():
    ROTOR_I.rotor_position = 'A'
    assert ROTOR_I.encipher_forward('B')=='K'

def test_ROTORI_encipher_forward_with_notch():
    ROTOR_I.rotor_position = 'A'
    assert ROTOR_I.encipher_forward('B')=='K'
    ROTOR_I.notch()
    assert ROTOR_I.encipher_forward('B')=='M'

def test_ROTORI_encipher_forward_with_notch_over():
    ROTOR_I.rotor_position = 'Y'
    assert ROTOR_I.encipher_forward('B')=='J'
    ROTOR_I.notch()
    assert ROTOR_I.encipher_forward('B')=='E'
    ROTOR_I.notch()   
    assert ROTOR_I.encipher_forward('B')=='K'   

def test_ROTORI_encipher_backwards():
    ROTOR_I.rotor_position = 'A'
    assert ROTOR_I.encipher_backwards('K')=='B' 

def test_ROTORI_encipher_backwards_with_notch():
    ROTOR_I.rotor_position = 'A'
    assert ROTOR_I.encipher_backwards('K')=='B'
    ROTOR_I.notch()
    assert ROTOR_I.encipher_backwards('K')=='E'
    assert ROTOR_I.encipher_backwards('M')=='K'

def test_ROTORI_encipher_backwards_with_notch_over():
    ROTOR_I.rotor_position = 'Y'
    assert ROTOR_I.encipher_backwards('B')=='J'
    ROTOR_I.notch()
    assert ROTOR_I.encipher_backwards('B')=='U'
    ROTOR_I.notch()
    assert ROTOR_I.encipher_backwards('B')=='W'

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
    ROTOR_I.ring_position = 1
    ROTOR_I.rotor_position = 'A'
    ROTOR_I.handle_ring_setting()
    assert ROTOR_I.rotor_position == 'A'

def test_ROTORI_ringsetting_2():
    ROTOR_I.ring_position = 2
    ROTOR_I.rotor_position = 'A'
    ROTOR_I.handle_ring_setting()
    assert ROTOR_I.rotor_position == 'B'

def test_ROTORI_ringsetting_26():
    ROTOR_I.ring_position = 26
    ROTOR_I.rotor_position = 'A'
    ROTOR_I.handle_ring_setting()
    assert ROTOR_I.rotor_position == 'Z'

def test_ROTORI_ringsetting_notch_over():
    ROTOR_I.ring_position = 3
    ROTOR_I.rotor_position = 'Y'
    ROTOR_I.handle_ring_setting()
    assert ROTOR_I.rotor_position == 'A'

def test_ROTORI_ringsetting_invalid_int():
    with pytest.raises(AssertionError):
        ROTOR_I.ring_position = 27
        ROTOR_I.rotor_position = 'Y'
        ROTOR_I.handle_ring_setting()
        assert ROTOR_I.rotor_position == 'A'

def test_ROTORI_ringsetting_invalid_type():
    with pytest.raises(AssertionError):
        ROTOR_I.ring_position = 'Not supported'
        ROTOR_I.rotor_position = 'Y'
        ROTOR_I.handle_ring_setting()
        assert ROTOR_I.rotor_position == 'A'

def test_ROTORI_ringsetting_encipher_forward():
    ROTOR_I.rotor_position = 'A'
    ROTOR_I.set_ring_position(2)
    assert ROTOR_I.rotor_position=='B'
    assert ROTOR_I.encipher_forward('K')=='T'
    ROTOR_I.rotor_position = 'A'
    ROTOR_I.set_ring_position(26)
    assert ROTOR_I.encipher_forward('Z')=='C'

def test_ROTORI_is_at_notch():
    ROTOR_I.rotor_position = ROTOR_I.notch_position
    assert ROTOR_I.is_in_turnover_pos()