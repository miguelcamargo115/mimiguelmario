from actor import Actor

from enemyEnum import EnemyStatus


class Enemy (Actor):
    direccion = 0
    isDead = False
    state = EnemyStatus 

    def __init__(self):
        Actor.__init__(self)
        pass

    def move():
        pass
    
    def detectCollision():
        return False
    
    def die():
        pass

    def destroy():
        pass




