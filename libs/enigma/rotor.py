UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Rotor:
    """
    Represents a Rotor that maps characters pairwise and turns the rotor to the right notches
    """

    def __init__(self, wiring:str=None, name:str=None, ring_position:int=1, rotor_position:int=1, notch_position:str=None):
        if wiring is not None:
            self.wiring = wiring
        else:
            self.wiring = UPPERCASE_LETTERS
        self.name = name
        self.notch_position = notch_position.upper()
        self.ring_position = ring_position
        self.rotor_position = rotor_position
        
        self.rev_wiring = ["0"] * 26
        for i in range(0, len(self.wiring)):
            index = ord(self.wiring[i])- ord("A")
            self.rev_wiring[index] = chr(ord("A") + i)
        self.rev_wiring = ''.join(self.rev_wiring)
    
    def __setattr__(self, name: str, value) -> None:
        self.__dict__[name] = value


    def __eq__(self, rotor) -> bool:
        return self.name == rotor.name


    def set_ring_position(self, ring_position:int = 1):
        assert type(ring_position) is int
        assert ring_position < 27
        self.ring_position = ring_position

    def encipher_forward(self, key: str) -> str:
        assert type(key) is str
        assert len(key) == 1
        key = key.upper()
        assert key in UPPERCASE_LETTERS
        index = (ord(key) - ord("A"))
        #Account for current rotor position
        rotor_shift = self.rotor_position - self.ring_position


        wired = self.wiring[(index + rotor_shift +26)%26]
        wired2 =(ord(wired)-rotor_shift +26)%26
        letter = chr(wired2)
        print(letter)
        
        return letter
    

    # mapping[(k + shift + 26) % 26] - shift + 26) % 26;


    def encipher_backwards(self, key: str) -> str:
        assert type(key) is str
        assert len(key) == 1
        key = key.upper()
        assert key in UPPERCASE_LETTERS
        index = (ord(key) - ord("A"))
        #Account for current rotor position
        rotor_shift = self.rotor_position
        index = (index + rotor_shift-1)%26
        letter = self.rev_wiring[index]
        return letter

    
    def notch(self) -> None:
        self.rotor_position = self.rotor_position + 1 if self.rotor_position <26 else 1


    def is_in_turnover_pos(self) -> bool:
        return self.rotor_position == ord(self.notch_position) - ord("A")


ROTOR_I = Rotor(wiring="EKMFLGDQVZNTOWYHXUSPAIBRCJ", name="Rotor_I", ring_position=1, rotor_position=1, notch_position='R')
ROTOR_II = Rotor(wiring="AJDKSIRUXBLHWTMCQGZNPYFVOE", name="Rotor_II", ring_position=1, rotor_position=1, notch_position='F')
ROTOR_III = Rotor(wiring="BDFHJLCPRTXVZNYEIWGAKMUSQO", name="Rotor_III", ring_position=1, rotor_position=1, notch_position='W')
ROTOR_IV = Rotor(wiring="ESOVPZJAYQUIRHXLNFTGKDCMWB", name="Rotor_IV", ring_position=1, rotor_position=1, notch_position='K')
ROTOR_V = Rotor(wiring="VZBRGITYUPSDNHLXAWMJQOFECK", name="Rotor_V", ring_position=1, rotor_position=1, notch_position='A')