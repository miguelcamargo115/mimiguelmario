class Actor():
    localPositionX = 0 
    localPositionY= 0  
    __positionLocal = [] 

    def __init__(self):
        pass 


    def updatePosition(self, positionX, positionY):
        self.localPositionX = positionX
        self.localPositionY = positionY
        self.__positionLocal = [self.localPositionX, self.localPositionY]
        return self.__positionLocal
    