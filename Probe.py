class Toyota:
    color = 'red'
    price = 1000000
    max_speed = 200
    current_speed = 0

    def info(self):
        print('Color: {}\nPrice: {}\nMax speed: {}\nCurrent speed: {}\n'.format(
            self.color, self.price, self.max_speed, self.current_speed
        ))

    def set_speed(self, speed):
        self.current_speed = speed


car_1 = Toyota()
car_1.info()
car_1.set_speed(190)
print(car_1.current_speed)
