class Rotor:
    """
    Represents a Rotor  
    """

    def __init__(self, wiring=None, name=None):
        if wiring != None:
            self.wiring = wiring
        else:
            self.wiring =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.name = name

    
    def __setattr__(self, name: str, value) -> None:
        self.__dict__[name] = value

    def __eq__(self, rotor) -> bool:
        return self.name == rotor.name

    def encipher(self, key: str):
        assert type(key) == str
        assert len(key) == 1
        key = key.upper()
        assert key in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        index = (ord(key) - ord("A"))
        letter = self.wiring[index]
        # print("letter: "+letter)
        return letter