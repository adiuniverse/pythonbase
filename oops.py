class Laptop:
    #properties
    name = 'hp'
    colour = 'black'
    ram = '8GB'
    display='60inch'

    def power_on(self):
        print('poweron')
    def power_off(self):
        print('poweroff')  
 
lap1 = Laptop()
lap2 = Laptop()
lap3 = Laptop()
lap1.power_off()