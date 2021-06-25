class CarPark:
    def __init__(self, num_spaces):
        self.__customers = [] # this will be an array of type Vehicle - containment
        self.__num_spaces = num_spaces
    def parkCustomer(self,veh):  #veh is of type Vehicle
        if self.__num_spaces > 0:
            self.__customers.append(veh)
        else:
            print("No spaces, go away")
    def leave(self,veh):
            for i in self.__customers:  # i represents each vehicle object in the list
                print(i.getColour())
            '''print("Please pay 300 bob.")
            self.customers.pop()
            return veh
        else:
            print("Your car isn't here!")
            return 0'''

class Vehicle:
    __num_wheels = 0
    def __init__(self,num_wheels,colour):
        # this is what a constructor looks like in Python
        self.__num_wheels = num_wheels
        self.__colour = colour
    def changeColour(self,col):
        self.__colour = col
    def getColour(self):
        return self.__colour
    def __str__(self):  # this defines what to do when you print() an instance of this class
        return "I am a vehicle with a lovely " + self.__colour + " colour and " + str(self.__num_wheels) + " wheels."

class Car(Vehicle):  # inherits from superclass Vehicle
    def __init__(self,num_wheels,colour):
        super().__init__(num_wheels,colour)  # call the superclass constructor
        self.type = "Car"

car1 = Car(3,"red")
print(car1)
car1.changeColour("yellow")
print(car1)

MrWCP = CarPark(2)
MrWCP.parkCustomer(car1)
MrWCP.leave(car1)
MrWCP.leave(car1)

