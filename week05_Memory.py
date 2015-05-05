#http://www.codeskulptor.org/#user39_Gv7hj1lOdi_2.py
#draw work
#draw flip 
import simplegui
memory = []
memory_list = []
index = 0
def new_game():
    global state
    state = 0

def buttonclick(pos):
    global state    
    index = (pos[0]//40)+2
    print index
    if state == 0:
        state = 1
    elif state == 1:
        state = 2
    else:
        state = 1
    
def draw(canvas): 
    global index
    for n in range(17):
        if n != index:
            canvas.draw_polygon([[(n-1)*40, 0],[(n-1)*40, 80],[40*n, 80],[40*n, 0]], 1, 'Black', 'green')                   
        elif n == index:    
            canvas.draw_text('B', [(n-1)*40-20, 20], 40, 'Blue')
frame = simplegui.create_frame('Testing', 640, 80)
frame.add_button('Restart',new_game,200)

#register event handlers
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(buttonclick)

#Get Rolling
new_game()
frame.start()
