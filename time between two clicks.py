import simplegui 

total_ticks = 0
time = 0

# Timer handler
def tick():
    global time
    time = time+0.01
    
# Button handler
def click():
    global time
    global total_ticks
    if total_ticks%2 == 0:
        timer.start()
    else:
        timer.stop()
        print "The time was",str(time)+"."        
        time = 0
    total_ticks = total_ticks+1

# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
frame.add_button("Click me", click, 200)
timer = simplegui.create_timer(10, tick)

# Start timer
frame.start()
