
# pip install tk

from tkinter import Tk
from tkinter import Button

root = Tk()
root.geometry("200x200")
root.title("hi world")
btn = Button(text = "click me", background="blue")
btn.pack()

root.mainloop()