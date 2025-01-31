

from enemy import Enemy


class Goomba(Enemy):
    walkinSpeed = 0
    walkinDistance = 0

    def __init__(self):
        Enemy.__init__(self)
        pass

    def pace(self): 
        pass
