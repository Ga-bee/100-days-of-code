import pandas as pd 

csv = pd.read_csv('./nato_phonetic_alphabet.csv')
df = pd.DataFrame(csv)

dictionay = {row.letter:row.code for index,row in df.iterrows()}
#print(dictionay)
while True:
    try:
        ask_name = input("Enter a word:").upper()
        dict_name = [letter for letter in ask_name]
        natoName = {letter: dictionay[letter] for letter in ask_name}
    except KeyError:
        print('This is not a valid word please try again.')
    else:
        break



print(natoName)

