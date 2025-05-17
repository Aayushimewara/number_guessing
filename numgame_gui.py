import tkinter as tk  #tkinter library tk for short
from tkinter import messagebox
root = tk.Tk() #store main window in root obj
root.title("Number Guessing Game")
root.geometry("300x200") #width and height
label = tk.Label(root,text="Choose Game Mode")
label.pack(pady=10)
player_button = tk.Button(root,text="Player Guesses")
player_button.pack(pady=5)
computer_button = tk.Button(root,text="Computer Guesses")
computer_button.pack(pady=5)
root.mainloop()


