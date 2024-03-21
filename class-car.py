class Car:
    def __int__(self, name, price, color):
        self.name = name
        self.price = price
        self.color = color
    def start(self):
        print(self.name+" started")

    car1 = Car("swift", 500000, "blue")
    car2 = Car("honda", 100000, "white")

    print(car1.name)
    car1.start()
    car2. start()