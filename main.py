

class Carshop:
    def __init__(self, name):
        self.name = name
        self.car_list = []


    # create a def that shows the car list for the specific carshop


class Car:
    def __init__(self,which_car_shop_to_send_to, brand, model, year, color, price, actual_value):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.price = price
        self.actual_value = actual_value
        which_car_shop_to_send_to.car_list.append(self)


#--------------- stop classes ---------------

zenshop = Carshop("ZenShop") # create the specific carshop object before creating the car objects

car1 = Car(zenshop,"Volvo", "XC60", 2015, "Yellow", 25000, 5000)
car2 = Car(zenshop, "Volvo", "242", 1984, "Black", 35000, 1500)


print(zenshop.name, zenshop.car_list)
