class Rotor:
    """
    Represents a Rotor that maps characters pairwise and turns once the rotor to the right notches
    """

    def __init__(self, wiring:str=None, name:str=None, ring_position:int=1, rotor_position:str='A', notch_position:str=None):
        if wiring != None:
            self.wiring = wiring
        else:
            self.wiring =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.name = name
        self.notch_position = notch_position.upper()
        self.ring_position = ring_position
        self.rotor_position = rotor_position.upper()
        
        self.rev_wiring = ["0"] * 26
        for i in range(0, len(self.wiring)):
            index = ord(self.wiring[i])- ord("A")
            self.rev_wiring[index] = chr(ord("A") + i)
        self.rev_wiring = ''.join(self.rev_wiring)
    
    def __setattr__(self, name: str, value) -> None:
        self.__dict__[name] = value

    def __eq__(self, rotor) -> bool:
        return self.name == rotor.name

    def handle_ring_settings(self) -> None:
        assert type(self.ring_position) is int
        assert self.ring_position < 27
        self.rotor_position = chr((ord(self.rotor_position) + self.ring_position-1 - ord("A")) % 26 + ord("A"))

    def set_ring_position(self, ring_position:int = 1):
        self.ring_position = ring_position
        self.handle_ring_settings()

    def handle_state(self):
        pass

    def encipher_forward(self, key: str) -> str:
        assert type(key) is str
        assert len(key) == 1
        key = key.upper()
        assert key in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        index = (ord(key) - ord("A"))
        letter = self.wiring[index]
        return letter
    
    def encipher_backwards(self, key: str) -> str:
        assert type(key) is str
        assert len(key) == 1
        key = key.upper()
        assert key in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        index = (ord(key) - ord("A"))
        letter = self.rev_wiring[index]
        return letter
    
    def notch(self) -> None:
        self.rotor_position = chr((ord(self.rotor_position) + 1 - ord("A")) % 26 + ord("A"))

    def is_in_turnover_pos(self) -> bool:
        return chr((ord(self.rotor_position) + 1 - ord("A")) % 26 + ord("A")) in self.notch_position


ROTOR_I = Rotor(wiring="EKMFLGDQVZNTOWYHXUSPAIBRCJ", name="Rotor_I", ring_position=1, rotor_position='A', notch_position='R')
ROTOR_II = Rotor(wiring="AJDKSIRUXBLHWTMCQGZNPYFVOE", name="Rotor_II", ring_position=1, rotor_position='A', notch_position='F')
ROTOR_III = Rotor(wiring="BDFHJLCPRTXVZNYEIWGAKMUSQO", name="Rotor_III", ring_position=1, rotor_position='A', notch_position='W')
ROTOR_IV = Rotor(wiring="ESOVPZJAYQUIRHXLNFTGKDCMWB", name="Rotor_IV", ring_position=1, rotor_position='A', notch_position='K')
ROTOR_V = Rotor(wiring="VZBRGITYUPSDNHLXAWMJQOFECK", name="Rotor_V", ring_position=1, rotor_position='A', notch_position='A')