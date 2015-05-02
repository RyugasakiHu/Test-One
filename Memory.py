#http://www.codeskulptor.org/#user39_Gv7hj1lOdi_0.py
import simplegui
n=0
memory = []
memory_list = []
poly = [[(n-1)*40, 0],[(n-1)*40, 80],[(n-1)*80, 80],[(n-1)*80, 0]]
#poly[0] = [(n-1)*40, 0] 
#poly[1] = [(n-1)*40, 80]
#poly[2] = [(n-1)*80, 80]
#poly[3] = [(n-1)*80, 0]
def new_game():
    global n,memory   
    if n < 8:
        n += 1
        for memory in memory_list:
            memory_list.append(poly)
    print n,memory_list

def draw(canvas): 
    for memory in memory_list:                  
        canvas.draw_polygon([poly[0],poly[1],poly[2],poly[3],], 1, 'Black', 'green')                   
    print memory_list,n
    #if n <= 8:
        #canvas.draw_polygon([[(n-1)*40, 0], [(n-1)*40, 80], [(n-1)*80, 80], [(n-1)*80, 0]], 1, 'Black', 'green')
        #n += 1

frame = simplegui.create_frame('Testing', 640, 80)
frame.set_draw_handler(draw)
frame.start()


new_game()
#mouse_click(pos)
#draw(canvas)
