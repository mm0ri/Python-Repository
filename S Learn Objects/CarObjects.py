class Car():

    def __init__(self, color, manufacturer, year, horse_power, weight):
        self.__color = color
        self.__manufacturer = manufacturer
        self.__year = year
        self.__horse_power = horse_power
        self.__weight = weight

    # methods

    def set_speed(self):
        None

    def set_weight(self):
        None
 
    def calc_power(self, weight, horse_power):
        None

    def get_attributes(self):
        print('Car color is: {0}, car manufacturer is: {1}, production year is: {2}, and this car has {3} horse power, also its weight is: {4}.'.format(self.__color, self.__manufacturer, self.__year ,self.__horse_power, self.__weight))

class Battery():

    def __init__(self, battery_size, charge_time):
        self.__battery_size = battery_size
        self.__charge_time = charge_time

    def get_battery_attributes(self):
        print('Battery size is: {0}, and it takes {1} hours to charge it full.'.format(self.__battery_size, self.__charge_time))

class E_Car(Car):

    def __init__(self, color, manufacturer, year, horse_power, weight):
        super().__init__(color, manufacturer, year, horse_power, weight)
        self.battery = Battery('85KwH', '2')

Ford = Car('White', 'FordCO', '2016', '105', '1100Kg')
Ford.get_attributes()

Tesla = E_Car('Black', 'Tesla', '2018', '400+', '2500Kg')
Tesla.get_attributes()
Tesla.battery.get_battery_attributes()