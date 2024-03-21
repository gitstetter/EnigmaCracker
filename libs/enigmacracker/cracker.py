from typing import List, Dict, Any

from libs.enigmacracker.metrics.ioc import calculate_ioc
from libs.enigma.rotor import Rotor, ROTOR_I, ROTOR_II, ROTOR_III, ROTOR_IV, ROTOR_V
from libs.enigma.reflector import Reflector, REFLECTOR_A, REFLECTOR_B, REFLECTOR_C
from libs.enigma.enigma import Enigma
from libs.enigma.plugboard import Plugboard

UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
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
        self.candidates_ring: List[Dict[str, Any]] = []
        self.candidates_plug: List[Dict[str, Any]] = []
        self.seen_plugs:List = []

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
                                    if fitness>=max_fitness:
                                        max_fitness=fitness
                                        optimal_rotors = f"{rotor1.name} {rotor2.name} {rotor3.name}"
                                        optimal_positions = f"{i} {j} {k}"
                                        optimal_enigma = enigma.export_settings()
                                        
                        self.candidates_rotor.append({'max_fitness': max_fitness, "rotors":optimal_rotors, "rotor_positions": optimal_positions, "decryption":decryption,"enigma": optimal_enigma})

        self.candidates_rotor.reverse()
        # print(self.candidates_rotor)

    def find_ring_setting(self, rotor: str = "right") -> int:
        best_candidate = self.candidates_rotor[0]['enigma']
        max_fitness = self.candidates_rotor[0]['max_fitness'] #-1e30
        rotor_positions = self.candidates_rotor[0]['rotor_positions'].split()

        for i in range(1,27):
            enigma=Enigma.from_dict(best_candidate)
            enigma.left_rotor.rotor_position = int(rotor_positions[0])
            enigma.middle_rotor.rotor_position = int(rotor_positions[1])
            enigma.right_rotor.rotor_position = int(rotor_positions[2])

            if rotor.lower()=="right":
                enigma.right_rotor.set_ring_position(ring_position=i)

            if rotor.lower()=="middle":
                enigma.middle_rotor.set_ring_position(ring_position=i)

            if rotor.lower()=="left":
                enigma.left_rotor.set_ring_position(ring_position=i)


            decryption = enigma.encipher(plain_text=self.ciphertext)
            fitness = calculate_ioc(decryption)
            if fitness>=max_fitness:
                max_fitness=fitness
                optimal_position = i

        return optimal_position


    def find_ring_configuration(self):

        # right rotor
        optimal_position_right = self.find_ring_setting('right')

        # middle rotor
        optimal_position_middle = self.find_ring_setting('middle')

        # left rotor
        optimal_position_left = self.find_ring_setting('left')

        best_candidate = self.candidates_rotor[0]['enigma']
        enigma=Enigma.from_dict(best_candidate)

        rotor_positions = self.candidates_rotor[0]['rotor_positions'].split()
        enigma.left_rotor.rotor_position = int(rotor_positions[0])
        enigma.middle_rotor.rotor_position = int(rotor_positions[1])
        enigma.right_rotor.rotor_position = int(rotor_positions[2])

        enigma.right_rotor.set_ring_position(ring_position=optimal_position_right)
        enigma.middle_rotor.set_ring_position(ring_position=optimal_position_middle)
        enigma.left_rotor.set_ring_position(ring_position=optimal_position_left)

        decryption = enigma.encipher(plain_text=self.ciphertext)
        fitness = calculate_ioc(decryption)

        optimal_positions_rotor = f"{rotor_positions[0]} {rotor_positions[1]} {rotor_positions[2]}"
        optimal_positions_rings = f"{enigma.left_rotor.ring_position}, {enigma.middle_rotor.ring_position}, {enigma.right_rotor.ring_position}"
        optimal_enigma = enigma.export_settings()

        self.candidates_ring.append({'max_fitness': fitness,"rotor_positions": optimal_positions_rotor ,"ring_positions": optimal_positions_rings, "enigma": optimal_enigma, "decryption": decryption})
        self.candidates_ring.reverse()
        # print(self.candidates_ring[0])

    def find_plug(self) -> str:
        max_fitness = self.candidates_ring[0]['max_fitness']#-1e30 #
        best_candidate = self.candidates_ring[0]['enigma']

        for i in UPPERCASE_LETTERS:
            for j in UPPERCASE_LETTERS:
                if i == j: continue
                if i in self.seen_plugs or j in self.seen_plugs: continue

                enigma=Enigma.from_dict(best_candidate)
                rotor_positions = self.candidates_rotor[0]['rotor_positions'].split()
                enigma.left_rotor.rotor_position = int(rotor_positions[0])
                enigma.middle_rotor.rotor_position = int(rotor_positions[1])
                enigma.right_rotor.rotor_position = int(rotor_positions[2])


                enigma.plugboard = Plugboard(f"{i}{j}")

                decryption = enigma.encipher(plain_text=self.ciphertext)
                fitness = calculate_ioc(decryption)
                if fitness>=max_fitness:
                    max_fitness=fitness
                    self.seen_plugs.append(i)
                    self.seen_plugs.append(j)
                    return f"{i}{j}"
        
    def find_plug_configuration(self, max_plugs: int = 0):
            assert max_plugs <= 10
            plugs= ""
            for _ in range(max_plugs):
                next_plug = self.find_plug()
                if next_plug != None:
                    plugs = next_plug if not plugs else plugs + " " + next_plug
            print(f"Plugs were found: {plugs}")
            best_candidate = self.candidates_ring[0]['enigma']
            enigma=Enigma.from_dict(best_candidate)
            rotor_positions = self.candidates_rotor[0]['rotor_positions'].split()
            enigma.left_rotor.rotor_position = int(rotor_positions[0])
            enigma.middle_rotor.rotor_position = int(rotor_positions[1])
            enigma.right_rotor.rotor_position = int(rotor_positions[2])
            enigma.plugboard = Plugboard(plugs) if len(plugs) != 0 else Plugboard()
            
            decryption = enigma.encipher(plain_text=self.ciphertext)
            fitness = calculate_ioc(decryption)
            self.candidates_plug.append({'max_fitness': fitness,"rotor_positions": rotor_positions, "plugboard":enigma.plugboard,"enigma": enigma, "decryption": decryption})
            self.candidates_plug.reverse()
            print(self.candidates_plug[0])