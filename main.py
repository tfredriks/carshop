

class Carshop:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.car_list = []  #every new Carshop object gets its own list


    # create a def that shows the car list for the specific carshop
    def show_balance():
        pass

    def show_car_list(self):
        print(self.name, "cars:")
        for i in self.car_list:
            print(i.brand, i.model, i.year, i.color, i.price, i.actual_value)



    def sell_car():
        pass



class Car:
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

zenshop.show_car_list()
#print(zenshop.name, zenshop.car_list)
