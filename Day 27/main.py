from tkinter import *


#Creating window
window = Tk()

window.title('My first Tkinter program')
window.minsize(500,300)
window.config(padx=30,pady=30)


#creating label

my_label = Label(text='Labeeel',font=('Comic Sans',24,'bold'))
my_label.grid(column=0,row=0)
#chaning the text
my_label['text'] = 'new text'
#or
my_label.config(text='newer text')

#button

input = Entry(width=15)
input.grid(column=3, row=2)

def button_clicked():
    print('igot clicked')
    text = input.get()
    my_label.config(text=text)


def clicavai():
    my_label.config(text='te peguei')
button = Button(text='click me', command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text='new button',command=clicavai)
new_button.grid(column=2, row=0)






def add(*args):
    i = 0
    for n in args:
        i += n
        
    print(i)

# add(2,3,4)











window.mainloop()