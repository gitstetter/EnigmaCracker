from rotor import Rotor, ROTOR_I, ROTOR_II, ROTOR_III, ROTOR_IV, ROTOR_V
from reflector import Reflector, REFLECTOR_A, REFLECTOR_B, REFLECTOR_C

class Enigma:
    """Represents an Enigma machine.
    """

    def __init__(self, reflector: Reflector, rotor1: Rotor, rotor2: Rotor, rotor3: Rotor, state="AAA", plugboard_settings: str="AA BB CC DD EE FF GG HH II JJ", ring="AAA"):

        self.reflector = reflector
        self.rotor1 = rotor1
        self.rotor2 = rotor2
        self.rotor3 = rotor3

        self.rotor1.state = state[0]
        self.rotor2.state = state[1]
        self.rotor3.state = state[2]
        self.rotor1.ring = ring[0]
        self.rotor2.ring = ring[1]
        self.rotor3.ring = ring[2]

        plugboard_settings = [(plugpair[0], plugpair[1]) for plugpair in plugboard_settings.split(sep=' ')]

        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        alpha_out = [" "] * 26
        for i in range(len(alpha)):
            alpha_out[i] = alpha[i]
        for k, v in plugboard_settings:
            alpha_out[ord(k) - ord("A")] = v
            alpha_out[ord(v) - ord("A")] = k

        
        self.transtab = str.maketrans(alpha, "".join(alpha_out))



    def encipher(self, plaintext_in):
        """Encrypt 'plaintext_in'."""
        ciphertext = ""
        plaintext_in_upper = plaintext_in.upper()
        plaintext = plaintext_in_upper.translate(self.transtab)
        for c in plaintext:

            # ignore non alphabetic char
            if not c.isalpha():
                ciphertext += c
                continue

            if self.rotor2.is_in_turnover_pos():
                self.rotor2.notch()
                self.rotor3.notch()
            if self.rotor1.is_in_turnover_pos():
                self.rotor2.notch()

            self.rotor1.notch()

            t = self.rotor1.encipher_right(c)
            t = self.rotor2.encipher_right(t)
            t = self.rotor3.encipher_right(t)
            t = self.reflector.encipher(t)
            t = self.rotor3.encipher_left(t)
            t = self.rotor2.encipher_left(t)
            t = self.rotor1.encipher_left(t)
            ciphertext += t

        res = ciphertext.translate(self.transtab)

        fres = ""
        for idx, char in enumerate(res):
            if plaintext_in[idx].islower():
                fres += char.lower()
            else:
                fres += char
        return fres

    def __str__(self):
        """Pretty display."""
        return """
        Reflector: {}
        Rotor 1: {}
        Rotor 2: {}
        Rotor 3: {}""".format(
            self.reflector, self.rotor1, self.rotor2, self.rotor3
        )