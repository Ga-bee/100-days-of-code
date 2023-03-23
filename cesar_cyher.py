alphabet =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
             'u', 'v', 'w', 'x', 'y', 'z']


def cesar(mode,text,shift):
    word = ''

    for letter in text:
        position = alphabet.index(letter) + shift

        if mode == 'encode':
            if position> len(alphabet):
                sub = (position) - len(alphabet)
                word += alphabet[sub]
            elif position < len(alphabet):
                word += alphabet[position]

            print(f"Your message encrypted is {word}")      
        
        elif mode == 'decode':
            word += alphabet[alphabet.index(letter) - shift]

            print(f"Your message decrypted is {word}")
    return

print("""
░█████╗░░█████╗░███████╗░██████╗░█████╗░██████╗░  ░█████╗░██╗██████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗  ██╔══██╗██║██╔══██╗██║░░██║██╔════╝██╔══██╗
██║░░╚═╝███████║█████╗░░╚█████╗░███████║██████╔╝  ██║░░╚═╝██║██████╔╝███████║█████╗░░██████╔╝
██║░░██╗██╔══██║██╔══╝░░░╚═══██╗██╔══██║██╔══██╗  ██║░░██╗██║██╔═══╝░██╔══██║██╔══╝░░██╔══██╗
╚█████╔╝██║░░██║███████╗██████╔╝██║░░██║██║░░██║  ╚█████╔╝██║██║░░░░░██║░░██║███████╗██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝  ░╚════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝""")

mode = str(input("Type 'encode' to encrypt or 'decode' to decrypt.\n")).lower()
text = input('Type your message.\n').lower()
shift = int(input('Type the shift number.\n'))
fora = numero%26

cesar(mode,text,shift)