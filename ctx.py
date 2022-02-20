class Car:
    def __init__(self):
        self.running = False
        self.odometer = 0
        self.direction = 90
    
    def move(self, amt):
        if self.running:
            self.odometer += amt

    def _turn(self, amt):
        if self.running:
            self.direction += amt

    def turn_right(self):
        self._turn(90)

    def turn_around(self):
        self._turn(180)

    def __enter__(self):
        self.running = True
        return self

    def __exit__(self, *args, **kwargs):
        self.running = False
        print(f'you have moved {car.odometer} miles')
        print(f'you are facing {car.direction} degrees')
    
with Car() as car:
    car.move(10)
    car.turn_right()
    car.move(10)
    car.turn_around()