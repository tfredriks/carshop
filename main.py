


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
        print("\n", self.name, "now has these cars:")
        for i in self.cars:
            print(i.brand, i.model, i.year, i.color, i.price, i.actual_value, i.condition)

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

    def calculate_total_price(self, firstcar, secondcar): #self blir zenshop. when run the function as zenshop.calculate_total_price(self, firstcar, secondcar) if buy 2 cars (put attributes like car1 etc)
            total_price = firstcar.price + secondcar.price
            print(
                "Total Price for", firstcar.brand, firstcar.model, 
                "and", 
                secondcar.brand, secondcar.model,"is:", total_price
                )
            pass

#----------------CLASS Car------------------------
class Car: #dont compare definitions/methods in the class with the init/constructor below
    def __init__(self,specific_carshop, brand, model, year, color, price, actual_value):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.price = price
        self.actual_value = actual_value
        self.condition = "New"
        specific_carshop = specific_carshop.cars.append(self)

    def get_details(specific_carshop, car): #returns(not yet) car details
        print("\nDetails for", car.brand, car.model )
        for i in specific_carshop.cars:
            if i == car:    #need to have like this since cars is a list of cars/to search
                print("Year: ",i.year, ", Color:", i.color, ", Price:", i.price, ", Actual Value:", i.actual_value, "Condition:", i.condition)
        

    def update_price(self, specific_carshop): 
       """ if the def were in Carshop class then could run zenshop.update_price...
       self, but now has to put specific_carshop as attribute """
       for i in specific_carshop.cars:
            if i == self:
                new_price = input("Specify new price for the car:")
                self.price = new_price
                return self.price


    def apply_discount():

        pass  

    def calculate_age(): #check year to date, aka age of the car
        pass

    def change_condition(self, specific_carshop): #update if new or 2nd hand #!!!!!!!!!!!!!!!!!!
        for i in specific_carshop.cars:
                    if i == self:
                        self.condition = "Used"
        

    
#----------------CLASS Customers------------------------
class Customers:
    def __init__(self, specific_carshop, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
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
#zenshop is pointing to specific_carshop in the attributes for Car class (when creating the car object JUST LOOK AT IT)
zenshop = Carshop("Zen Shop") # create the specific carshop object before creating the car objects
smoothshop = Carshop("Smooth Shop")

# Car objects in Zen Shop's car list
car1 = Car(zenshop,"Volvo", "XC60", 2015, "Yellow", 25000, 5000)
car2 = Car(zenshop, "Volvo", "242", 1984, "Black", 35000, 1500)
car3 = Car(zenshop, "Volvo", "850", 1955, "Red", 35000, 1500)
car4 = Car(zenshop, "Volvo", "242", 1984, "Black", 35000, 1500)
car5 = Car(zenshop, "Volvo", "850", 1955, "Red", 35000, 1500)
car6 = Car(zenshop,"Volvo", "XC60", 2015, "Yellow", 25000, 5000)
car7 = Car(zenshop, "Volvo", "242", 1984, "Black", 35000, 1500)
car8 = Car(zenshop, "Volvo", "850", 1955, "Red", 35000, 1500)
car9 = Car(zenshop, "Volvo", "242", 1984, "Black", 35000, 1500)
car10 = Car(zenshop, "Volvo", "850", 1955, "Red", 35000, 1500)

# Car objects in Smooth Shop's car list
# FIX SUCH THAT CAN HAVE car1 in the list as car1 (car11) below
car11 = Car(smoothshop,"Volvo", "XC60", 2015, "Yellow", 25000, 5000)
car12 = Car(smoothshop, "Volvo", "242", 1984, "Black", 35000, 1500)
car13 = Car(smoothshop, "Volvo", "850", 1955, "Red", 35000, 1500)
car14 = Car(smoothshop, "Volvo", "242", 1984, "Black", 35000, 1500)
car15 = Car(smoothshop, "Volvo", "850", 1955, "Red", 35000, 1500)
car16 = Car(smoothshop,"Volvo", "XC60", 2015, "Yellow", 25000, 5000)
car17 = Car(smoothshop, "Volvo", "242", 1984, "Black", 35000, 1500)
car18 = Car(smoothshop, "Volvo", "850", 1955, "Red", 35000, 1500)
car19 = Car(smoothshop, "Volvo", "242", 1984, "Black", 35000, 1500)
car20 = Car(smoothshop, "Volvo", "850", 1955, "Red", 35000, 1500)

# Customer objects in Zen Shop's customer list
customer1 = Customers(zenshop, "Adam", "Bertilsson", 25)
customer2 = Customers(zenshop, "Erik", "Svensson", 78)
customer3 = Customers(zenshop, "Lena", "Ericsson", 43)
customer4 = Customers(zenshop, "Anna", "Moufa", 35)
customer5 = Customers(zenshop, "Tomas", "Kolbert", 45)

# Customer objects in Smooth Shop's customer list
# FIX SUCH THAT CAN HAVE customer1 in the list as customer1 (customer11) below
customer11 = Customers(smoothshop, "Johan", "Svensson", 50)
customer12 = Customers(smoothshop, "Anne", "Martinsson", 55)
customer13 = Customers(smoothshop, "Jasmin", "Dobrosson", 35)
customer14 = Customers(smoothshop, "Xi", "Zheng", 22)
customer15 = Customers(smoothshop, "Zhang", "Jia Jie", 18)

#--------methods runs below
Carshop.show_cars(zenshop)


Carshop.show_balance(zenshop)
Carshop.sell_car(car3, zenshop)

Carshop.show_customers(zenshop)
print("\n\n")
Carshop.remove_car(car1,zenshop)    #remove car1 from zenshop
Carshop.show_cars(zenshop)



Car.get_details(zenshop, car2)

car1 = Car(zenshop,"Volvo", "XC60", 2015, "Yellow", 25000, 5000)
zenshop.calculate_total_price(car1, car2)

Car.change_condition(car1, zenshop)
Carshop.show_cars(zenshop)

#Car.update_price(car5, zenshop) #fix such that the def is written the same way, much easier to follow
Car.get_details(zenshop, car5)

Carshop.show_cars(smoothshop)
Carshop.show_customers(smoothshop)
