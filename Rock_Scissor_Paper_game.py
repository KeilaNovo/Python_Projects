"""
This program is Rock, Paper 
Scissor game
"""

from random import randint

options = ['ROCK','PAPER','SCISSOR']

message ={
  'tie':"Yawn it's a tie!",
"won":"Yay you won",
"lost":"Aww you lost!"
}

def decide_winner(user_choice, computer_choice):
  print "You selected: %s" % user_choice
  print  "The computer: %s" %computer_choice
  if user_choice == computer_choice:
    print message["tie"]
  elif user_choice == options[0] and computer_choice ==options[2]:
    print message["won"]
  elif user_choice == options[1] and computer_choice == options[2]:
    print message["lost"]
  elif user_choice == options[0] and computer_choice == options[1]:
    print message["lost"]
  else:
    print message["lost"]

def play_RPS():
  user_choice = raw_input("Enter Rock, Paper or Scissor: ")
  user_choice = user_choice.upper()
  computer_choice = options[randint(0,2)]
  decide_winner(user_choice, computer_choice)


play_RPS()
