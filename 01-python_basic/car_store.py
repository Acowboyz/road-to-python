# basic class
class Store(object):
    def select_car(self):
        pass
    
    def order(self, car_type):
        # Will call the method in child class
        return self.select_car(car_type)
    
class BMWCareStore(Store):
    def select_car(self, car_type):
        return BMWFactory().select_car_by_type(car_type)


class TOYOTACarStore(Store):
    def select_car(self,  car_type):
        # Car Store --> Factory --> Toyota (return)
        return TOYOTAFactory().select_car_by_type(car_type)

class BMWFactory(object):
    def select_car_by_type(self, car_type):
        if car_type == "BMW520i":
            return BMW520i()

# Design pattern "simply factory"
class TOYOTAFactory(object):
    # TOYOTA Factory
    def select_car_by_type(self, car_type):
        if car_type == "CRV":
            return CRV()

class Car(object):
    def move(self):
        print("moving")

class CRV(Car):
    def Intro(self):
        print("CRV")

class BMW520i(Car):
    def Intro(self):
        print("BMW520i")

bmw_store = BMWCareStore()
bmw_car = bmw_store.order("BMW520i")
bmw_car.Intro()

toyota_store = TOYOTACarStore()
toyota_car = toyota_store.order("CRV")
toyota_car.Intro()
