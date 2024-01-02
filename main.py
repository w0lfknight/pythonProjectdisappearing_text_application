from tkinter import Tk
import tkinter as tk
import time


window = Tk()
window.title("Text Disappearing Application")
window.minsize(500, 500)

counter = 5





def countdown():
    global counter
    while counter >= 0:
        timer = timer_label.config(text=str(counter))
        window.update()

        return counter
    window.after(1000, check_disappear)
    timer_label.config(text="time's up")


def disappear_text():
    textbox.delete("1.0", tk.END)
    textbox.insert(tk.END, "")


def check_disappear():
    global counter, text

    if text == textbox.get("1.0", tk.END):

        if countdown() == 2:
            textbox.tag_add(text, "1.0", tk.END)
            textbox.tag_config(text, foreground='red')

        elif countdown() == 0:

            window.after(1000, disappear_text)
            counter = -1
            text = "\n"

        window.after(1000, check_disappear)
        counter -= 1


    else:
        window.after(1000, check_disappear)
        text = textbox.get("1.0", tk.END)
        textbox.tag_add(text, "1.0", tk.END)
        textbox.tag_config(text, foreground='black')

        counter = 5


title = tk.Label(window, text="Welcome To The Text Disappearing Application", font=("Helventica", 18))
title.grid(row=0, column=1)

text = ''
textbox = tk.Text(height=25, width=55)
textbox.focus()
textbox.grid(row=3, column=1, padx=10, pady=10)

timer_label = tk.Label(window, text="00:00")
timer_label.grid(row=4, column=1)



window.after(1000, check_disappear)

window.mainloop()

