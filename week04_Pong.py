#http://www.codeskulptor.org/#user39_mGoLDP1pHg_4.py
import simplegui
import random
import math
#initialize globals
w = 600
h = 400
br = 15
pad_w = 8
pad_h = 80
half_pad_w = pad_w/2
half_pad_h = pad_h/2
left = False
right = True
ball_pos = [w/2,h/2]
ball_vel = [1,1]
A = [0,h/2 - half_pad_h]
B = [0,h/2 + half_pad_h]
C = [pad_w,h/2 + half_pad_h]
D = [pad_w,h/2 - half_pad_h]
paddle1_pos = A,B,C,D
E = [w - pad_w,h/2 - pad_h/2]
F = [w - pad_w,h/2 + pad_h/2]
G = [w,h/2 + pad_h /2]
H = [w,h/2 - pad_h/2]
paddle2_pos = E,F,G,H
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0
N = 0
#initialize ball_pos and ball_vel for new bal in middle of table
#if direction is right so was the ball`s velocity,else left
def spawn_ball():
    global ball_pos,ball_vel,N
    global paddle1_pos,paddle2_pos
    global A,B,C,D,E,F,G,H
    N = 0
    ball_vel = [1,1]
    ball_pos = [w/2,h/2]
    A = [0,160]
    B = [0,240]
    C = [8,240]
    D = [8,160]
    paddle1_pos = A,B,C,D
    E = [592,160]
    F = [592,240]
    G = [600,240]
    H = [600,160]
    paddle2_pos = E,F,G,H
#define event handlers    
def new_game():
    global score1,score2
    score1 = 0
    score2 = 0
    return spawn_ball()

def draw(c):
    global score1,score2,ball_pos,paddle1_vel,paddle2_vel
    N = 0
    #draw mid line and gutters
    c.draw_line([w/2,0],[w/2,h],1,'White')
    c.draw_line([pad_w,0],[pad_w,h],1,'White')
    c.draw_line([w-pad_w,0],[w-pad_w,h],1,'White')
    c.draw_text(str(score1),[150,60],48,'White')
    c.draw_text(str(score2),[450,60],48,'White')
    #update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    #draw ball
    c.draw_circle(ball_pos,br,2,'White','White')
    #update paddle`s velical position,keep paddle on the screen
    #keep paddle1 on the screen
    A[1] += paddle1_vel
    B[1] += paddle1_vel
    C[1] += paddle1_vel
    D[1] += paddle1_vel
    
    if B[1] >= h :
        A[1] = h - pad_h
        D[1] = h - pad_h
        B[1] = h 
        C[1] = h 
    elif A[1] <= 0 :
        A[1] = 0
        D[1] = 0 
        B[1] = pad_h
        C[1] = pad_h 
        
    #keep paddle2 on the screen
    E[1] += paddle2_vel
    F[1] += paddle2_vel
    G[1] += paddle2_vel
    H[1] += paddle2_vel
    
    if G[1] >= h :
        E[1] = h - pad_h
        H[1] = h - pad_h
        G[1] = h 
        F[1] = h 
    elif E[1] <= 0 :
        E[1] = 0
        H[1] = 0 
        G[1] = pad_h
        F[1] = pad_h 
    #draw paddles
    c.draw_polygon(paddle1_pos, 1, 'White','White')
    c.draw_polygon(paddle2_pos, 1, 'White','White')    
    #ball collision up down
    if ball_pos[1] - br <= 0:
        ball_vel[1] = math.pow(-1,N)*(math.fabs(ball_vel[1]) + 0.5)
    if ball_pos[1] + br >= h:
        ball_vel[1] = -math.pow(-1,N)*(math.fabs(ball_vel[1]) + 0.5)
    #ball collision left
    if ball_pos[0] <= br + pad_w:
        N += 1
        if D[1] <= ball_pos[1] <= C[1]:
            ball_vel[0] = -math.pow(-1,N)*(math.fabs(ball_vel[0]) + 1)
        else:    
            spawn_ball()
            score2 +=1
    #ball collision right        
    if ball_pos[0] + br >= w - pad_w:
        N += 1
        if E[1] <= ball_pos[1] <= F[1]:
            ball_vel[0] = math.pow(-1,N)*(math.fabs(ball_vel[0]) + 1)
        else:    
            spawn_ball()
            score1 +=1
    
def keydown(key):
    global paddle1_vel,paddle2_vel
    #paddle1 move
    if key==simplegui.KEY_MAP['w']:
        paddle1_vel -= 6
    elif key==simplegui.KEY_MAP['s']:
        paddle1_vel += 6
    #paddle2 move
    if key==simplegui.KEY_MAP['up']:
        paddle2_vel -= 6
    elif key==simplegui.KEY_MAP['down']:
        paddle2_vel += 6    
 
def keyup(key):
    global paddle1_vel,paddle2_vel
    #paddle1 stop
    if key==simplegui.KEY_MAP['w']:
        paddle1_vel =0
    elif key==simplegui.KEY_MAP['s']:
        paddle1_vel =0
    #paddle2 stop
    if key==simplegui.KEY_MAP['up']:
        paddle2_vel = 0
    elif key==simplegui.KEY_MAP['down']:
        paddle2_vel = 0    

#create frame
frame = simplegui.create_frame('Pong',w,h)
frame.add_button('Restart',new_game,200)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

#start frame
new_game()
frame.start()
