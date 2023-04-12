import pandas as pd 

csv = pd.read_csv('./nato_phonetic_alphabet.csv')
df = pd.DataFrame(csv)

dictionay = {row.letter:row.code for index,row in df.iterrows()}
print(dictionay)

ask_name = input("What's your name??").upper()
dict_name = [letter for letter in ask_name]

natoName = {letter: dictionay[letter] for letter in ask_name}

print(natoName)

