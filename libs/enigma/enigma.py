from . rotor import Rotor
from . reflector import Reflector
from . plugboard import Plugboard

UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Enigma:
    """
    Represents an Enigma machine.
    """

    def __init__(self, reflector:Reflector, rotor1:Rotor, rotor2:Rotor, rotor3:Rotor, plugboard:Plugboard, rotor_states:str=None, ring_positions:str=None):

        self.reflector = reflector
        self.rotor1 = rotor1
        self.rotor2 = rotor2
        self.rotor3 = rotor3
        self.plugboard = plugboard
        
        if rotor_states is not None:
            self.rotor1.state = rotor_states[0]
            self.rotor2.state = rotor_states[1]
            self.rotor3.state = rotor_states[2]

        if ring_positions is not None:
            self.rotor1.set_ring_position(ring_positions[0])
            self.rotor2.set_ring_position(ring_positions[1])
            self.rotor3.set_ring_position(ring_positions[2])

            self.rotor1.handle_ring_setting()
            self.rotor2.handle_ring_setting()
            self.rotor3.handle_ring_setting()


    def encipher(self, plaintext)->str:
        """
        Encrypt a message according to enigma setup
        """
        plain_text = plaintext.upper()
        encoded_text = ""
        for char in plain_text:
            if char is " ":
                encoded_text += char
                continue
            assert char in UPPERCASE_LETTERS
            if self.rotor2.is_in_turnover_pos():
                self.rotor2.notch()
                self.rotor3.notch()
            elif self.rotor1.is_in_turnover_pos():
                self.rotor2.notch()
            self.rotor1.notch()

            # if self.rotor1.is_in_turnover_pos():
            #     self.rotor2.notch()
            # if self.rotor2.is_in_turnover_pos():
            #     self.rotor3.notch()
            # self.rotor1.notch()

            temp = self.plugboard.map_plugs(char)
            temp = self.rotor1.encipher_forward(temp)
            temp = self.rotor2.encipher_forward(temp)
            temp = self.rotor3.encipher_forward(temp)
            temp = self.reflector.encipher(temp)
            temp = self.rotor3.encipher_backwards(temp)
            temp = self.rotor2.encipher_backwards(temp)
            temp = self.rotor1.encipher_backwards(temp)
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
            self.reflector, self.rotor1, self.rotor2, self.rotor3
        )