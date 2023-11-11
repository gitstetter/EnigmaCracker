from libs.enigma.rotor import ROTOR_I, ROTOR_II, ROTOR_III, ROTOR_IV, ROTOR_V
from libs.enigma.reflector import REFLECTOR_A, REFLECTOR_B, REFLECTOR_C
from libs.enigma.enigma import Enigma
from libs.enigma.plugboard import Plugboard

EnigmaMachine2 = Enigma(reflector=REFLECTOR_B, 
                       left_rotor=ROTOR_III, 
                       middle_rotor=ROTOR_II, 
                       right_rotor=ROTOR_I, 
                       rotor_positions="16 10 1" ,
                       ring_positions="3 1 17",
                       plugboard=Plugboard()
                       )

x=EnigmaMachine2.encipher('ABCDEFGHIJKLMNOPQRSTUVWXYZAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBABCDEFGHIJKLMNOPQRSTUVWXYZ')

print('result is')
print(x)

# ROTOR_I.encipher_forward('B')