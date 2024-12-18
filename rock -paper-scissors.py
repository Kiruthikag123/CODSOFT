import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'scissors' and computer_choice == 'paper') or \
       (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    return "You lose!"

def play_game():
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        while user_choice not in ['rock', 'paper', 'scissors']:
            user_choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        print(f"Result: {result}\n")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        while play_again not in ['yes', 'no']:
            play_again = input("Invalid input. Please enter yes or no: ").lower()
        if play_again == 'no':
            break

play_game()
