class Character:
    def __init__(self,name,initial_health):
        self.name = name
        self.health = initial_health
        self.inventory = []
        
    def __str__(self):
        s  = 'Name: ' + self.name
        s += ' Health: ' + str(self.health)
        s += ' Inventory: ' + str(self.inventory)
        return s
    def grab(self,item):
        self.inventory.append(item)
        
    def get_health(self):
        return self.health

def example():
    me = Character('Ryugasaki',100)
    print str(me)
    me.grab('pistol')
    me.grab('ammo x 7')
    print str(me)
    print 'Health: ',me.get_health()
    
example()    
