class Bicycle():

    def __init__(self, color):
        self.__color = color
        self.__side = 'Steering wheel is not turned anywhere'
        self.__speed = 0
    
    def set_speed(self):
        self.__speed = 0

    def set_side(self):
        self.__side = 'Steering wheel is turned forward'

    #Methods

    def get_color(self):
        return print('Bike color is:', self.__color)
        
    def get_speed(self):
        return print(self.__speed)

    def get_side(self):
        return print(self.__side)

    def accelerate_speed(self):
        self.__speed +=5

    def downscale_speed(self):
        self.__speed -+5

    def turn_left(self):
        self.__side = 'Steering wheel is turned left'

    def turn_right(self):
        self.__side = 'Steering wheel is turned Right'

    def stop_movement(self):
        self.__speed -= self.__speed

def main():

    color = input('Enter bike color: ')

    Pobeda = Bicycle(color)

    Pobeda.get_side()
    Pobeda.get_color()

main()