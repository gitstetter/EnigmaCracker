from typing import List


import sys
sys.path.append("./libs")

import os

cwd = os.getcwd()
print("Current working directory:", cwd)

from enigmacracker.metrics.ioc import calculate_ioc
from enigma.rotor import Rotor, ROTOR_I, ROTOR_II, ROTOR_III, ROTOR_IV, ROTOR_V
from enigma.reflector import Reflector, REFLECTOR_A, REFLECTOR_B, REFLECTOR_C
from enigma.enigma import Enigma
from enigma.plugboard import Plugboard

ROTORS = [ROTOR_I, ROTOR_II, ROTOR_III, ROTOR_IV, ROTOR_V]
REFLECTORS = [REFLECTOR_A, REFLECTOR_B, REFLECTOR_C]


class Cracker:
    def __init__(self,enigma:Enigma=None, rotors: List[Rotor]=ROTORS, reflectors: List[Reflector]=REFLECTORS, plugboard:Plugboard=None, ciphertext:str=""):
        # self.enigma=enigma    
        self.rotors = rotors
        self.reflectors = reflectors
        self.plugboard = plugboard
        self.ciphertext = ciphertext

    def find_rotor_configuration(self):


        for rotor1 in self.rotors:
            for rotor2 in self.rotors:
                if rotor1==rotor2: continue
                for rotor3 in self.rotors:
                    if rotor1==rotor3 or rotor2==rotor3: continue
                    print(f"{rotor1}, {rotor2}, {rotor3}")


