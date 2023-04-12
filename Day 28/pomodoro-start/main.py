from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100,pady=100,bg = YELLOW)
canvas = Canvas(width=200,height=224,bg = YELLOW, highlightthickness= 0)
tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(100,112, image= tomato_image )
canvas.create_text(102,130,text='00:00',fill='white', font=(FONT_NAME, 35,'bold'))
canvas.pack()

#label timer
canvas.create_text(102,250,text='Timer',fill='green', font=(FONT_NAME, 35,'bold'))

# timer.grid(column=1,row=0)
#button start
button_start = Button(text='Start')
#button reset
button_reset = Button(text='Reset')
#label check


window.mainloop()