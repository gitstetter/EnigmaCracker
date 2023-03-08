class Rotor:
    """
    Represents a Rotor  
    """

    def __init__(self, wiring:str=None, name:str=None, notchPosition:int=None, rotorPosition:int=None):
        if wiring != None:
            self.wiring = wiring
        else:
            self.wiring =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.name = name
        self.notchPosition = notchPosition
        self.rotorPosition = rotorPosition
        
        self.rwiring = ["0"] * 26
        for i in range(0, len(self.wiring)):
            index = ord(self.wiring[i])- ord("A")
            self.rwiring[index] = chr(ord("A") + i)
        self.rwiring = ''.join(self.rwiring)
    
    def __setattr__(self, name: str, value) -> None:
        self.__dict__[name] = value

    def __eq__(self, rotor) -> bool:
        return self.name == rotor.name

    def encipher_forward(self, key: str):
        assert type(key) == str
        assert len(key) == 1
        key = key.upper()
        assert key in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        index = (ord(key) - ord("A"))
        letter = self.wiring[index]
        print("letter forward: "+letter)
        return letter
    
    def encipher_backwards(self, key: str):
        assert type(key) == str
        assert len(key) == 1
        key = key.upper()
        assert key in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        index = (ord(key) - ord("A"))
        letter = self.rwiring[index]
        print("letter backwards: "+letter)
        print(self.rwiring)
        print('wiring:  '+self.wiring)
        return letter

ROTOR_I = Rotor(wiring="EKMFLGDQVZNTOWYHXUSPAIBRCJ", name="Rotor_I", rotorPosition=1, notchPosition=1)
ROTOR_II = Rotor(wiring="AJDKSIRUXBLHWTMCQGZNPYFVOE", name="Rotor_II", rotorPosition=1, notchPosition=1)
ROTOR_III = Rotor(wiring="BDFHJLCPRTXVZNYEIWGAKMUSQO", name="Rotor_III", rotorPosition=1, notchPosition=1)
ROTOR_IV = Rotor(wiring="ESOVPZJAYQUIRHXLNFTGKDCMWB", name="Rotor_IV", rotorPosition=1, notchPosition=1)
ROTOR_V = Rotor(wiring="VZBRGITYUPSDNHLXAWMJQOFECK", name="Rotor_V", rotorPosition=1, notchPosition=1)


