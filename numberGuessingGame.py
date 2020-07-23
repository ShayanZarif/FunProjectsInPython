from random import randint as ri
from time import sleep as s
def get_user_guess():
  aguess = int(raw_input("Guess a number: "))
  return aguess
def roll_dice(number_of_sides):
  first_roll = ri(1,number_of_sides)
  second_roll = ri(1,number_of_sides)
  max_val = number_of_sides * 2
  print("The maximum possible value is %d"%( max_val))
  guess = get_user_guess()
  if guess > max_val:
    print("Invalid Guess.Exceeded max value.")
  else:
    print("Rolling...")
    s(2)
    print("Your First roll is: %d" %(first_roll))
    print("Your Second roll is: %d" %(second_roll))
    s(1)
    total_roll = first_roll + second_roll
    print("Total Roll: %d" %(total_roll))
    s(2)
    if guess == total_roll:
      print("You Won!!")
    else:
      print("You lost.")
roll_dice(6)   
