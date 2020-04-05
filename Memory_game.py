# implementation of card game - Memory

import simplegui
import random

a = range(1,9)
b = range(1,9)
a.extend(b)

i = range(0,16)
my_nums = a
random.shuffle(my_nums)

exposed = [False] * 16

state = 0
card1 = None
card2 = None
counter = 0

# helper function to initialize globals
def new_game():
    global exposed, state, counter
    
    state = 0 
    counter = 0
    random.shuffle(my_nums)
    label.set_text('Turns = ' + str(counter))
    exposed = [False] * 16
    
        
# define event handlers
def mouseclick(pos):
    # add game state logic here
    
    global state, card1, card2, counter 
        
    list(pos)
    
    if exposed[pos[0] // 50] == False:
        exposed[pos[0]//50] = True
        if state == 0:
            state = 1
            card1 = i[pos[0]//50]
        elif state == 1:
            state = 2
            card2 = i[pos[0]//50]
            counter += 1
            label.set_text('Turns = ' + str(counter))
        else:
            state = 1
            if my_nums[card2] == my_nums[card1]:
                exposed[card1] = True
                exposed[card2] = True
            else:
                exposed[card1] = False
                exposed[card2] = False
            card1 = i[pos[0]//50]

            
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for indx in i:
        if exposed[indx]:
            canvas.draw_text(str(my_nums[indx]), (15 + 50*i[indx], 65), 40, "white")
        else:
            canvas.draw_polygon([[50*indx, 1], [50*indx, 100], [50*indx +50,100], [50*indx +50, 1]], 2, 'black', 'green')


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = " +str(counter))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)


# get things rolling
new_game()
frame.start()
