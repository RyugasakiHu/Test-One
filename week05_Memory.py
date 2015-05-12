#http://www.codeskulptor.org/#user39_A7ClIfU8Xa_1.py
#draw work(basic ui)
#draw flip (interactive UI)
#record mouse input???
#flip twice (set list for expose)
#set random(random_list)
#compare memory 
import simplegui
import random

def new_game():
    global state,flipOne,flipTwo,moves,flip,num,moves
    state,flipOne,flipTwo = 0,0,0
    moves = 0
    flip = [False]*16
    num = [i for i in range(8)]*2
    random.shuffle(num)
    print num

def buttonclick(pos):
    global state,memory,flip,flipOne,flipTwo,moves
    memory = (pos[0]//40)
    if state == 0:
        state = 1
        flipOne = memory
        flip[memory] = True
    elif state == 1:
        state = 2
        flipTwo = memory
        flip[memory] = True
        if num[flipOne] == num[flipTwo]:
            moves += 1  
#        label.set_text("Moves = " + str(moves))    
        print moves   
    else:
        state = 1
    
def draw(canvas):  
    for n in range(16):
        if flip[n]:            
            canvas.draw_polygon([[(n)*40, 0],[(n)*40, 80],[40*(n+1), 80],[40*(n+1), 0]], 1, 'Black', 'black')
            canvas.draw_text(str(num[n]), [(n+1)*40-30, 55], 40, 'white')
        else:    
            canvas.draw_polygon([[(n)*40, 0],[(n)*40, 80],[40*(n+1), 80],[40*(n+1), 0]], 1, 'Black', 'green')
    
frame = simplegui.create_frame('Testing', 640, 80)
frame.add_button('Restart',new_game,200)
#label = frame.add_label('Moves = ' + str(moves))

#register event handlers
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(buttonclick)

#Get Rolling
new_game()
frame.start()
