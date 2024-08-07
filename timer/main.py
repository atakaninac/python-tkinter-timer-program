import tkinter as tk


#Get the User Input
def user_input():
    global user_min
    user_min = int(entry.get())
    canvas.itemconfig(timer_text, text=f"{user_min}:00")

#Timer Function
def timer(number):
    min = int(number / 60)
    sec = number % 60
    global countdown

    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if number > 0:
        countdown = window.after(1000, timer, number-1)
        
#Starting Timer
def start():
    timer(user_min*60)

#Reset
def reset():
    window.after_cancel(countdown)
    canvas.itemconfig(timer_text, text="00:00")

#Window
window = tk.Tk()
window.title("Timer")
window.config(padx=50, pady=25, bg="#E2DAD6")

#Canvas
canvas = tk.Canvas(height=440, width=600, bg="#E2DAD6", highlightthickness=0)
img = tk.PhotoImage(file="./file.png")
canvas.create_image(300, 220, image=img)
timer_text = canvas.create_text(300, 220, text="00:00", font=("Arial", 60, "bold"))

canvas.grid(row=1, column=1)

#Labels
label_text = tk.Label(text="Timer", font=("Arial", 50), bg="#E2DAD6", fg="#6482AD")

label_text.grid(row=0, column=1)

#Buttons
button1 = tk.Button(text="Start", height=5, width=12, command=start)
button2 = tk.Button(text="Reset", height=5, width=12, command=reset)
button3 = tk.Button(text="Enter Minutes", height=5, width=12, command=user_input)

button1.grid(row=2, column=0)
button2.grid(row=2, column=2)
button3.grid(row=1, column=0)


#Entry
entry = tk.Entry(width=5, font=("Arial", 25))

entry.grid(row=0, column=0)

#Keep the Program Running
window.mainloop()