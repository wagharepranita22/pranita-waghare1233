import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(text, shift, direction):
    end_txt=' '
    if direction == "decode":
        shift*=-1
    for letter in  text:
        if letter in alphabet:
            possition = alphabet.index(letter)
            new_position = possition+shift
            end_txt += alphabet[new_position]
        else:
            end_txt+=letter
    print(f"The {direction} text is {end_txt}")
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(text=text,shift=shift,direction=direction)
    result = input("Type Yes if  want to continue ,otherwise type no : ").lower()
    if result == "no":
        print("Good bye !")
        break



# MY solution
# def caesar(text,shift,direction):
#     if direction=="encode":
#         cipher_str=''
#         for letter in text:
#             possion=alphabet.index(letter)
#             new_possition=possion+shift
#             new_letter=alphabet[new_possition]
#             cipher_str+=new_letter
#
#         print(f"The encoded text is {cipher_str}")
#     elif direction=="decode":
#         Plain_text=''
#         for letter in text:
#             possion = alphabet.index(letter)
#             new_possition = possion - shift
#             new_letter = alphabet[new_possition]
#             Plain_text += new_letter
#         print(f"The de-coded text is {Plain_text}")

