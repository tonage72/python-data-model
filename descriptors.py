import re

class VIN:
    _validation_regex = re.compile('\d{9}')
    def __init__(self, vin='000000000'):
        self._vin = vin

    def __get__(self, instance, owner):
        return self._vin
        
    def __set__(self, *args, **kwargs):
        print(args)
        print(kwargs)
        if not self._validation_regex.match(new_value):
            print('Your vin must adhere to the appropriate formatting')
            return
        self._vin = new_value

    def __delete__(self, instance):
        print('No! You need a vin number')

class Car:
    vin = VIN()
    def __init__(self, color, vin=None):
        self._color = color
        if not vin is None:
            self.vin = VIN(vin)

    @property
    def color(self):
        print('Some calculation')
        return self._color

    @color.setter
    def color(self, value):
        if value not in {'red', 'green', 'blue'}:
            raise ValueError(f'The Color {value} is not valid')
        self._color = value

    @color.deleter
    def color(self):
        raise AttributeError('You cannot delete')
        #del self._color

car = Car('red')