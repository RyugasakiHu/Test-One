#http://www.codeskulptor.org/#user39_A7ClIfU8Xa_0.py
#draw work
#draw flip 
#flip twice 
import simplegui
memory = []


memory_list = []
index = 0
first_card = [0,0]
sec_card = [0,0]


def new_game():
    global state,first_card,sec_card
    state = 0
    first_card = [0,0]
    sec_card = [0,0]

def buttonclick(pos):
    global state,memory,memory_list     
    memory = (pos[0]//40)+1
    if state == 0:
        state = 1
        memory_list.append(memory)
    elif state == 1:
        state = 2
    else:
        state = 1
    
def draw(canvas):  
    for n in range(17):
        if n != memory:            
            canvas.draw_polygon([[(n-1)*40, 0],[(n-1)*40, 80],[40*n, 80],[40*n, 0]], 1, 'Black', 'green')                   
        else:    
            canvas.draw_text('B', [(n)*40-30, 55], 40, 'white')
frame = simplegui.create_frame('Testing', 640, 80)
frame.add_button('Restart',new_game,200)

#register event handlers
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(buttonclick)

#Get Rolling
new_game()
frame.start()
