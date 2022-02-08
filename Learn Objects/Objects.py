class Car():
    Engine = 1
    Wheels = 'yes'

    def Eng_Start(self, Engine):
        if Engine is 1:
            print('Engine is started')

    
obj = Car()
obj.Eng_Start(1)