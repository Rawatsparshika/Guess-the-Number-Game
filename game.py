import random

def guess_the_number():
    print("Welcome to Guess the Number!")
    print("I am thinking of a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    number_of_attempts = 0
    guessed_correctly = False
    
    while not guessed_correctly:
        # Get user input
        try:
            user_guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        number_of_attempts += 1
        
        # Check if the guess is correct, too high, or too low
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed_correctly = True
            print(f"Congratulations! You guessed the number in {number_of_attempts} attempts.")

def main():
    while True:
        guess_the_number()
        
        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
