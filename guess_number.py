# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import math
import random
import simplegui

num_range = 100
count = 0
stop = 7


# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
  
    global secret_number
    global count
    count =0 
    secret_number = random.randrange(num_range)
    print "New Game! Guess a number!"
    print ""

# define event handlers for control panel
def range100():
    global num_range
    global stop
    global count
    num_range = 100
    stop = 7
    print ""
    new_game()

def range1000():
    global num_range
    global stop
    global count
    num_range = 1000
    stop = 10
    print ""
    new_game()
    
    
def input_guess(guess):
    print ""
    print "Guess was " + guess
    
    global count
    count +=1 
    
    if  int(guess) == secret_number:
        print "You guessed right!!!"
        print ""
        new_game()  
    elif count == stop:
        print("GAME OVER! You ran out of guesses")
        print ""
        new_game()
    elif int(guess) > secret_number:
        print "Lower!"
        print ("You have " +str(stop - count) + " guesses left")
    else: 
        print "Higher!"
        print ("You have " +str(stop - count) + " guesses left")
    
    
   
    
  
    
# create frame
f = simplegui.create_frame("GUESSER", 200,200)
f.add_input("Your Guess (Press Enter)", input_guess, 200)
blank = f.add_label('')
label1 = f.add_label('New Game: Change range')
f.add_button("Number (0,100)",range100, 200)
f.add_button("Number (0,1000)", range1000, 200)

# register event handlers for control elements and start frame


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
