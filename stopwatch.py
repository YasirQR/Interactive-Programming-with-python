
import simplegui

# define global variables


counter = 0 
stops = 0
wins = 0
has_stopped = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D

def format(t):
    
    seconds = t / 10
    A = seconds // 60
    s1 = seconds % 60
    B = s1 // 10
    C = s1 % 10   
    D = t % 10
    
    return str(A) +":" + str(B) + str(C) + "." + str(D)

def victory():
    global wins
    if int(counter) % 50 == 0 and counter != 0:
        wins += 1


# define event handlers for buttons; "Start", "Stop", "Reset"

def start():
    global has_stopped
    timer.start()
    has_stopped = False
    
def stop():
    global stops
    global has_stopped
    timer.stop()
    
    if not has_stopped:
        stops += 1
        victory()
        has_stopped = True
    
def reset():
    timer.stop()
    global counter, wins, stops
    counter = 0
    wins = 0
    stops = 0


# define event handler for timer with 0.1 sec interval

def time_handler():
    global counter
    counter += 1
  
# define draw handler

def draw(canvas):
    canvas.draw_text(format(counter), (75, 120), 64, 'White')
    canvas.draw_text(str(wins) + "/" + str(stops), (240, 30), 30, 'White')

    
# create frame

frame = simplegui.create_frame("frame", 300,200)
timer = simplegui.create_timer(100, time_handler)
        
# register event handlers

frame.set_draw_handler(draw)
label0 = frame.add_label('Stop the timer at 5 seconds intervals!')
label1 = frame.add_label('')
button1 = frame.add_button('Start', start, 100)
label2 = frame.add_label('')
button2 = frame.add_button("Stop", stop, 100)
label3 = frame.add_label('')
button3 = frame.add_button("Reset", reset, 100)

# start frame
frame.start()
