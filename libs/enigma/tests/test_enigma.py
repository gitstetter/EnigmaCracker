import pytest
from enigma.rotor import ROTOR_I, ROTOR_II, ROTOR_III, ROTOR_IV, ROTOR_V
from enigma.reflector import REFLECTOR_A, REFLECTOR_B, REFLECTOR_C
from enigma.enigma import Enigma
from enigma.plugboard import Plugboard

@pytest.fixture
def EnigmaMachine():
    EnigmaMachine = Enigma(reflector=REFLECTOR_B, 
                        left_rotor=ROTOR_III, 
                        middle_rotor=ROTOR_II, 
                        right_rotor=ROTOR_I, 
                        rotor_positions="A A A" ,
                        ring_positions="1 1 1",
                        plugboard=Plugboard()
                        )
    return EnigmaMachine

@pytest.fixture
def EnigmaMachine2():
    EnigmaMachine2 = Enigma(reflector=REFLECTOR_B, 
                        left_rotor=ROTOR_III, 
                        middle_rotor=ROTOR_II, 
                        right_rotor=ROTOR_I, 
                        rotor_positions="A A A" ,
                        ring_positions="5 7 1",
                        plugboard=Plugboard()
                        )
    return EnigmaMachine2


def test_rotors_all_notching(EnigmaMachine):
    EnigmaMachine.left_rotor.rotor_position = EnigmaMachine.left_rotor.notch_position
    EnigmaMachine.middle_rotor.rotor_position = EnigmaMachine.middle_rotor.notch_position
    EnigmaMachine.right_rotor.rotor_position = EnigmaMachine.right_rotor.notch_position
    
    if EnigmaMachine.middle_rotor.is_in_turnover_pos():
            EnigmaMachine.middle_rotor.notch()
            EnigmaMachine.left_rotor.notch()
    elif EnigmaMachine.left_rotor.is_in_turnover_pos():
            EnigmaMachine.middle_rotor.notch()
    EnigmaMachine.right_rotor.notch()

    #ROTOR_III notch_position='W'
    #ROTOR_II notch_position='F'
    #ROTOR_I notch_position='R'
    assert EnigmaMachine.left_rotor.rotor_position =='X'
    assert EnigmaMachine.middle_rotor.rotor_position =='G'
    assert EnigmaMachine.right_rotor.rotor_position =='S'

def test_encrypt_letter(EnigmaMachine2):
    x=EnigmaMachine2.encipher('A')
    assert x=='I'
