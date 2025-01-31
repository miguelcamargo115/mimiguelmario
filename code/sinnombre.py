from enum import Enum

from actor import Actor


class sinNombre(Actor):

    direction = 0
    dead = False
    moving = False
    state = Enum

    def __init__(self):
        Actor.__init__(self)
        pass

    def move():
        pass

    def detectCollision():
        return False
    
    def isJumping():
        return False
    
    def isdead():
        return False
    
    def ismoving():
        return False