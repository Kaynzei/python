#read about the caser cipher encryption to understand this. its used to encode information by kings in the past.
#a arange of aphabet are alighned perpendular to each other.(abcdef/ABCDEF) to code def with 2 shifts to the left, 
#it will result to efg.You can code any word hello might yield mjqqt

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n','o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n','o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text =input('Type your message:\n').lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text , shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter) #This is collecting the word given and looking for the index in alphabet bank above, after which adds the shift number to it
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")

encrypt(plain_text=text , shift_amount= shift)