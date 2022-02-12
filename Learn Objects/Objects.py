from tkinter.messagebox import NO


class Car():
    carName = None 
    carPrice = None
    maxSpeed = None
    color = None

class Ford(Car):
    carName = 'ModelT'
    carPrice = str(100) + '$'
    maxSpeed = str(120) + ' km'
    color = 'Black'
    

obj = Ford()
#obj.ShowInfo()