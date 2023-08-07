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
def EnigmaMachineSettings():
    EnigmaMachineSettings = Enigma(reflector=REFLECTOR_B, 
                        left_rotor=ROTOR_III, 
                        middle_rotor=ROTOR_II, 
                        right_rotor=ROTOR_I, 
                        rotor_positions="A A A" ,
                        ring_positions="5 7 1",
                        plugboard=Plugboard()
                        )
    return EnigmaMachineSettings


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

def test_encrypt_letter(EnigmaMachineSettings):
    EnigmaMachineSettings.rotate()
    char = "A"
    temp = EnigmaMachineSettings.plugboard.map_plugs(char)
    temp = EnigmaMachineSettings.right_rotor.encipher_forward(temp)
    assert temp=='K'
    temp = EnigmaMachineSettings.middle_rotor.encipher_forward(temp)
    assert temp=='Q'
    temp = EnigmaMachineSettings.left_rotor.encipher_forward(temp)
    assert temp=='D'
    temp = EnigmaMachineSettings.reflector.encipher(temp)
    assert temp=='H'

            