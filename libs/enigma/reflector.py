UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Reflector:
    """
    Represents a reflector which directs current back through thr rotors
    """

    def __init__(self, wiring:str=None, name:str=None):
        if wiring != None:
            self.wiring = wiring
        else:
            self.wiring =  UPPERCASE_LETTERS
        self.name = name

    
    def __setattr__(self, name: str, value) -> None:
        self.__dict__[name] = value

    def __eq__(self, reflector) -> bool:
        return self.name == reflector.name
    
    def __str__(self) -> str:
        return self.name    
    
    def __len__(self):
        return len(self.name)

    def encipher(self, key: str)->str:
        """
        Simulates the passing of a character through the reflector.
        """
        assert type(key) == str
        assert len(key) == 1
        key = key.upper()
        assert key in UPPERCASE_LETTERS
        index = (ord(key) - ord("A"))
        letter = self.wiring[index]
        return letter



REFLECTOR_A = Reflector(wiring="EJMZALYXVBWFCRQUONTSPIKHGD", name="A")
REFLECTOR_B = Reflector(wiring="YRUHQSLDPXNGOKMIEBFZCWVJAT", name="B")
REFLECTOR_C = Reflector(wiring="FVPJIAOYEDRZXWGCTKUQSBNMHL", name="C")
