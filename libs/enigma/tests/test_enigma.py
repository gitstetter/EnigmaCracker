import pytest
from enigma.rotor import ROTOR_I, ROTOR_II, ROTOR_III, ROTOR_IV, ROTOR_V
from enigma.reflector import REFLECTOR_A, REFLECTOR_B, REFLECTOR_C
from enigma.enigma import Enigma
from enigma.plugboard import Plugboard

@pytest.fixture
def EnigmaMachinePlain():
    EnigmaMachinePlain = Enigma(reflector=REFLECTOR_B, 
                        left_rotor=ROTOR_III, 
                        middle_rotor=ROTOR_II, 
                        right_rotor=ROTOR_I, 
                        rotor_positions="1 1 1" ,
                        ring_positions="1 1 1",
                        plugboard=Plugboard()
                        )
    return EnigmaMachinePlain

@pytest.fixture
def EnigmaMachineRotorPositions():
    EnigmaMachineRotorPositions = Enigma(reflector=REFLECTOR_B, 
                        left_rotor=ROTOR_III, 
                        middle_rotor=ROTOR_II, 
                        right_rotor=ROTOR_I, 
                        rotor_positions="1 2 3" ,
                        ring_positions="1 1 1",
                        plugboard=Plugboard()
                        )
    return EnigmaMachineRotorPositions


def test_rotors_all_notching(EnigmaMachinePlain):
    EnigmaMachinePlain.left_rotor.rotor_position = ord(EnigmaMachinePlain.left_rotor.notch_position) - ord("A")
    EnigmaMachinePlain.middle_rotor.rotor_position = ord(EnigmaMachinePlain.middle_rotor.notch_position) - ord("A")
    EnigmaMachinePlain.right_rotor.rotor_position = ord(EnigmaMachinePlain.right_rotor.notch_position) - ord("A")
    
    EnigmaMachinePlain.rotate()

    #ROTOR_III notch_position='W'
    #ROTOR_II notch_position='F'
    #ROTOR_I notch_position='R'
    assert EnigmaMachinePlain.left_rotor.rotor_position ==24
    assert EnigmaMachinePlain.middle_rotor.rotor_position ==7
    assert EnigmaMachinePlain.right_rotor.rotor_position ==19

def test_right_rotor_notching(EnigmaMachinePlain):
    EnigmaMachinePlain.right_rotor.rotor_position = ord(EnigmaMachinePlain.right_rotor.notch_position) - ord("A")
    
    EnigmaMachinePlain.rotate()

    #ROTOR_III notch_position='W'
    #ROTOR_II notch_position='F'
    #ROTOR_I notch_position='R'
    assert EnigmaMachinePlain.left_rotor.rotor_position ==1
    assert EnigmaMachinePlain.middle_rotor.rotor_position ==2
    assert EnigmaMachinePlain.right_rotor.rotor_position ==19

def test_middle_rotor_notching(EnigmaMachinePlain):
    EnigmaMachinePlain.middle_rotor.rotor_position = ord(EnigmaMachinePlain.middle_rotor.notch_position) - ord("A")
    EnigmaMachinePlain.right_rotor.rotor_position = ord(EnigmaMachinePlain.right_rotor.notch_position) - ord("A")
    
    EnigmaMachinePlain.rotate()

    #ROTOR_III notch_position='W'
    #ROTOR_II notch_position='F'
    #ROTOR_I notch_position='R'
    assert EnigmaMachinePlain.left_rotor.rotor_position ==2
    assert EnigmaMachinePlain.middle_rotor.rotor_position ==7
    assert EnigmaMachinePlain.right_rotor.rotor_position ==19

def test_encrypt_letter(EnigmaMachineRotorPositions):
    EnigmaMachineRotorPositions.rotate()
    char = "A"
    temp = EnigmaMachineRotorPositions.plugboard.map_plugs(char)
    temp = EnigmaMachineRotorPositions.right_rotor.encipher_forward(temp)
    assert temp=='F'
    temp = EnigmaMachineRotorPositions.middle_rotor.encipher_forward(temp)
    # assert temp=='K' #break
    temp = EnigmaMachineRotorPositions.left_rotor.encipher_forward(temp)
    # assert temp=='T' 
    temp = EnigmaMachineRotorPositions.reflector.encipher(temp)
    assert temp=='Z'

            