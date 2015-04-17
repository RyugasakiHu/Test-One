#http://www.codeskulptor.org/#user39_At2zZDku5g_0.py
# Examples of mouse input

import simplegui
import math

# intialize globals
WIDTH = 450
HEIGHT = 300
ball_list = []
br = 15
ball = []

# helper function
def dis(p, q):
    return math.sqrt( (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

# define event handler for mouse click, draw
def click(pos):
    global ball
    change = False
    for ball in ball_list:
        if dis([ball[0],ball[1]],pos) < br:
            ball[2] = 'Green'
            change = True
            print ball
    if not change:
        ball_list.append([pos[0],pos[1],'Red'])
        print ball

def draw(canvas):
    for ball in ball_list:
        canvas.draw_circle([ball[0], ball[1]], br,1, "Black", ball[2])

# create frame
frame = simplegui.create_frame("Mouse selection", WIDTH, HEIGHT)
frame.set_canvas_background("White")

# register event handler
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# start frame
frame.start()
#####################
#RRRRRRRRemove
#http://www.codeskulptor.org/#user39_At2zZDku5g_1.py
# Examples of mouse input

import simplegui
import math

# intialize globals
WIDTH = 450
HEIGHT = 300
ball_list = []
br = 15
ball = []
bc = 'red'

# helper function
def dis(p, q):
    return math.sqrt( (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

# define event handler for mouse click, draw
def click(pos):
    global ball
    remove = []
    for ball in ball_list:
        if dis(ball,pos) < br:
            remove.append(ball)
            print ball
    if remove == []:
        ball_list.append(pos)
    else :
        for ball in remove:
            ball_list.pop(ball_list.index(ball))            

def draw(canvas):
    for ball in ball_list:
        canvas.draw_circle([ball[0], ball[1]], br,1, "Black",'Red')

# create frame
frame = simplegui.create_frame("Mouse selection", WIDTH, HEIGHT)
frame.set_canvas_background("White")

# register event handler
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# start frame
frame.start()
    
