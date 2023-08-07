from . rotor import Rotor
from . reflector import Reflector
from . plugboard import Plugboard

UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Enigma:
    """
    Represents an Enigma machine.
    """

    def __init__(self, reflector:Reflector, left_rotor:Rotor, middle_rotor:Rotor, right_rotor:Rotor, plugboard:Plugboard, rotor_positions:str="A A A", ring_positions:str="1 1 1"):

        self.reflector = reflector
        self.left_rotor = left_rotor
        self.middle_rotor = middle_rotor
        self.right_rotor = right_rotor
        self.plugboard = plugboard

        self.rotor_positions = rotor_positions.split()
        assert len(self.rotor_positions)==3
        self.ring_positions = ring_positions.split()
        assert len(self.ring_positions)==3

        self.left_rotor.rotor_position = self.rotor_positions[0]
        self.middle_rotor.rotor_position = self.rotor_positions[1]
        self.right_rotor.rotor_position = self.rotor_positions[2]

        self.left_rotor.set_ring_position(int(self.ring_positions[0]))
        self.middle_rotor.set_ring_position(int(self.ring_positions[1]))
        self.right_rotor.set_ring_position(int(self.ring_positions[2]))

    def rotate(self):
        #Notching rotors
        if self.middle_rotor.is_in_turnover_pos() and self.right_rotor.is_in_turnover_pos():
            self.middle_rotor.notch()
            self.left_rotor.notch()
        elif self.right_rotor.is_in_turnover_pos():
            self.middle_rotor.notch()
        self.right_rotor.notch()

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

            self.rotate()

            print(char)
            temp = self.plugboard.map_plugs(char)
            print(temp)
            print("right rotor at:",self.right_rotor.rotor_position)
            temp = self.right_rotor.encipher_forward(temp)
            print(temp)
            print("middle rotor at:",self.middle_rotor.rotor_position)
            temp = self.middle_rotor.encipher_forward(temp)
            print(temp)
            print("left rotor at:",self.left_rotor.rotor_position)
            temp = self.left_rotor.encipher_forward(temp)
            print(temp)
            temp = self.reflector.encipher(temp)
            print(temp)
            temp = self.left_rotor.encipher_backwards(temp)
            print(temp)
            temp = self.middle_rotor.encipher_backwards(temp)
            print(temp)
            temp = self.right_rotor.encipher_backwards(temp)
            print(temp)
            temp = self.plugboard.map_plugs(temp)
            print(temp)
            
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