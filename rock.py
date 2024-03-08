import random
def get_your_choice():
    while True:
        your_choice = input("Enter your choose[rock, paper, or scissor]:").lower()
        if your_choice in ["rock", "paper", "scissor"]:
            return your_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissor.")
def get_computer_choice():
    return random.choice(["rock", "paper", "scissor"])
def determine_winner(your_choice, computer_choice):
    if your_choice == computer_choice:
        return "It's a tie!"
    elif (
        (your_choice == "rock" and computer_choice == "scissor") or
        (your_choice == "scissor" and computer_choice == "paper") or
        (your_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"
def play_game():
    your_score = 0
    computer_score = 0
    while True:
        your_choice = get_your_choice()
        computer_choice = get_computer_choice()
        print(f"You have choosen: {your_choice}")
        print(f"Computer chosen: {computer_choice}")
        result = determine_winner(your_choice, computer_choice)
        print(result)
        if result == "You win!":
            your_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        print(f"Your score: {your_score}")
        print(f"Computer's score: {computer_score}")
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            if(your_score > computer_score):
                print("you won the game")
            elif(your_score < computer_score):
                print("you lost the game")
            else:
                print("the game is tied")
            break
if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissor game!")
    play_game()
    print("Thank you so much for playing!")