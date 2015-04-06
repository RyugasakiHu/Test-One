'http://www.codeskulptor.org/#user39_rWICaFpGQ1_0.py'
import simplegui

A=0
BC=0
D=0
X=0
Y=0
panel=0
input = 0
interval = 100
def tiktok():
    global input
    input = input + 1
    
#def show format 
def format(input):
    #clear global variable
    global A,BC,D
    #convert value
    time_display = str(A) + ':' + '0' + str(BC) + '.' + str(D)
    time_displays = str(A) + ':' + str(BC) + '.' + str(D)
    #return discuss
    if input/600 > 0:
        A = input/600
        BC = (input-600*A)/10
        if BC < 10:
            D = input-600*A-10*BC
            return time_display
        else :
            BC=BC 
            return time_displays
    else :
        A = 0
        BC = input
        if BC < 100:	
            BC = BC / 10
            D = input - BC*10
            return time_display
        else :
            BC = BC /10
            D = input - BC*10
            return time_displays
    
#def score
def score():
    return str(X) + "/" + str(Y) 
    
#def draw handle
def draw(canvas):
    canvas.draw_text(format(input),[100,100],24,'white')
    canvas.draw_text(score(),[250,20],24,'green')

def start():
    timer.start()

def stop():
    global X,Y,D
    if D%10==0:
        X=X+1
    else:
        Y=Y+1
    timer.stop() 

def reset():
    global input,X,Y
    input,X,Y = 0,0,0
    timer.stop()

frame = simplegui.create_frame('time',300,200)
#def event handlers for buttons'start' 'stop' 'reset'
frame.add_button('Start',start,200)
frame.add_button('Stop',stop,200)
frame.add_button('Reset',reset,200)
#register event handlers
timer = simplegui.create_timer(interval,tiktok)
timer = simplegui.create_timer(interval,tiktok)
frame.set_draw_handler(draw)
#2.555
frame.start()
