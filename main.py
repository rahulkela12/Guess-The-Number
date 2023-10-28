# import random
# print("Welcome To guess the Number")
# print("I'm Thinking of a number between 1 and 100.")
# difficulty = input("Choose The Difficulty.Type 'easy or 'hard'\n")
# comp_num = random.randint(1, 101)
# if difficulty == "easy":
#     chances = 10
# else:
#     chances = 5
# stop_loop = False
# while chances != 0 and stop_loop == False:
#     print(f"You Have {chances} attempts remaining to guess the number.")
#     user_choice =int(input("Make a Guess: "))
#     if user_choice == comp_num:
#         print(f"You got it.The answer is {user_choice}")
#         stop_loop = True
#     elif user_choice > comp_num:
#         print("Too High")
#     else:
#         print("Too Low")
#     chances -= 1
#     if chances == 0 and stop_loop == False:
#         print("You've have run out of guesses,you lose")
#     elif stop_loop == False:
#         print("Guess Again")
from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
#  print(f"Pssst, the correct answer is {answer}")

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()

