from libs.enigma.rotor import ROTOR_I, ROTOR_II, ROTOR_III, ROTOR_IV, ROTOR_V
from libs.enigma.reflector import REFLECTOR_A, REFLECTOR_B, REFLECTOR_C
from libs.enigma.enigma import Enigma
from libs.enigma.plugboard import Plugboard

EnigmaMachine = Enigma(reflector=REFLECTOR_B, rotor1=ROTOR_I, rotor2=ROTOR_II, rotor3=ROTOR_III, rotor_states="ABC" ,plugboard=Plugboard(plug_settings="AV BS CG DL FU HZ IN KM OW RX"))
x=EnigmaMachine.encipher('E')

print(x)