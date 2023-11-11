import pytest
from enigma.rotor import ROTOR_I, ROTOR_II, ROTOR_III, ROTOR_IV, ROTOR_V
from enigma.reflector import REFLECTOR_A, REFLECTOR_B, REFLECTOR_C
from enigma.enigma import Enigma
from enigma.plugboard import Plugboard

@pytest.fixture
def EnigmaMachineRotorRingPositions():
    EnigmaMachineRotorRingPositions = Enigma(reflector=REFLECTOR_B, 
                        left_rotor=ROTOR_III, 
                        middle_rotor=ROTOR_II, 
                        right_rotor=ROTOR_I, 
                        rotor_positions="16 10 1" ,
                        ring_positions="3 1 17",
                        plugboard=Plugboard()
                        )
    return EnigmaMachineRotorRingPositions

@pytest.fixture
def EnigmaMachineRotorRingPlugs():
    EnigmaMachineRotorRingPlugs = Enigma(reflector=REFLECTOR_B, 
                        left_rotor=ROTOR_III, 
                        middle_rotor=ROTOR_II, 
                        right_rotor=ROTOR_I, 
                        rotor_positions="16 10 1" ,
                        ring_positions="3 1 17",
                        plugboard=Plugboard("AQ JH FR EW TZ")
                        )
    return EnigmaMachineRotorRingPlugs


def test_encrypt_phrase(EnigmaMachineRotorRingPositions):
    encrypted_text=EnigmaMachineRotorRingPositions.encipher('THISBETTERBEWORKINGFORREALTHISTIME')
    assert encrypted_text == 'vjrqfaanthvttssrrgujemcrfmhxqmsgtf'.upper()


def test_encrypt_phrase2(EnigmaMachineRotorRingPlugs):
    encrypted_text=EnigmaMachineRotorRingPlugs.encipher('THISBETTERBEWORKINGFORREALTHISTIME')
    assert encrypted_text == 'mjfaroueydvnqsjffgubwziqymiiamxgzz'.upper()


