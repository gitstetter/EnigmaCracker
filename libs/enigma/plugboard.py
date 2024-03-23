UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Plugboard:
    """
    Represents a Plugboard that maps characters according to the plug settings of the enigma machine
    """

    def __init__(self, plug_settings: str = "AA BB CC DD EE FF GG HH II JJ") -> None:
        self.plug_input = plug_settings
        self.plug_settings = [(pair[0].upper(), pair[1].upper()) for pair in plug_settings.split(' ')]

        assert len(self.plug_settings)<=10

        #check for duplicate values in settings
        for mapping_pair in self.plug_settings:
            temp=self.plug_settings.copy()
            temp.remove(mapping_pair)
            assert mapping_pair[0] not in str(temp)
            assert mapping_pair[1] not in str(temp)

        self.mapping = {letter:letter for letter in UPPERCASE_LETTERS}

        for pair0, pair1 in self.plug_settings: 
            self.mapping.update({pair0:pair1})
            self.mapping.update({pair1:pair0})

    def map_plug(self, key:str):
        """
        Maps a character to its counterpart according to a plug setting.
        """
        return self.mapping[key]
    
    def __str__(self):
        """
        Pretty display.
        """
        return str(self.plug_input)
    


