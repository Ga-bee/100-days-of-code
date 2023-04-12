from tkinter import *

window = Tk()
window.title('Mile to Km Converter')
window.minsize(500,200)
window.config(padx=20,pady=20)

#entry1
input = Entry()
input.insert(END, string="Entry the miles")
input.grid(row=0,column=1)

#label 1
miles = Label(text='Miles')
miles.grid(row=0,column=2)

#label 2
equal = Label(text='is equal to')
equal.grid(row=1,column=0)

#label 3
km = Label(text='Km')
km.grid(row=1,column=2)

#output
def calculate():
    mile = input.get()
    km = mile *  1,609344
    result = Label()
    result.config(text = km)
    result.grid(row=1,column=1)


#button
button = Button()
button.config(text='calculate',command=calculate)
button.grid(column=1, row=2)
window.mainloop()