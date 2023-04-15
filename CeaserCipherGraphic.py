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
# This has a graphical interfaze to make it a complete program.

import tkinter as tk
from tkinter import messagebox

# Caesar cipher function that encrypts or decrypts the input text based on the given shift value
def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if mode == 'decrypt':
                    shifted -= 2 * shift
                result += chr((shifted - ord('a')) % 26 + ord('a'))
            else:
                if mode == 'decrypt':
                    shifted -= 2 * shift
                result += chr((shifted - ord('A')) % 26 + ord('A'))
        else:
            result += char
    return result

# Function to be called when the "Process" button is clicked
def process_message():
    mode = mode_var.get()
    try:
        shift = int(shift_entry.get())
        if shift < 1 or shift > 25:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Invalid shift value. Please enter a number between 1 and 25.")
        return

    message = message_text.get("1.0", tk.END).strip()
    result = caesar_cipher(message, shift, mode)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, result)

# Create the main window
root = tk.Tk()
root.title("Caesar Cipher")

# Create the mode selection radio buttons
mode_var = tk.StringVar(value='encrypt')
encrypt_rb = tk.Radiobutton(root, text="Encrypt", variable=mode_var, value='encrypt')
decrypt_rb = tk.Radiobutton(root, text="Decrypt", variable=mode_var, value='decrypt')
encrypt_rb.grid(row=0, column=0, sticky="w")
decrypt_rb.grid(row=0, column=1, sticky="w")

# Create the shift value input field
shift_label = tk.Label(root, text="Shift value (1-25):")
shift_entry = tk.Entry(root)
shift_label.grid(row=1, column=0, sticky="e")
shift_entry.grid(row=1, column=1, sticky="w")

# Create the message input field
message_label = tk.Label(root, text="Message:")
message_text = tk.Text(root, wrap=tk.WORD, height=5)
message_label.grid(row=2, column=0, sticky="e")
message_text.grid(row=2, column=1, sticky="w")

# Create the "Process" button
process_button = tk.Button(root, text="Process", command=process_message)
process_button.grid(row=3, columnspan=2)

# Create the result display field
result_label = tk.Label(root, text="Result:")
result_text = tk.Text(root, wrap=tk.WORD, height=5)
result_label.grid(row=4, column=0, sticky="e")
result_text.grid(row=4, column=1, sticky="w")

# Run the main loop
root.mainloop()
