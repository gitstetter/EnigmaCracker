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
                        rotor_positions="A A A" ,
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
                        rotor_positions="A B C" ,
                        ring_positions="1 1 1",
                        plugboard=Plugboard()
                        )
    return EnigmaMachineRotorPositions


def test_rotors_all_notching(EnigmaMachinePlain):
    EnigmaMachinePlain.left_rotor.rotor_position = EnigmaMachinePlain.left_rotor.notch_position
    EnigmaMachinePlain.middle_rotor.rotor_position = EnigmaMachinePlain.middle_rotor.notch_position
    EnigmaMachinePlain.right_rotor.rotor_position = EnigmaMachinePlain.right_rotor.notch_position
    
    EnigmaMachinePlain.rotate()

    #ROTOR_III notch_position='W'
    #ROTOR_II notch_position='F'
    #ROTOR_I notch_position='R'
    assert EnigmaMachinePlain.left_rotor.rotor_position =='X'
    assert EnigmaMachinePlain.middle_rotor.rotor_position =='G'
    assert EnigmaMachinePlain.right_rotor.rotor_position =='S'

def test_right_rotor_notching(EnigmaMachinePlain):
    EnigmaMachinePlain.right_rotor.rotor_position = EnigmaMachinePlain.right_rotor.notch_position
    
    EnigmaMachinePlain.rotate()

    #ROTOR_III notch_position='W'
    #ROTOR_II notch_position='F'
    #ROTOR_I notch_position='R'
    assert EnigmaMachinePlain.left_rotor.rotor_position =='A'
    assert EnigmaMachinePlain.middle_rotor.rotor_position =='B'
    assert EnigmaMachinePlain.right_rotor.rotor_position =='S'

def test_middle_rotor_notching(EnigmaMachinePlain):
    EnigmaMachinePlain.middle_rotor.rotor_position = EnigmaMachinePlain.middle_rotor.notch_position
    EnigmaMachinePlain.right_rotor.rotor_position = EnigmaMachinePlain.right_rotor.notch_position
    
    EnigmaMachinePlain.rotate()

    #ROTOR_III notch_position='W'
    #ROTOR_II notch_position='F'
    #ROTOR_I notch_position='R'
    assert EnigmaMachinePlain.left_rotor.rotor_position =='B'
    assert EnigmaMachinePlain.middle_rotor.rotor_position =='G'
    assert EnigmaMachinePlain.right_rotor.rotor_position =='S'

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

            