from enemy import Enemy


class Koopa(Enemy):
    walkingSpeed = 0
    walkingDistance = 0 

    def __init__(self):
        Enemy.__init__(self)
        pass
    
    def pace(self):
        pass

    def saludo(self):
        return  "saludos desde koopa"
        
        
