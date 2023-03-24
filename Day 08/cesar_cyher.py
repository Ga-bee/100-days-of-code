alphabet =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
             'u', 'v', 'w', 'x', 'y', 'z']


def cesar(mode,text,shift):
    word = ''
    if shift > 26:
        shift = shift%26
    
    
    if mode == 'encode':
        for char in text:
            if char in alphabet:
                position = alphabet.index(char) + shift   
                if position> len(alphabet):
                    sub = (position) - len(alphabet)
                    word += alphabet[sub]
                elif position < len(alphabet):
                    word += alphabet[position]
            else:
                word += char
        print(f"Your message encrypted is {word}")      
            
    elif mode == 'decode':
        for char in text:
            if char in alphabet:
                word += alphabet[alphabet.index(char) - shift]
            else:
                word += char
        print(f"Your message decrypted is {word}")


          
    return

def menu():
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
    return mode, text, shift


while True:
    start = menu()

    cesar(start[0],start[1],start[2])
    again= input('Woul you like to go again? Yes or No\n').lower()
    if again == 'yes':
        continue
    else:
        break