import requests as rq
from tkinter import *


def slamano():
    response = rq.get(url="https://www.thecocktaildb.com/api/json/v1/1/random.php")
    #https://www.thecocktaildb.com/api/json/v1/1/search.php?i=vodka
    #www.thecocktaildb.com/api/json/v1/1/random.php
    drink = response.json()
    dic={}
    dic = {"Drink selected":drink['drinks'][0]['strDrink'],
           "Glass":drink['drinks'][0]['strGlass'],
           "Instructions":drink['drinks'][0]['strInstructions']
    }
    print(drink['drinks'][0])
    print("Drink selected: "+drink['drinks'][0]['strDrink']+"\nGlass: "+drink['drinks'][0]['strGlass']+"Instructions: "+drink['drinks'][0]['strInstructions'])
    # text_format = f'''Drink selected: {dic["Drink selected"]}
    #                   Glass: {dic["Glass"]}
    #                   Instructions: \n{dic["Instructions"]}'''
    d_glass =f"Glass: \n{drink['drinks'][0]['strGlass']}"
    d_selected = f"Drink selected: \n{drink['drinks'][0]['strDrink']} "

    d_Text = f"Instructions: \n{drink['drinks'][0]['strInstructions']}"
    
    drinks_text.config(text= d_Text)
    drink_glass.config(text=d_glass)
    drink_selected.config(text= d_selected)
    # canvas.itemconfig(drinks_text, text=dic)
    return dic
window = Tk()
window.title('Random dink selector')
window.config(padx=100,pady=100,bg=("#B1DDC6"))

# canvas = Canvas(width=300,height=300)
# canvas.create_text(150,150,text='DRINK', font=('Arial', 60, 'bold'))
# canvas.create_text(150,150,text='', font=('Arial', 60, 'normal'))
drinks = Label(text= "DRINK", font=('Arial', 60, 'normal'),bg=("#B1DDC6"),padx=50,pady=50)
drinks.grid(column=1,row=0)
drink_selected= Label(text= "Drink selected: ", font=('Arial', 10, 'normal'),bg=("#B1DDC6"),padx=5,pady=5)
drink_selected.grid(column=1, row=1)
drink_glass=  Label(text= "Glass: ", font=('Arial', 10, 'normal'),bg=("#B1DDC6"),padx=5,pady=5)
drink_glass.grid(column=1, row=2)
drinks_text = Label(text= "Instructions: ", font=('Arial', 10, 'normal'),bg=("#B1DDC6"),padx=5,pady=5)
drinks_text.grid(row=3,column=0,columnspan=2)
selector = Button(text="Select drink" ,command=slamano,padx=5,pady=5)
selector.grid(column=1,row=4)




window.mainloop()