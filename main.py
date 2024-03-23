from libs.enigma.rotor import ROTOR_I, ROTOR_II, ROTOR_III, ROTOR_IV, ROTOR_V
from libs.enigma.reflector import REFLECTOR_A, REFLECTOR_B, REFLECTOR_C
from libs.enigma.enigma import Enigma
from libs.enigma.plugboard import Plugboard

EnigmaMachine2 = Enigma(reflector=REFLECTOR_B, 
                       left_rotor=ROTOR_III, 
                       middle_rotor=ROTOR_II, 
                       right_rotor=ROTOR_I, 
                       rotor_positions="16 10 1",
                       ring_positions="3 1 17",
                       plugboard=Plugboard("CE KL FP MD")
                     #   plugboard=Plugboard()
                       )

x=EnigmaMachine2.encipher('Jeder Mensch sollte wissen, wie man Enigma-Maschine verwendet. Es ist ein faszinierendes Stueck Geschichte und Technologie. Durch das Studium der Enigma konnen wir die Komplexitaet und den Einfallsreichtum vergangener Generationen besser verstehen. Die Maschine wurde im Zweiten Weltkrieg intensiv genutzt und spielte eine entscheidende Rolle bei der Entschluesselung von Nachrichten. Ihr Einfluss auf die moderne Kryptografie ist nicht zu unterschaetzen. Das Geheimnis der Enigma hat die Neugierde und den Forschungsgeist vieler Menschen auf der ganzen Welt geweckt. Es ist ein Symbol fur den unermuedlichen Drang des Menschen nach Wissen und Innovation. Moge ihr Erbe weiterleben und uns dazu inspirieren, die Geheimnisse der Welt zu erforschen.')

print('result is')
print(x)
print(len(x))
