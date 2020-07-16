class Lunch:

    def __init__(self, menu):
        self.menu = menu    # String

    def menu_price(self):
        if self.menu == 'Menu 1':
            print('Price is 12 Quid sterling')
        elif self.menu == 'Menu 2':
            print('Price is 14 Quid sterling')
        else:
            print('Error in input menu.')


my_lunch=Lunch('Menu cock1')
my_lunch.menu_price()