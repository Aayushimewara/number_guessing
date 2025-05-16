import random
def number_guessing_game():
    player_name = input("Enter your name: ")
    number_to_guess = random.randint(1, 100)  # Random number between 1 and 100
    guess = None  # Initialize guess variable
    attempts = 0  # Count attempts
    guess_history = [] #list
    print(f"Welcome to the Number Guessing Game {player_name}!")
    while guess != number_to_guess:
        guess = int(input("Enter your guess (between 1 and 100): "))
        undo = input("Type 'undo' to remove your last guess, or press Enter to continue: ")
        if undo.lower() == 'undo' and guess_history:
         removed = guess_history.pop()
         attempts -= 1
         print(f"Last guess {removed} removed. Try again.")
         continue

        guess_history.append(guess)
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
         #  print(f"Correct! You guessed the number in {attempts} attempts.")
            player_stats = {
                "name": player_name,
                "attempts": attempts,
                "result": "Win"
            }
            print("\nGame Summary:")
            for key, value in player_stats.items():
                print(f"{key.capitalize()}: {value}")


            print("Your guesses were:", guess_history)

def computer_guesses():
    print("Think of a number between 1 and 100. I will try to guess it!")
    input("Press Enter when you're ready...")
    low = 1
    high = 100
    attempts = 0
    while low <= high:
        guess = (low + high) // 2
        attempts += 1
        print(f"My guess is: {guess}")
    
        feedback = input("Is it 'correct', 'low', or 'high'? ").lower()

        if feedback == "correct":
           print(f"I guessed your number in {attempts} tries!")
           break
        elif feedback == "low":
           low = guess + 1
        elif feedback == "high":
           high = guess - 1
        else:
           print("Please enter 'correct', 'low', or 'high'.")
      
while True:
    mode = input("Choose mode: '1' for player guesses, '2' for computer guesses, 'q' to quit: ")

    if mode == '1':
        number_guessing_game()
    elif mode == '2':
        computer_guesses()
    elif mode.lower() == 'q':
        print("Thanks for playing!Goodbye.")
        break
    else:
        print("Invalid Mode Selected.")


