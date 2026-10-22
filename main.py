

class Carshop:
    def __init__(self, name):
        self.name = name
        self.balance = 25000
        self.car_list = []  #every new Carshop object gets its own list


    # create a def that shows the car list for the specific carshop
    def show_balance(self):
        print(self.name, "balance is:", self.balance)
        

    def show_car_list(self):
        print(self.name, "now has these cars:")
        for i in self.car_list:
            print(i.brand, i.model, i.year, i.color, i.price, i.actual_value)

    

    def sell_car(car_to_sell, specific_carshop):   #self points at the car u sell
        print("selling the", car_to_sell.brand, car_to_sell.model, car_to_sell.year, car_to_sell.price)
        specific_carshop.car_list.remove(car_to_sell)
        specific_carshop.balance+=car_to_sell.price
        specific_carshop.balance+=5 # gets a bonus
        print(specific_carshop.name, "balance is:", specific_carshop.balance)
        Carshop.show_car_list(specific_carshop)
        


class Car: #dont compare definitions/methods in the class with the init/constructor below
    def __init__(self,specific_carshop, brand, model, year, color, price, actual_value):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.price = price
        self.actual_value = actual_value
        specific_carshop = specific_carshop.car_list.append(self)


#--------------- stop classes ---------------

zenshop = Carshop("ZenShop") # create the specific carshop object before creating the car objects

car1 = Car(zenshop,"Volvo", "XC60", 2015, "Yellow", 25000, 5000)
car2 = Car(zenshop, "Volvo", "242", 1984, "Black", 35000, 1500)
car3 = Car(zenshop, "Volvo", "850", 1955, "Red", 35000, 1500)
#zenshop is pointing to specific_carshop in the attributes for Car class (when creating the car object JUST LOOK AT IT)

Carshop.show_car_list(zenshop)
#print(zenshop.name, zenshop.car_list)

Carshop.show_balance(zenshop)
Carshop.sell_car(car3, zenshop)