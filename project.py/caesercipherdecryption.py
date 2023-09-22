#Decrypt

def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
    print(f"The decoded text is {plain_text}")

#The direction variable

if direction == "encode":
    encrypt(plain_text=text , shift_amount= shift)
elif direction == "decode":
    decrypt(cipher_text=text , shift_amount= shift)