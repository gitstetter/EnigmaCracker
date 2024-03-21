def calculate_ioc(text:str)->float:
    """
    Function to calculate the Index of Coincidence (IoC)
    For random 26-letter text the IC is approximately 0.038; standard German shows about 0.07.
    """
    text:str = text.lower()
    
    # Initialize a dictionary to store letter frequencies
    frequencies:dict = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
    
    # Count the occurrences of each letter
    total_letters:int = 0  # Variable to count total letters in the text
    for char in text:
        if char.isalpha():  # Only consider alphabetical characters, no whitespace
            frequencies[char] += 1
            total_letters += 1
    
    # Calculate the numerator of the IoC formula
    numerator:int = sum(frequencies[char] * (frequencies[char] - 1) for char in frequencies.keys())
    
    # Calculate the denominator of the IoC formula
    denominator:int = total_letters * (total_letters - 1)
    
    # Calculate the IoC
    ioc:float = numerator / denominator
    
    return ioc

def main():
    text_ciphered = "BKREVE BMLVYMAO QCY RC YESNRP PE LXWLQCAEBJ ZOT ACWISMP XGQ UKBDCFZC BFH KPRU VGCSMLDH ZFS DMC GQBY VFVRFXEP YYGGSDLTVBCD"
    text = 'Enigma messages can be solved by recovering the message key settings the ring settings and the plug settings individually'
    ioc = calculate_ioc(text)
    print("Index of Coincidence:", ioc)
    ioc = calculate_ioc(text_ciphered)
    print("Index of Coincidence:", ioc)

if __name__ == "__main__":
    main()