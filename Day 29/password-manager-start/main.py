from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_entry.delete(0,END)
    letters_list = ['a','b', 'c','d','e','f','g','h','i','j','k','l','m','n', 'o', 'p', 'q','r', 's','t','u', 'v','w', 'x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    symbols_list = ['!','@','$','%','&','*','(',')']
    numbers = random.randint(3,4)
    symbol = random.randint(3,4)
    letters = random.randint(3,4)
    passw = [str(random.randint(0,10)) for number in range(numbers)]
    passw += [random.choice(symbols_list) for sym in range(symbol)]
    passw += [random.choice(letters_list) for letter in range(letters) ]
    
    random.shuffle(passw)
    password = ''.join(passw)

    password_entry.insert(0, password)
    pyperclip.copy(password)

# print(random.shuffle(password))
# ---------------------------- SAVE PASSWORD ------------------------------- #
def saveit():
    # email
    email_text = email.get()

    # site
    site = website.get()

    # password
    pass_text = password_entry.get()

    new_data = {
        site: {
            'email': email_text,
            'password': pass_text

        }
    }


    if len(site)<1 or len(pass_text)<1:
        messagebox.showinfo(title='Oops',message='Hey, you forgot to enter your infos')
    else:
        try:
            with open('./accounts_manager.json', mode='r') as file:

                #read old data
                data = json.load(file)


        except FileNotFoundError:
            with open('./accounts_manager.json', mode='w') as file:

                #save updated data
                json.dump(new_data,file, indent=4)
                #file.write(f'| {site} | {email_text} | {pass_text}| \n')

        else:
            # update old data
            new_data.update(data)
            with open('./accounts_manager.json', mode='w') as file:

                # save updated data
                json.dump(new_data, file, indent=4)
                # file.write(f'| {site} | {email_text} | {pass_text}| \n')
        finally:
            website.delete(0,END)
            password_entry.delete(0,END)

#--------------------------- Search password -------------------------- #

def search_pass():
    site = website.get()
    try:
        with open('./accounts_manager.json','r') as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='No data file found.')

    else:
        if site in data:
            messagebox.showinfo(title= site, message=f'Email:{data[site]["email"]}   \nPassword:{data[site]["password"]}')
        else:
            messagebox.showinfo(title= 'Error', message=f'No details for {site} in database.')
# ---------------------------- UI SETUP ------------------------------- #


#conifguring window
window = Tk()
# window.minsize(500,500)
window.config(padx=50,pady=50)
window.title('Password manager')

#putting image
canvas = Canvas(width=200, height=200)
locker_image = PhotoImage(file='./logo.png')
canvas.create_image(100,100, image= locker_image)
canvas.grid(column=1,row=0)

###Entries

#Entries
# entry = Entry(width=30)
# #Add some text to begin with
# entry.insert(END, string="Some text to begin with.")
# #Gets text in entry
# print(entry.get())
# entry.pack()



#########labels

#website
web_label = Label(text='Website:')
web_label.grid(row=1,column=0)

#email
email_label = Label(text= 'Email/Username:')
email_label.grid(row=2, column=0)

#password
pass_label = Label(text='Password:')
pass_label.grid(row=3,column=0)


#entries

##website
website = Entry(width=21)
website.grid(column=1,row=1,columnspan=2, sticky='w')
website.focus()

##Email
email = Entry(width=36)
email.grid(column=1,row=2,columnspan=2, sticky='w')
email.insert(END,'gabrieladealmeidajorge@hotmail.com')

##password

password_entry = Entry(width=21)
password_entry.grid(column=1,row=3,sticky='w')



######buttons

# ## button generate password
gen_password = Button(text='Generate Password',width=15,command=generate_password)
gen_password.grid(column=2,row=3,sticky='e')


# ##button apply

apply = Button(text='Add', width=36, command=saveit)
apply.grid(column=1,row=4, columnspan=2)

## search button
search = Button(text='Search',width=15, command=search_pass)
search.grid(row=1, column=2)
# #password.get()
# #email.get()
# #website.get()





window.mainloop()