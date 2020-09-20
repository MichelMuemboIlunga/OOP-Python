class Vehicle:
    def __init__(self, make, model, year, weight, needs_maintenance=False, trips_since_maintenance=0):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.needs_maintenance = needs_maintenance
        self.trips_since_maintenance = trips_since_maintenance

    def set_make(self, make):
        self.make = make

    def set_model(self, model):
        self.model = model

    def set_year(self, year):
        self.year = year

    def set_weight(self, weight):
        self.weight = weight


# creating a cars sub class that inherit from a vehicle parent(super) class
class Cars(Vehicle):
    def __init__(self, make, model, year, weight, needs_maintenance, trips_since_maintenance, is_driving):
        super().__init__(make, model, year, weight, needs_maintenance, trips_since_maintenance)
        self.is_driving = is_driving

    def drive(self, is_driving=True):
        self.is_driving = is_driving
        print(f"Is {self.model} car driving {self.is_driving}")

    def stop(self, is_driving=False):
        self.is_driving = is_driving
        if not self.is_driving:
            self.trips_since_maintenance += 1
            print(f"your car is made at {self.make} at {self.year} the model is {self.model} "
                  f" the weight of the car is {self.weight} "
                  f"and the distance drive is {self.trips_since_maintenance}")
            if self.trips_since_maintenance > 100:
                self.needs_maintenance = True
                print(f"You need maintenance {self.needs_maintenance} ")
            else:
                print(f"your cars is in a good maintenance {self.trips_since_maintenance}")
        else:
            print("You are driving")

    def repair(self):
        self.trips_since_maintenance = 0
        self.needs_maintenance = False
        print(f"Your trip is {self.trips_since_maintenance} and your maintenance state is {self.needs_maintenance} ")


# creating a plane sub class
class Plane(Vehicle):
    def __init__(self, make, model, year, weight, needs_maintenance, trips_since_maintenance, flying, landing):
        super().__init__(make, model, year, weight, needs_maintenance, trips_since_maintenance)
        self.flying = flying
        self.landing = landing

    def fly(self, flying=True):
        self.flying = flying
        self.flying = flying
        print(f"Is {self.model} plane flying {self.flying}")

    def land(self, landing=False):
        self.landing = landing
        if not self.landing:
            self.trips_since_maintenance += 1
            print(f"your plane is made at {self.make} at {self.year} the model is {self.model} "
                  f" the weight of the car is {self.weight} "
                  f"and the distance drive is {self.trips_since_maintenance}")

            while self.trips_since_maintenance > 100:
                self.needs_maintenance = True
                print(f"You need maintenance {self.needs_maintenance} you can not fly land now ")
                break

            else:
                print(f"your Plane is in a good maintenance {self.trips_since_maintenance}")
        else:
            print("You are flying")


# creating cars

myCar1 = Cars("New york", "Benz", 1995, 78, False, 10, True)
myCar1.drive()

myCar2 = Cars("Canada", "Audi", 2000, 100, True, 99, False)
myCar2.stop()

myCar3 = Cars("Germany", "Porches", 1993, 200, False, 101, True)
myCar3.stop()
myCar3.repair()

myPlane = Plane("Europe", "B52", 2001, 10000, True, 101, False, True)
myPlane.fly()
myPlane.land()

myPlane2 = Plane("Europe", "B52", 2001, 10000, True, 10, True, True)
myPlane2.land()
