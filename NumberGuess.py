"""
This program rolls a pair of dice and asks the user to guess the sum. If the user,s guess is equal to the total value of the dice roll, the user will win
"""

from random import randint
#We use sleep to stop the program the seconds we put in the ()
from time import sleep

def get_user_guess():
  guess = int(raw_input("Guess the number:"))
  return guess

def roll_dice(number_of_sides):
  first_roll= randint(1,number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides*2
  print "The maximum possible value is: %d" % max_val
  guess= get_user_guess()
  if guess > max_val:
    print "No guessing higher than the maximun possible value! "
  else:
    print "Rolling....."
    sleep(2)
    print "The 1st roll is : %d" % first_roll
    sleep(1)
    print "The 2nd roll is: %d" % second_roll
    sleep(1)
    total_roll = first_roll + second_roll
    print total_roll
    print "Result...."
    sleep(1)
    if guess == total_roll:
      print "You win!!"
    else:
      print "You lost!"


#You must put a number as an argument inside the function , like the number of the sides
#We call the function to run the program
roll_dice(7)
