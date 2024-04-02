def erypt(text,shift):
    cipher_str=''
    for letter in text:
        possion=alphabet.index(letter)
        new_possition=possion+shift
        new_letter=alphabet[new_possition]
        cipher_str+=new_letter

    print(f"The encoded text is {cipher_str}")

    Plain_text=''
    for letter in text:
        possion = alphabet.index(letter)
        new_possition = possion - shift
        new_letter = alphabet[new_possition]
        Plain_text += new_letter
    print(f"The de-coded text is {Plain_text}")




alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
if direction.lower()=='encode':
    encrypt(text,shift)
elif direction.lower()=='decode':
    decrypyt(text,5)

