UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Rotor:
    """
    Represents a Rotor that maps characters pairwise and turns the rotor to the right notches.
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

    def __str__(self) -> str:
        return self.name    
    
    def __len__(self):
        return len(self.name)

    def set_ring_position(self, ring_position:int = 1):
        """
        Convenience method for setting the ring position af a rotor.
        """
        assert type(ring_position) is int
        assert ring_position < 27
        self.ring_position = ring_position

    def encipher(self, key: str, mapping: str) -> str:
        """
        Maps a character to its counterpart and the defined mapping.        
        """
        assert type(key) is str
        assert len(key) == 1
        key = key.upper()
        assert key in UPPERCASE_LETTERS
        index = (ord(key) - ord("A"))%26
        rotor_shift = self.rotor_position - self.ring_position
        index = (index + rotor_shift)%26
        letter = mapping[index]
        letter = chr(ord("A") + (ord(letter) - ord("A") + 26 - rotor_shift) % 26)

        return letter

    def encipher_forward(self, key: str) -> str:
        """
        Simulates the forward pass of a character through a rotor.
        """
        return self.encipher(key=key, mapping=self.wiring)

    def encipher_backwards(self, key: str) -> str:
        """
        Simulates the backward pass of a character through a rotor.
        """
        return self.encipher(key=key, mapping=self.rev_wiring)

    def notch(self) -> None:
        """
        Turns a rotor by one position.
        """
        self.rotor_position = self.rotor_position + 1 if self.rotor_position <26 else 1

    def is_in_turnover_pos(self) -> bool:
        """
        Determines if a rotor is in turnover position for the next rotor.
        """
        return self.rotor_position == ord(self.notch_position) - ord("A")


ROTOR_I = Rotor(wiring="EKMFLGDQVZNTOWYHXUSPAIBRCJ", name="I", ring_position=1, rotor_position=1, notch_position='R')
ROTOR_II = Rotor(wiring="AJDKSIRUXBLHWTMCQGZNPYFVOE", name="II", ring_position=1, rotor_position=1, notch_position='F')
ROTOR_III = Rotor(wiring="BDFHJLCPRTXVZNYEIWGAKMUSQO", name="III", ring_position=1, rotor_position=1, notch_position='W')
ROTOR_IV = Rotor(wiring="ESOVPZJAYQUIRHXLNFTGKDCMWB", name="IV", ring_position=1, rotor_position=1, notch_position='K')
ROTOR_V = Rotor(wiring="VZBRGITYUPSDNHLXAWMJQOFECK", name="V", ring_position=1, rotor_position=1, notch_position='A')