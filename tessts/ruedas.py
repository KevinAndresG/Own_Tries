#!/usr/bin/python3
class Vehicles():

    def __init__(self):
        __lenght = 200
        __width = 100
        __wheels = 4

    def mwheels(self, nwheels):
        self.__wheels = nwheels
        if isinstance(self.__wheels, int) is False:
            return ("must be an integer")
        if self.__wheels >= 17:
            print("it's centipede")
        if self.__wheels in range(9, 17):
            print("this's is a truck because it has", self.__wheels, "wheels")
        if self.__wheels in range(nwheels, 6):
            if self.__wheels == 2:
                print("this's a motorcycle beacuse it has",
                      self.__wheels, "wheels")
            if self.__wheels == 4:
                print("this's a car beacuse it has", self.__wheels, "wheels")
            if self.__wheels != 2 and self.__wheels != 4 and self.__wheels and self.__wheels != 0:
                print("None")
            if self.__wheels == 0:
                print("this's an ovni")

    def state(self):
        print("the size of the car is ", self.__width)


vehicule1 = Vehicles()
truck = Vehicles()

vehicule1.wheels = 2
vehicule1.mwheels(0)
vehicule1.mwheels(10)
vehicule1.mwheels(3)
vehicule1.mwheels(20)
vehicule1.mwheels(1)
vehicule1.mwheels(54545)
vehicule1.mwheels(-1)
print(vehicule1.mwheels("HI"))
print(vehicule1.mwheels(5.5))
print('\n__________now just a truck__________\n')
truck.mwheels(15)

print('\n__________TRY__________\n')

vehicule1.width = 5

vehicule1.state()
