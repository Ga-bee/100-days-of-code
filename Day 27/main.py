# import tkinter


# #Creating window
# window = tkinter.Tk()

# window.title('My first Tkinter program')
# window.minsize(500,300)


# #creating label

# my_label = tkinter.Label(text='Labeeel',font=('Comic Sans',24,'bold'))
# my_label.pack(side='left')

def add(*args):
    i = 0
    for n in args:
        i += n
        
    print(i)

add(2,3,4)











# window.mainloop()