from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 * 60
SHORT_BREAK_MIN = 5 * 60
LONG_BREAK_MIN = 20 * 60
reps = 0
timer = None
mark = ''

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_Text, text = '00:00')
    timer_label.config(text='Timer',fg=GREEN)
    global reps
    reps = 0
    check_label.config(text='')

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps%2 !=0:
        #time to work
        # count_down(WORK_MIN)
        count_down(5)
        timer_label.config(text='Work',fg=GREEN)
    else:
        if reps == 8:
            # count_down(LONG_BREAK_MIN)
            count_down(10)
            timer_label.config(text='Break',fg=RED)
        else:
            # count_down(SHORT_BREAK_MIN)
            count_down(3)
            timer_label.config(text='Break',fg=PINK)
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}' 
    canvas.itemconfig(timer_Text, text = f'{count_min}:{count_sec}')
    if count > 0 :
        global timer
        timer = window.after(1000,count_down, count - 1)

    elif count == 0:
        global mark
        if reps%2 == 0:
            work_sessions = math.floor(reps/2)
            for _ in range(work_sessions):
                mark += '✔️'

                check_label.config(text=mark)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100,pady=100,bg = YELLOW)


# window.after(1000,say)

canvas = Canvas(width=200,height=224,bg = YELLOW, highlightthickness= 0)
tomato_image = PhotoImage(file='tomato.png')



#label timer
# canvas.create_text(102,250,text='Timer',fg=GREEN, font=(FONT_NAME, 35,'bold'))
timer_label = Label(text='Timer',bg=YELLOW , fg=GREEN, font=(FONT_NAME, 35,'bold'))
timer_label.pack(side='top')


#canvas
canvas.create_image(100,112, image= tomato_image )
timer_Text = canvas.create_text(102,130,text='00:00',fill='white', font=(FONT_NAME, 35,'bold'))
canvas.pack()


#button start

button_start = Button(text='Start', command= start_timer)
button_start.pack(side='left')

#button reset
button_reset = Button(text='Reset',command=reset_timer)
button_reset.pack(side='right')

#label check
check_label = Label(bg=YELLOW , fg=GREEN, text='')
check_label.pack(side='bottom')




window.mainloop()