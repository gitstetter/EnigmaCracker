from . rotor import Rotor
from . reflector import Reflector
from . plugboard import Plugboard

UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Enigma:
    """
    Represents an Enigma machine.
    """

    def __init__(self, reflector:Reflector, left_rotor:Rotor, middle_rotor:Rotor, right_rotor:Rotor, plugboard:Plugboard, rotor_states:str=None, ring_positions:str=None):

        self.reflector = reflector
        self.left_rotor = left_rotor
        self.middle_rotor = middle_rotor
        self.right_rotor = right_rotor
        self.plugboard = plugboard
        
        if rotor_states is not None:
            self.left_rotor.state = rotor_states[0]
            self.middle_rotor.state = rotor_states[1]
            self.right_rotor.state = rotor_states[2]

        if ring_positions is not None:
            self.left_rotor.set_ring_position(ring_positions[0])
            self.middle_rotor.set_ring_position(ring_positions[1])
            self.right_rotor.set_ring_position(ring_positions[2])

            self.left_rotor.handle_ring_setting()
            self.middle_rotor.handle_ring_setting()
            self.right_rotor.handle_ring_setting()


    def encipher(self, plain_text:str)->str:
        """
        Encrypt a message according to enigma setup
        """
        plain_text = plain_text.upper()
        encoded_text = ""
        for char in plain_text:
            if char is " ":
                encoded_text += char
                continue
            assert char in UPPERCASE_LETTERS

            #Notching rotors
            if self.middle_rotor.is_in_turnover_pos():
                self.middle_rotor.notch()
                self.left_rotor.notch()
            elif self.right_rotor.is_in_turnover_pos():
                self.middle_rotor.notch()
            self.right_rotor.notch()

            temp = self.plugboard.map_plugs(char)
            temp = self.right_rotor.encipher_forward(temp)
            temp = self.middle_rotor.encipher_forward(temp)
            temp = self.left_rotor.encipher_forward(temp)
            temp = self.reflector.encipher(temp)
            temp = self.left_rotor.encipher_backwards(temp)
            temp = self.middle_rotor.encipher_backwards(temp)
            temp = self.right_rotor.encipher_backwards(temp)
            temp = self.plugboard.map_plugs(temp)
            
            encoded_text += temp
        return encoded_text

    def __str__(self):
        """Pretty display."""
        return """
        Reflector: {}
        Rotor 1: {}
        Rotor 2: {}
        Rotor 3: {}""".format(
            self.reflector, self.left_rotor, self.middle_rotor, self.right_rotor
        )