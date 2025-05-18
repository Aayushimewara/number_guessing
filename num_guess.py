import random

class PlayerGuessesGame:
    def __init__(self, player_name):
        self.player_name = player_name
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.guess_history = []

    def make_guess(self, guess):
        self.guess_history.append(guess)
        self.attempts += 1
        if guess < self.number_to_guess:
            return "Too low!"
        elif guess > self.number_to_guess:
            return "Too high!"
        else:
            return "Correct!"

    def undo_last_guess(self):
        if self.guess_history:
            removed = self.guess_history.pop()
            self.attempts -= 1
            return f"Removed guess: {removed}"
        return "Nothing to undo."

    def get_summary(self):
        return {
            "name": self.player_name,
            "attempts": self.attempts,
            "guesses": self.guess_history
        }

class ComputerGuessesGame:
    def __init__(self):
        self.low = 1
        self.high = 100
        self.attempts = 0
        self.current_guess = None

    def next_guess(self):
        if self.low > self.high:
            return None
        self.current_guess = (self.low + self.high) // 2
        self.attempts += 1
        return self.current_guess

    def update_feedback(self, feedback):
        if feedback == "low":
            self.low = self.current_guess + 1
        elif feedback == "high":
            self.high = self.current_guess - 1
