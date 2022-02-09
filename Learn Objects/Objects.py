from tkinter.messagebox import NO


class Car():
    carName = None 
    carPrice = None
    maxSpeed = None
    color = None

class Ford(Car):
    carName = 'Fiesta'
    carPrice = str(100) + '$'
    maxSpeed = str(120) + ' km'
    color = 'Black'

    def ShowInfo():
        print(carName, carPrice, maxSpeed, color)

obj = Ford()
obj.ShowInfo()