
#----classes

#----------------CLASS Carshop------------------------
class Carshop:
    def __init__(self, name):
        self.name = name
        self.balance = 25000
        self.cars = []  #every new Carshop object gets its own list
        self.customers = []

    # create a def that shows the car list for the specific carshop
    def show_balance(self):
        print(self.name, "balance is:", self.balance)
        
    def show_cars(self): #shows the cars for specific carshop
        print(self.name, "now has these cars:")
        for i in self.cars:
            print(i.brand, i.model, i.year, i.color, i.price, i.actual_value)

    def show_customers(specific_carshop): #and add if the customer has bought or not bought any cars
        print("Customer list of", specific_carshop.name)
        for i in specific_carshop.customers:
            print(i. firstname, i.lastname, i.boughtcars)

    def sell_car(car_to_sell, specific_carshop):   #self points at the car u sell
        print("selling the", car_to_sell.brand, car_to_sell.model, car_to_sell.year, car_to_sell.price)
        specific_carshop.cars.remove(car_to_sell)
        specific_carshop.balance+=car_to_sell.price
        specific_carshop.balance+=5 # gets a bonus
        print(specific_carshop.name, "balance is:", specific_carshop.balance)
        Carshop.show_cars(specific_carshop)

    def show_sales_history(): #what the  carshop has sold
        pass

    def remove_car(self,specific_carshop):   #remove from stock
        specific_carshop.cars.remove(self)
        pass

    def search_car():
        pass    

#----------------CLASS Cars------------------------
class Car: #dont compare definitions/methods in the class with the init/constructor below
    def __init__(self,specific_carshop, brand, model, year, color, price, actual_value):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.price = price
        self.actual_value = actual_value
        specific_carshop = specific_carshop.cars.append(self)

    def get_details(specific_carshop, car): #returns(not yet) car details
        print("\n")
        for i in specific_carshop.cars:
            if i == car:    #need to have like this since cars is a list of cars/to search
                print(i.brand, i.model, i.year, i.color, i.price, i.actual_value)
        

    def update_price():
        pass

    def apply_discount():
        pass

    def calculate_total_price(): #if buy many cars
        pass

    def calculate_age(): #check year to date, aka age of the car
        pass

    def change_condition(): #update if new or 2nd hand
        pass

#----------------CLASS Customers------------------------
class Customers:
    def __init__(self, specific_carshop, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.boughtcars = []    # at print shows [] if the customers hasnt bought any cars
        specific_carshop = specific_carshop.customers.append(self)

    def customer_details():
        pass

    def update_contact_info():
        pass

    def view_purchase_history():
        pass

    def buy_car():
        pass

    def calculate_total_spent():
        pass


#--------------- stop classes ---------------

#--objects of classes

# Zenshop object in Carshop class
zenshop = Carshop("ZenShop") # create the specific carshop object before creating the car objects

# Car objects in Car class
car1 = Car(zenshop,"Volvo", "XC60", 2015, "Yellow", 25000, 5000)
car2 = Car(zenshop, "Volvo", "242", 1984, "Black", 35000, 1500)
car3 = Car(zenshop, "Volvo", "850", 1955, "Red", 35000, 1500)
#zenshop is pointing to specific_carshop in the attributes for Car class (when creating the car object JUST LOOK AT IT)

# Customer objects in Customers class

customer1 = Customers(zenshop, "Adam", "Bertilsson")
customer2 = Customers(zenshop, "Erik", "Svensson")
customer3 = Customers(zenshop, "Lena", "Ericsson")
customer4 = Customers(zenshop, "Anna", "Moufa")
customer5 = Customers(zenshop, "Tomas", "Kolbert")








#--------methods runs below
Carshop.show_cars(zenshop)


Carshop.show_balance(zenshop)
Carshop.sell_car(car3, zenshop)

Carshop.show_customers(zenshop)
print("\n\n")
Carshop.remove_car(car1,zenshop)    #remove car1 from zenshop
Carshop.show_cars(zenshop)

Car.get_details(zenshop, car2)