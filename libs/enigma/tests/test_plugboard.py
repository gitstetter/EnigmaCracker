from enigma.plugboard import *
import pytest


def test_plugboard_correct_mapping():
    PLUGBOARD = Plugboard(plug_settings="AB FG DE")
    assert PLUGBOARD.map_plug('A')=='B'
    assert PLUGBOARD.map_plug('B')=='A'
    assert PLUGBOARD.map_plug('F')=='G'
    assert PLUGBOARD.map_plug('G')=='F'
    assert PLUGBOARD.map_plug('Z')=='Z'
    
def test_plugboard_no_settings():
    PLUGBOARD = Plugboard()
    assert PLUGBOARD.map_plug('A')=='A'
    assert PLUGBOARD.map_plug('B')=='B'

def test_plugboard_duplicate_settings():
    with pytest.raises(AssertionError):
        PLUGBOARD = Plugboard(plug_settings="AB AE")

def test_plugboard_too_many_plug_settings():
    with pytest.raises(AssertionError):
        PLUGBOARD = Plugboard(plug_settings="AB CD EF GH IJ KL MN OP QR ST UV WX")