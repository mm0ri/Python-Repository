def data_input():
    print('--------------\n Book of restraunts.\n--------------\n Enter restraunt name and cuisine type: ')
    name, cuisine = input().split(', ')
    return name, cuisine

class Restraunt():

    #def __init__(self,r_name,r_type):

    def __init__(self):
        #r_name, r_type = data_input()
        self.__r_name = None
        self.__r_type = None
        self.__v_served = 0

    # methods

    def set_name_type(self):
        r_name, r_type = data_input()
        self.__r_name = r_name
        self.__r_type = r_type

    def describe_r(self):
        print('The restraunt has name: {0}, and his cuisine is: {1}'.format(self.__r_name, self.__r_type))

    def open_r(self):
        print(self.__r_name, 'Is opened!')

    def served_visitors_increase(self, visitors):
        self.__v_served += visitors
 
    def get_served_visitors(self):
        print('Visitors were served today:', self.__v_served)

class IceCreamStand(Restraunt):

    def __init__(self):
        #super().__init__(self)
        self.__res = ''
        self.__flavors = ['Chocolate', 'Strawberry']

    def show_flavors(self):

        for element in self.__flavors:
            self.__res = self.__res + element + ' '
        print('The ice cream stand has:', self.__res)



def main_cycle():

    #r_name, r_type = data_input()
    #Bureau = Restraunt(r_name, r_type)

    #Bureau = Restraunt()
    #Bureau.set_name_type()
    #Bureau.describe_r()
    #Bureau.open_r()
    #Bureau.served_visitors_increase(112)
    #Bureau.get_served_visitors()

    #SushiSet = Restraunt()
    #SushiSet.set_name_type()
    #SushiSet.describe_r()
    #SushiSet.open_r()

    BaskinRobbins = IceCreamStand()
    BaskinRobbins.set_name_type()
    BaskinRobbins.describe_r()
    BaskinRobbins.show_flavors()

main_cycle()