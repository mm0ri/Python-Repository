def data_input():
    print('--------------\n Book of restraunts.\n--------------\n Enter restraunt name and cuisine type: ')
    name, cuisine = input().split(', ')
    return name, cuisine

class Restraunt():

    #def __init__(self,r_name,r_type):

    def __init__(self):
        r_name, r_type = data_input()
        self.__r_name = r_name
        self.__r_type = r_type
        self.__v_served = 0

    # methods

    def describe_r(self):
        print('The restraunt has name: {0}, and his cuisine is: {1}'.format(self.__r_name, self.__r_type))

    def open_r(self):
        print(self.__r_name, 'Is opened!')

    def served_visitors_increase(self, visitors):
        self.__v_served += visitors
 
    def get_served_visitors(self):
        print('Visitors were served today:', self.__v_served)


def main_cycle():

    #r_name, r_type = data_input()
    #Bureau = Restraunt(r_name, r_type)

    Bureau = Restraunt()
    Bureau.describe_r()
    Bureau.open_r()
    Bureau.served_visitors_increase(112)
    Bureau.get_served_visitors()

    #SushiSet = Restraunt()
    #SushiSet.describe_r()
    #SushiSet.open_r()

main_cycle()