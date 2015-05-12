#http://www.codeskulptor.org/#user40_arFxNIlWNu_3.py
#draw basic ui(size)
#draw flip (interactive UI,draw number)
#record mouse input???
#flip (set list for expose)
#set random(random_list)
#flip twice(interactive with mouse input)
#compare memory 
#unflip function
#streamline
import simplegui
import random

def new_game():
    global state,flipOne,flipTwo,moves,flip,num,turns
    state,flipOne,flipTwo = 0,0,0
    turns = 0
    flip = [False]*16
    num = [i for i in range(8)]*2
    random.shuffle(num)
    label.set_text("Turns = " + str(turns))
    print num

def buttonclick(pos):
    global state,memory,flip,flipOne,flipTwo,turns
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
            turns += 1  
        label.set_text("Turns = " + str(turns))    
        print turns   
    else:
        if num[flipOne] != num[flipTwo]:
            flip[flipOne],flip[flipTwo] = False,False
        flipOne = memory
        flip[memory] = True    
        turns += 1 
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
label = frame.add_label('Turns =')

#register event handlers
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(buttonclick)

#Get Rolling
new_game()
frame.start()
