from itertools import count
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#f0583f"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
CHECK = "✔"
off = TRUE
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text="00:00", font=(FONT_NAME, 35, "bold"))
    check.config(text="")
    global off
    off = TRUE


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global off
    off = FALSE
    reps += 1
    if reps == 8:
        count_down(LONG_BREAK_MIN * 60)
    elif reps > 8:
        reps = 0
        canvas.itemconfig(timer_text, text="Complete\nclick Reset", font=(FONT_NAME, 18, "bold"))
    elif reps % 2 == 1:
        check.config(text=(CHECK * (int(reps / 2)+1)))
        count_down(WORK_MIN * 60)
    else:
        count_down(SHORT_BREAK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    seconds = count % 60
    minutes = int(count/60)
    if not off:
        # dynamic typing example
        #if seconds < 10:
        #    seconds = f"0{seconds}"
        if seconds < 10:
            canvas.itemconfig(timer_text, text=f"{minutes}:0{seconds}")
        else:
            canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
        if count > 0:
            window.after(1000, count_down, count - 1)
        else:
            start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

label = Label(text="Timer", font=(FONT_NAME, 48, "bold"), pady=10, bg=YELLOW, fg=RED)
label.grid(column=1, row=0)

start = Button(text="Start", font=(FONT_NAME, 18, "bold"), padx=10, pady=10, fg=GREEN, command=start_timer)
start.grid(column=0, row=3)


reset = Button(text="Reset", font=(FONT_NAME, 18, "bold"), padx=10, pady=10, fg=PINK, command=reset_timer)
reset.grid(column=2, row=3)

check = Label(text="", font=(FONT_NAME, 35, "bold"), padx=10, pady=15, bg=YELLOW, fg=GREEN)
check.grid(column=1, row=2)



window.mainloop()