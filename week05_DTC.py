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
    
#http://www.codeskulptor.org/#user39_At2zZDku5g_2.py
def count_odd(numbers):
    count = 0
    for num in numbers:
        if num % 2 ==1:
            count += 1
    return count  

def check_odd(numbers):
    odd = False
    for num in numbers:
        if num % 2 == 1:
            odd = True
    return odd        
    
def remove_odd2(numbers):
    for num in numbers:
        if num % 2 == 1:
            numbers.remove(num)
            
def remove_odd3(numbers):
    remove = []
    for num in numbers:
        if num % 2 == 1:
            remove.append(num)
          
    for num in remove:
        numbers.remove(num)
def run():
    numbers = [1,2,3,4,5,6,7,11,22,33,44,55,7]
    print numbers
    remove_odd2(numbers)
    print numbers
    
run()    

#http://www.codeskulptor.org/#user39_pBOTunF5O3_0.py

import simplegui
import random

chipher = {}
message = ''
letters = 'abcdefghijklmnopqrstuvwxyz'

def init():
    letters_list = list(letters)
    random.shuffle(letters_list)
    for ch in letters:
        chipher[ch] = letters_list.pop()
    
def encode():
    emsg = ''
    for ch in message:
        emsg += chipher[ch]
    print message + " " + 'encodes to' + " " + emsg
        
def decode():
    dmsg = ''
    for ch in message:
        for key,value in chipher.items():
            if ch == value:
                dmsg += key
    print message + " " + 'encodes to' + " " + dmsg

def newmsg(msg):
    global message
    message = msg
    label.set_text(msg)
    return msg
    
frame = simplegui.create_frame('Cipher',2, 200, 200)     
frame.add_input('Message:',newmsg,200)
label = frame.add_label('',200)
frame.add_button('Encode',encode)
frame.add_button('Dncode',decode)

init()
frame.start()

#http://www.codeskulptor.org/#user39_pBOTunF5O3_1.py
import simplegui

image = simplegui.load_image('http://commondatastorage.googleapis.com/codeskulptor-assets/gutenberg.jpg')

map_w = 1521
map_h = 1818

scale = 3

can_w = map_w // scale
can_h = map_h // scale

mag_size = 120
mag_pos = [can_w//2,can_h//2]

def click(pos):
    global mag_pos
    mag_pos = list(pos)
    
def draw(canvas):
    canvas.draw_image(image,
                      [map_w//2,map_h//2],[map_w,map_h],
                      [can_w//2,can_h//2],[can_w,can_h])
    map_center = [scale * mag_pos[0],scale * mag_pos[1]]
    map_rectangle = [mag_size,mag_size]
    mag_center = mag_pos
    mag_rectangle = [mag_size,mag_size]
    canvas.draw_image(image,map_center,map_rectangle,mag_center,mag_rectangle)
    
frame = simplegui.create_frame('map',can_w,can_h)    
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)
frame.start()
