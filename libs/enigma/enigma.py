from .rotor import Rotor
from .reflector import Reflector
from .plugboard import Plugboard

UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Enigma:
    """
    Represents an Enigma machine to be used for encrypting messages.
    """

    def __init__(self, reflector:Reflector, left_rotor:Rotor, middle_rotor:Rotor, right_rotor:Rotor, plugboard:Plugboard, rotor_positions:str="1 1 1", ring_positions:str="1 1 1"):

        self.reflector = reflector
        self.left_rotor = left_rotor
        self.middle_rotor = middle_rotor
        self.right_rotor = right_rotor
        self.plugboard = plugboard

        self.rotor_positions = rotor_positions.split()
        assert len(self.rotor_positions)==3
        self.ring_positions = ring_positions.split()
        assert len(self.ring_positions)==3

        self.left_rotor.rotor_position = int(self.rotor_positions[0])
        self.middle_rotor.rotor_position = int(self.rotor_positions[1])
        self.right_rotor.rotor_position = int(self.rotor_positions[2])

        self.left_rotor.set_ring_position(int(self.ring_positions[0]))
        self.middle_rotor.set_ring_position(int(self.ring_positions[1]))
        self.right_rotor.set_ring_position(int(self.ring_positions[2]))

    @classmethod
    def from_dict(cls, configs: dict):
        """
        Alternative constructor for configs which have been 
        exported by export_settings method
        """
        return cls(configs['reflector'],configs['left_rotor'],configs['middle_rotor'],configs['right_rotor'],
                Plugboard(configs['plug_settings']),configs['rotor_positions'], configs['ring_positions'],)
        

    def __setattr__(self, name: str, value) -> None:
        self.__dict__[name] = value

    def rotate(self) -> None:
        """
        Rotates the three rotors according if a rotor is in turnover position.
        """
        if self.middle_rotor.is_in_turnover_pos():
            self.middle_rotor.notch()
            self.left_rotor.notch()
        elif self.right_rotor.is_in_turnover_pos():
            self.middle_rotor.notch()
        self.right_rotor.notch()

    def encipher(self, plain_text:str)->str:
        """
        Encrypts a message by passing each character given the current enigma 
        setup through the plugboard, rotors, reflector and back.
        """
        plain_text = plain_text.upper()
        encoded_text = ""
        for char in plain_text:
            if char in [" ", ",",".",":",";","-","_","=","?","%","&","(",")","[","]"]:
                encoded_text += char
                continue
            assert char in UPPERCASE_LETTERS

            self.rotate()

            temp = self.plugboard.map_plug(char)
            temp = self.right_rotor.encipher_forward(temp)
            temp = self.middle_rotor.encipher_forward(temp)
            temp = self.left_rotor.encipher_forward(temp)
            temp = self.reflector.encipher(temp)
            temp = self.left_rotor.encipher_backwards(temp)
            temp = self.middle_rotor.encipher_backwards(temp)
            temp = self.right_rotor.encipher_backwards(temp)
            temp = self.plugboard.map_plug(temp)
            
            encoded_text += temp
        return encoded_text
    
    def export_settings(self) -> dict:
        """
        Export the instance of the enigma machine as dictionary.
        Rotor and ring positions, as well as the plugboard settings are persisted.
        To be used with from_dict method.
        """
        return {
        'reflector': self.reflector,
        'left_rotor': self.left_rotor,
        'middle_rotor': self.middle_rotor,
        'right_rotor': self.right_rotor,
        'rotor_positions': f'{self.left_rotor.rotor_position} {self.middle_rotor.rotor_position} {self.right_rotor.rotor_position}',
        'ring_positions': f'{self.left_rotor.ring_position} {self.middle_rotor.ring_position} {self.right_rotor.ring_position}',
        'plug_settings': f'{self.plugboard}'
        }

    def __str__(self):
        """
        Pretty display.
        """
        return f"""reflector: '{self.reflector}',
        left_rotor: '{self.left_rotor}',
        middle_rotor: '{self.middle_rotor}',
        right_rotor: '{self.right_rotor}',
        rotor_positions: '{self.left_rotor.rotor_position} {self.middle_rotor.rotor_position} {self.right_rotor.rotor_position}',
        ring_positions: '{self.left_rotor.ring_position} {self.middle_rotor.ring_position} {self.right_rotor.ring_position}',
        plug_settings: '{self.plugboard}'"""