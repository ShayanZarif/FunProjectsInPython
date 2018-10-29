""" 
This is a rock paper scissors game in python
"""
from random import randint as ri

options = ["ROCK", "PAPER", "SCISSORS"]
message = {
	"tie": "Yawn it's a tie!",
  "won": "Yay yoy won!",
  "lost": "Aww you lost!"
}
def decide_winner(user_choice,computer_choice):
  print("Your choice is " + user_choice)
  print("Computer's choice is " + computer_choice)
  if user_choice == computer_choice:
    print("%s",message["tie"])
  elif user_choice == options[0] and computer_choice == options[2]:
    print('%s'%(message['won']))
    
  elif user_choice == options[1] and computer_choice == options[0]:
	print('%s'%(message['won']))
    
  elif user_choice == options[2] and computer_choice == options[1]:
    print(message['won'])
  else:
    print(message['lost'])
    
def play_RPS():
  user_choice = raw_input("Enter Rock, Paper or Scissors: ").upper()
  computer_choice = options[ri(0,2)]         
  decide_winner(user_choice,computer_choice)                        
play_RPS()
                 
                          
                          