#   _____                              _____            _               
#  / ____|                            / ____|          | |              
# | |     __ _  ___  ___  __ _ _ __  | |    _   _ _ __ | |__   ___ _ __ 
# | |    / _` |/ _ \/ __|/ _` | '__| | |   | | | | '_ \| '_ \ / _ \ '__|
# | |___| (_| |  __/\__ \ (_| | |    | |___| |_| | |_) | | | |  __/ |   
#  \_____\__,_|\___||___/\__,_|_|     \_____\__, | .__/|_| |_|\___|_|   
#                                            __/ | |                    
#                                           |___/|_|                    
# By A.S.

# The following program is for a Ceaser Cypher.
# It is one of the most simple algorithms for cyryptography.
# It works by using a substitution method.
# In it the letters of the alphabet are shifted by a fixed number of spaces.

# Caesar cipher function that encrypts or decrypts the input text based on the given shift value
def caesar_cipher(text, shift, mode='encrypt'):
    # Define the alphabet for the cipher
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # Create a shifted version of the alphabet based on the shift value
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    
    # Create a translation table based on the mode (encrypt/decrypt)
    if mode == 'encrypt':
        cipher = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    else:
        cipher = str.maketrans(shifted_alphabet + shifted_alphabet.upper(), alphabet + alphabet.upper())
    
    # Return the translated text using the translation table
    return text.translate(cipher)

def main():
    # Ask the user to choose the mode (encrypt/decrypt)
    mode = input("Choose mode (encrypt/decrypt): ").lower()
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode. Please choose either 'encrypt' or 'decrypt'.")
        return

    # Ask the user to enter the shift value (1-25)
    shift = int(input("Enter the shift value (1-25): "))
    if shift < 1 or shift > 25:
        print("Invalid shift value. Please enter a number between 1 and 25.")
        return

    # Ask the user to input their message
    message = input("Enter your message: ")
    # Call the caesar_cipher function with the given input
    result = caesar_cipher(message, shift, mode)
    # Print the encrypted or decrypted message
    print(f"\n{'Encrypted' if mode == 'encrypt' else 'Decrypted'} message: {result}")

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
