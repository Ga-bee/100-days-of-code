from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"


window = Tk()
window.title('Flashcard App')
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

card_back = PhotoImage(file="./images/card_back.png")
card_front = PhotoImage(file="./images/card_front.png")


right_button_image=PhotoImage(file="./images/right.png")
wrong_button_image=PhotoImage(file="./images/wrong.png")

w_button = Button(image=wrong_button_image, highlightthickness=0)
w_button.grid(row=1,column=0)

r_button = Button(image=right_button_image, highlightthickness=0)
r_button.grid(row=1,column=1)

language_label = Label(font=('Arial', 40, 'italic'), text='German')
word_label = Label(font=('Arial', 60, 'bold'), text='English')


canvas = Canvas(width=200,height=400)
canvas.create_image(20,20,image= card_front)
canvas.grid(row=0, column=0,columnspan=2)

window.mainloop()
