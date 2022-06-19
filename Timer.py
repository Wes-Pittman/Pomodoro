# Python program to illustrate a Pomodoro Timer with built-in intervals and sounds
import tkinter as tk

# Workspace / Main Window
ws = tk.Tk()
ws.title("Pomodoro Timer")
label = tk.Label(ws, text="Select Intervals")
label.pack()

# Dimensions
ws.minsize(width=300, height=120)

# Running
ws.mainloop()
