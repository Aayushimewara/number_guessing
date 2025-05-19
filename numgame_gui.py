import tkinter as tk
from tkinter import messagebox
from num_guess import PlayerGuessesGame, ComputerGuessesGame

root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x400")

player_game = None
computer_game = None
player_name = ""    	

# --- Name Entry Frame ---
name_frame = tk.Frame(root)
name_frame.pack(pady=10)

tk.Label(name_frame, text="Enter your name:").pack()
name_entry = tk.Entry(name_frame)
name_entry.pack()

def submit_name():
    global player_name
    player_name = name_entry.get()
    if player_name:
        messagebox.showinfo("Welcome", f"Welcome {player_name}!")
        mode_frame.pack()
        name_frame.pack_forget()
    else:
        messagebox.showwarning("Missing Name", "Please enter your name.")

tk.Button(name_frame, text="Submit Name", command=submit_name).pack(pady=5)

# --- Mode Selection Frame ---
mode_frame = tk.Frame(root)

tk.Label(mode_frame, text="Choose Game Mode").pack()

def start_player_mode():
    global player_game
    player_game = PlayerGuessesGame(player_name)
    guess_frame.pack()
    comp_frame.pack_forget()

def start_computer_mode():
    global computer_game
    computer_game = ComputerGuessesGame()
    comp_frame.pack()
    guess_frame.pack_forget()

tk.Button(mode_frame, text="Player Guesses", command=start_player_mode).pack(pady=5)
tk.Button(mode_frame, text="Computer Guesses", command=start_computer_mode).pack(pady=5)

# --- Player Guess Frame ---
guess_frame = tk.Frame(root)

tk.Label(guess_frame, text="Enter your guess:").pack()
guess_entry = tk.Entry(guess_frame)
guess_entry.pack()

guess_result = tk.Label(guess_frame, text="")
guess_result.pack()

def submit_player_guess():
    try:
        guess = int(guess_entry.get())
        result = player_game.make_guess(guess)
        guess_result.config(text=result)
        if result == "Correct!":
            summary = player_game.get_summary()
            messagebox.showinfo("Game Over", f"You won in {summary['attempts']} attempts!\nGuesses: {summary['guesses']}")
            guess_frame.pack_forget()
    except ValueError:
        guess_result.config(text="Please enter a valid number.")

tk.Button(guess_frame, text="Submit Guess", command=submit_player_guess).pack(pady=5)

def undo_guess():
    if player_game:
        message = player_game.undo_last_guess()
        guess_result.config(text=message)

tk.Button(guess_frame, text="Undo Last Guess", command=undo_guess).pack(pady=5)

# --- Computer Guess Frame ---
comp_frame = tk.Frame(root)

computer_guess_label = tk.Label(comp_frame, text="Think of a number between 1 and 100. I will try to guess it!")
computer_guess_label.pack(pady=10)

computer_feedback_label = tk.Label(comp_frame, text="")
computer_feedback_label.pack()

def computer_guess():
    guess = computer_game.next_guess()
    if guess is not None:
        guessing_button.pack_forget()
        computer_guess_label.config(text=f"My guess is: {guess}")
        computer_feedback_label.config(text="Choose: Too Low, Too High, or Correct")
    else:
        computer_guess_label.config(text="I couldn't guess it!")
        computer_feedback_label.config(text="")

guessing_button= tk.Button(comp_frame, text="Start Guessing", command=computer_guess)
guessing_button.pack(pady=5)

def feedback_response(feedback):
    if feedback == "correct":
        messagebox.showinfo("Game Over", f"I guessed your number in {computer_game.attempts} tries!")
        comp_frame.pack_forget()
    else:
        computer_game.update_feedback(feedback)
        computer_guess()

tk.Button(comp_frame, text="Too Low", command=lambda: feedback_response("low")).pack()
tk.Button(comp_frame, text="Too High", command=lambda: feedback_response("high")).pack()
tk.Button(comp_frame, text="Correct", command=lambda: feedback_response("correct")).pack()

root.mainloop()
