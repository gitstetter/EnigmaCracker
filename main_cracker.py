from typing import List, Dict, Any

from libs.enigmacracker.metrics.ioc import calculate_ioc
from libs.enigma.rotor import Rotor, ROTOR_I, ROTOR_II, ROTOR_III, ROTOR_IV, ROTOR_V
from libs.enigma.reflector import Reflector, REFLECTOR_A, REFLECTOR_B, REFLECTOR_C
from libs.enigma.enigma import Enigma
from libs.enigma.plugboard import Plugboard

# ROTORS = [ROTOR_I, ROTOR_II, ROTOR_III, ROTOR_IV, ROTOR_V]
ROTORS = [ROTOR_I, ROTOR_II, ROTOR_III]
# REFLECTORS = [REFLECTOR_A, REFLECTOR_B, REFLECTOR_C]
REFLECTORS = [REFLECTOR_B]


class Cracker:
    def __init__(self, rotors: List[Rotor]=ROTORS, reflectors: List[Reflector]=REFLECTORS, plugboard:Plugboard=None, ciphertext:str=""):

        self.rotors = rotors
        self.reflectors = reflectors
        self.plugboard = plugboard
        self.ciphertext = ciphertext
        self.candidates_rotor: List[Dict[str, Any]] = []
        self.candicates_ring: List[Dict[str, Any]] = []
        self.candicates_plug: List[Dict[str, Any]] = []

    def find_rotor_configuration(self):
        max_fitness=-1e30
        for reflector in self.reflectors:
            for rotor1 in self.rotors:
                for rotor2 in self.rotors:
                    if rotor1==rotor2: continue
                    for rotor3 in self.rotors:
                        if rotor1==rotor3 or rotor2==rotor3: continue
                        print(f"{reflector}, {rotor1}, {rotor2}, {rotor3}")

                        for i in range(1,27):
                            for j in range(1,27):
                                for k in range(1,27):
                                    enigma = Enigma(reflector=reflector, left_rotor=rotor1, middle_rotor=rotor2, right_rotor=rotor3, plugboard=Plugboard(), rotor_positions=f"{i} {j} {k}", ring_positions="1 1 1")
                                    decryption = enigma.encipher(plain_text=self.ciphertext)
                                    fitness = calculate_ioc(decryption)
                                    if fitness>max_fitness:
                                        max_fitness=fitness
                                        optimal_rotors = f"{rotor1.name}, {rotor2.name}, {rotor3.name}"
                                        optimal_positions = f"{i} {j} {k}"
                                        optimal_enigma = enigma.export_settings()
                                        
                        self.candidates_rotor.append({'max_fitness': max_fitness, "rotor_positions": optimal_positions, "enigma": optimal_enigma})

        self.candidates_rotor.reverse()
        print(self.candidates_rotor[0])


    def find_ring_setting(self):
        best_candidate = self.candidates_rotor[0]['enigma']
        max_fitness = self.candidates_rotor[0]['max_fitness']
        rotor_positions = self.candidates_rotor[0]['rotor_positions'].split()
        for i in range(1,27):
            enigma=Enigma.from_dict(best_candidate)
            enigma.left_rotor.rotor_position = int(rotor_positions[0])
            enigma.middle_rotor.rotor_position = int(rotor_positions[1])
            enigma.right_rotor.rotor_position = int(rotor_positions[2])
        

cracker = Cracker(ciphertext="XGOOXNCDRJDWALOOWFMJKXUUZTOJXLSSCWFU")
cracker.find_rotor_configuration()
cracker.find_ring_setting()

                        # print(f"{optimal_rotors} {optimal_positions} : {max_fitness}")
                        # x = Enigma.from_dict(optimal_enigma)
                        # print(x)
                        # print(x.encipher(self.ciphertext))
                        # print(x)            