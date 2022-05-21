import math
def num_units(load):
    if (load / 8000).is_integer():
        unitsrequired = int (load / 8000)
    else:
        unitsrequired = int (load / 8000) + 1
    return unitsrequired

def num_trailers (load):
    if (load / 4000).is_integer():
        trailersrequired = int(load / 4000)
    else:
        trailersrequired = int(load / 4000) + 1
    return trailersrequired

def total_order_amount(load):
    return load * 3000

clientName = input('Enter Client name: ')
collectionAddress = input('Enter Collection Address: ')
deliveryAddress = input('Enter Delivery Address: ')
load = float((input("enter the load in kilograms:")))

    #total number of units required to transport the load
print(f"number of units required to transport the load{num_units(load)}")
    
    #The number of trailers required to transport the load
print(f"The number of trailers required to transport the load is{num_trailers(load)}")

    #The total order amount if each kilograms is charged at 3000
print(f"The total order amount if each kilograms is charged at 3000 is{total_order_amount(load)}")
    
    #The Receipt for customer
print(f"customers reciept:")
print(f" customer name: {clientName}")
print(f" Collection address is: {collectionAddress}")
print(f" delivery address is: {deliveryAddress}")
print(f" The load in kilograms is: {load}")
print(f" transportation  units required: {num_units(load)}")
print(f"Total  number of trailers required : {num_trailers(load)}")
print(f" payable amount: {total_order_amount(load)}")
