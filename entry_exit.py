from Bike import Bike
# from Car import Car
# from Bus import Bus
from Lot import Lot


print("Please define lot size")
# lot_ref=Lot
# def enter_lot():
#    Width=input("enter Width")
#    Depth=input("enter Depth")
#    Number=input("enter Number")
#    Series=input("enter Series")
#    Status=input("enter Status")
#    InTime=input("enter InTime")
#    lt=Lot(Width,Depth,Number,Series,Status,InTime)
Width=int(input("enter Width"))
Depth=int(input("enter Depth"))
Number=input("enter Number")
Series=input("enter Series")
Status=input("enter Status")
InTime=input("enter InTime")
lt=Lot(Width,Depth,Number,Series,Status,InTime)

def enter_bike():
   Milage=input("Enter Mileage")
   Name=input("enter name")
   Capacity=input("enter capacity")
   Width=input("enter Width")
   Depth=input("enter Depth")
   Number=input("enter Number")
   Manufacturer=input("Manufacturer")
   Allocation_time=print("Allocation Time ")
   bk=Bike(Milage,Name,Capacity,Width,Depth,Number,Manufacturer)

   
# ,Name,Capacity,Width,Depth,Number,Manufacturer
Bi=Bike(20,"rx100",2,100,25,"ts310159","yamaha")
print(Bi)
