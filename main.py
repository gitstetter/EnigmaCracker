from libs.enigma.rotor import ROTOR_I, ROTOR_II, ROTOR_III, ROTOR_IV, ROTOR_V
from libs.enigma.reflector import REFLECTOR_A, REFLECTOR_B, REFLECTOR_C
from libs.enigma.enigma import Enigma
from libs.enigma.plugboard import Plugboard

EnigmaMachine2 = Enigma(reflector=REFLECTOR_B, 
                       left_rotor=ROTOR_I, 
                       middle_rotor=ROTOR_II, 
                       right_rotor=ROTOR_III, 
                       rotor_positions="A A A" ,
                       ring_positions="5 7 1",
                       plugboard=Plugboard()
                       )

x=EnigmaMachine2.encipher('E')

print(x)