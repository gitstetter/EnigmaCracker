from enigma.plugboard import *
import pytest


def test_plugboard_correct_mapping():
    PLUGBOARD = Plugboard(plug_settings="AB FG DE")
    assert PLUGBOARD.map_plugs('A')=='B'
    assert PLUGBOARD.map_plugs('B')=='A'
    assert PLUGBOARD.map_plugs('F')=='G'
    assert PLUGBOARD.map_plugs('G')=='F'
    assert PLUGBOARD.map_plugs('Z')=='Z'
    
def test_plugboard_no_settings():
    PLUGBOARD = Plugboard()
    assert PLUGBOARD.map_plugs('A')=='A'
    assert PLUGBOARD.map_plugs('B')=='B'

def test_plugboard_duplicate_settings():
    with pytest.raises(AssertionError):
        PLUGBOARD = Plugboard(plug_settings="AB AE")

def test_plugboard_too_many_plug_settings():
    with pytest.raises(AssertionError):
        PLUGBOARD = Plugboard(plug_settings="AB CD EF GH IJ KL MN OP QR ST UV WX")