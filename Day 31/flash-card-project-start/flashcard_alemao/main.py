from tkinter import *
import pandas as pd
from random import choice
import time

chosen = {}
BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pd.read_csv('../data/words_to_learn_german.csv')
except FileNotFoundError:
    file = pd.read_csv('../data/German_words.txt.csv')
    to_learn = file.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient="records")
# print(file_file)


##----------------------remove right words------------------

def is_known():
    to_learn.remove(chosen)
    generate_words()
    data = pd.DataFrame(to_learn)
    data.to_csv('../data/german_words.txt.csv',index=False)



##--------------------- Generate words -----------------------

def generate_words():
    global chosen
    chosen = choice(to_learn)
    print(chosen, chosen["German"])
    canvas.itemconfig(language_text, text="German")
    canvas.itemconfig(word_text, text=chosen["German"])
    word_label.config(text=chosen["German"])

    canvas.itemconfig(card_image, image= card_front)

    window.after(5000, original_language)

#    word_label.config(text=words["English"])


# ##---------------------- UI Setup ----------------------------

window = Tk()
window.title('Flashcard App')
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

card_back = PhotoImage(file="../images/card_back.png")
card_front = PhotoImage(file="../images/card_front.png")


right_button_image=PhotoImage(file="../images/right.png")
wrong_button_image=PhotoImage(file="../images/wrong.png")

w_button = Button(image=wrong_button_image, highlightthickness=0,command=generate_words)
w_button.grid(row=1,column=0)

r_button = Button(image=right_button_image, highlightthickness=0,command=is_known)
r_button.grid(row=1,column=1)

language_label = Label(font=('Arial', 40, 'italic'), text='German')
word_label = Label(font=('Arial', 60, 'bold'), text='English')


canvas = Canvas(width=800,height=526)
card_image = canvas.create_image(400,263,image= card_front)
language_text =  canvas.create_text(400,100,text='language', font=('Arial', 40, 'italic'))
word_text = canvas.create_text(400,250,text='word', font=('Arial', 60, 'bold'))


canvas.config(bg= BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0,columnspan=2)


def original_language():
    canvas.itemconfig(card_image,image= card_back)
    canvas.itemconfig(language_text ,text='English')
    canvas.itemconfig(word_text,text=chosen["English"])
window.after(10,generate_words )
window.after(5000, original_language)



window.mainloop()