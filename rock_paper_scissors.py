import random

def play():
    options = ['rock', 'paper', 'scissors']
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user = input("Choose rock, paper, or scissors (or 'quit' to exit): ").lower()
        if user == 'quit':
            print("Thanks for playing!")
            break
        if user not in options:
            print("Invalid choice. Try again.")
            continue
        computer = random.choice(options)
        print(f"Computer chose: {computer}")
        if user == computer:
            print("It's a tie!")
        elif (user == 'rock' and computer == 'scissors') or \
             (user == 'paper' and computer == 'rock') or \
             (user == 'scissors' and computer == 'paper'):
            print("You win!")
        else:
            print("You lose!")

if __name__ == "__main__":
    play()
