from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#4E3636"
RED = "#e7305b"
GREEN = "#321E1E"
BACKCOLOR = "#116D6E"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_label.config(text="")
    global reps
    reps = 0




# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)

    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    ### this part of code fix seconds from 00:0 to 00:00
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text,  text=f"{count_min}:{count_sec}")
    print(count)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        ## each time when we done one work session create a checklabel
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_label.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=BACKCOLOR)


timer_label = Label(text="Timer", fg=GREEN, bg=BACKCOLOR, font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=1, row=0)


canvas = Canvas(width=200, height=223, bg=BACKCOLOR, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 111, image=tomato_img)


timer_text = canvas.create_text(100, 130, text="00:00", fill="#321E1E", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)


# check_text = "✔"
check_label = Label(fg=GREEN, bg=BACKCOLOR, font=(FONT_NAME, 15))
check_label.grid(column=1, row=4)


start_button = Button(text="Start", command=start_timer, fg="black", bg="#DC5F00")
start_button.grid(column=0, row=3)


reset_button = Button(text="Reset", command=reset_timer, fg="black", bg="#DC5F00")
reset_button.grid(column=3, row=3)





window.mainloop()
