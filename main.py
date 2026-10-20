

class Carshop:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.car_list = []  #every new Carshop object gets its own list


    # create a def that shows the car list for the specific carshop
    def show_balance():
        pass

    def show_car_list():
        pass

    def send_new_car_to_specific_carshop(self): #self is what car object to be sent
        self.append(self)






class Car:
    def __init__(self,specific_carshop, brand, model, year, color, price, actual_value):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.price = price
        self.actual_value = actual_value
        specific_carshop.car_list.append(self)


#--------------- stop classes ---------------

zenshop = Carshop("ZenShop") # create the specific carshop object before creating the car objects

car1 = Car(zenshop,"Volvo", "XC60", 2015, "Yellow", 25000, 5000)
car2 = Car(zenshop, "Volvo", "242", 1984, "Black", 35000, 1500)


print(zenshop.name, zenshop.car_list)
