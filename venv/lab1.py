from abc import ABC, abstractmethod

class Item(ABC):
    pass


class ComputerLike(ABC, Item):
    # __CPU = ""
    # __GPU = ""
    # __Memory = ""
    def __init__(self, CPU, GPU, Memory):
        self.__CPU = CPU
        self.__GPU = GPU
        self.__Memory = Memory

    def getCPU(self):
        return self.__CPU
    def getGPU(self):
        return self.__GPU
    def getMemory(self):
        return self.__Memory

    def setCPU(self, value):
        self.__CPU = value
    def setGPU(self, value):
        self.__GPU = value
    def setMemory(self, value):
        self.__Memory = value

class HasDisplay(ABC, ComputerLike):
    pass

class HasCamera(ABC,ComputerLike):
    pass

class MobilePhone(HasDisplay, HasCamera):
    # __NumberOfSimCards = 0

    def __init__(self, NumberOfSimCards):
        self.__NumberOfSimCards = NumberOfSimCards
        super(HasDisplay, HasCamera, self).__init__() #??
    def getx(self):
        return self.__NumberOfSimCards
    def setx(self, value):
        self.__NumberOfSimCards = value


class Tablet(HasDisplay, HasCamera):
    # hasSimCard = True

    def __init__(self, hasSimCard):
        self.__hasSimCard = hasSimCard
        super(HasDisplay, HasCamera, self).__init__() #??
    def getx(self):
        return self.__hasSimCard
    def setx(self, value):
        self.__hasSimCard = value

