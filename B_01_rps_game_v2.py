from typing import Any

import random

# Check that users have entered a valid
# option based on a list


def string_checker(question, valid_ans=("yes", "no")):
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it's a lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # Check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if the user does not enter something that is valid
        print(error)
        print()


# displays instructions
def instruction():
    print('''

**** Instructions ****

To begin, choose the number of rounds you would like to play. 
(Or choose infinite mode)

Then play against a computer. you need to choose if you want to
use rock, paper, or scissors.

The rules are:
- paper beats rock
- rock beats scissors
- scissors beat paper

press <xxx> to end the game at any time.

good luck!

    ''')


# Check that users have entered a valid
# option based on a list
def int_check(question):

    while True:

        error = "Please enter an integer that is 1 or more"

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # checks that the number is more than / equal to 1
            if response < 1:
                print(error)

            else:
                return response

        except ValueError:
            print(error)


# compares user / computer choice and returns
# result (win / lose / tie)
def rps_compare(user, comp):

    # if the user and the computer choice is the same, it's a tie
    if user == comp:
        round_result = "tie"

    # There are three ways to win
    elif user == "paper" and comp == "rock":
        round_result = "win"
    elif user == "scissors" and comp == "paper":
        round_result = "win"
    elif user == "rock" and comp == "scissors":
        round_result = "win"

    # if it's not a win / tie, then it's a loss
    else:
        round_result = "lose"

    return round_result


# Main routine starts here


# Initialise game variables
mode = "regular"
rounds_played = 0
rounds_tied = 0
rounds_lost = 0

rps_list = ["rock", "paper", "scissors", "xxx"]
game_history = []

print("📰✂💎 Paper / Scissors / Rock 💎✂📰")
print()

# ask user if they want to see the instructions and display
# them if required
want_instructions = string_checker("Would you like to read the instructions? ")

# Checks users enter yes(y) or no (n)
if want_instructions == "yes":
    instruction()

# ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings
    if mode == "infinite":
        rounds_heading = f"\nRound {rounds_played + 1} (Infinite Mode)"
    else:
        rounds_heading = f"\nRound {rounds_played + 1} of {num_rounds}"

    print(rounds_heading)

    # randomly choose from the rps list (excluding the exit code)
    comp_choice = random.choice(rps_list[:-1])
    print("Computer choice", comp_choice)

    user_choice = string_checker("Choose: ", rps_list)
    print("you chose", user_choice)

    # allows you to end the game for infinite mode
    if user_choice == "xxx":
        break

    result = rps_compare(user_choice, comp_choice)

    # Adjust game lost / game tied counters and add results to game history
    if result == "tie":
        rounds_tied += 1
        feedback = "👔 It's a tie! 👔"
    elif result == "lose":
        rounds_lost += 1
        feedback = "😢😢 You lose 😢😢"
    else:
        feedback = "👍👍 You won! 👍👍"

    # set up round feedback and output it user.
    # add it to the game history list (include the round number)
    round_feedback = f"{user_choice} vs {comp_choice}, {feedback}"
    history_item = f"Round: {rounds_played + 1} - {round_feedback}"

    print(round_feedback)
    game_history.append(history_item)

    rounds_played += 1

    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1


# Game loop ends here

# Game history / Statistics area

if rounds_played > 0:
    # calculate statistics
    rounds_won = rounds_played - rounds_tied - rounds_lost
    percent_won = rounds_won / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100
    percent_tied = 100 - percent_won - percent_lost

    # output game statistics
    print("\n📊 GAME STATISTICS 📊")
    print(f"👍 Won: {percent_won:.2f} \t")
    print(f"😢 Lost: {percent_lost:.2f} \t")
    print(f" Tied: {percent_tied:.2f}")

    # Display game history if user want to see it
    show_history = string_checker("\nDo you want to see the game history? ")
    if show_history == "yes":
        print("\n⌛ Game History ⌛")

        for item in game_history:
            print(item)

    print()
    print("Thanks for playing!")

else:
    print("🐔 Youuuuuu chicken... 🐔")
