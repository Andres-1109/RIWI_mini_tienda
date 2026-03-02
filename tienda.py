
import os
print("Types of clients:")
print("0. Irregular")
print("1. Regular")
print("2. VIP")
clientType = 0
while True:
    try:
        clientType = int(input("Insert the type of client:"))
        if 0<=clientType<=2:
            break 
        else:
            print("Insert a number between 0 and 2")   
    except ValueError:
        print("Insert a valid number")
    
        print("Insert a number between 0 and 2")

while True:
    name = str(input("Please insert the name of the client: "))
    if name == None:
        print("Name is required")
    else:
        break

while True:        
    product = str(input("Please insert the name of the product: "))     
    if product == None:
        print("Product name is required")
    else:
        break

while True:
    try:
        price = float(input("Please insert the price of the product: "))
        if price <= 0:
            print("Please insert a valid price")
        else:
            break
    except ValueError:
        print("Please insert a valid price")    

while True:
    try:
        quantity = float(input("Please insert the quantity of the prouct: "))
        if quantity <= 0:
            print("Please insert a valid quantity")
        else:
            break
        break
    except ValueError:
        print("Please insert a valid quantity")        

#Subtotal calculation
subtotal = price * quantity
totalgross = 0
discount = 0

#Discount calculation
if subtotal>= 50000:
    discount = subtotal*0.05
    totalgross = subtotal - discount
else:
    totalgross = subtotal

#ClientDiscount
nameClientType = None
if clientType == 0:
    clientDiscount = totalgross* 0
    nameClientType = "Irregular"
elif clientType == 1:
    clientDiscount = totalgross * 0.05
    nameClientType = "Regular"
elif clientType == 2 and subtotal > 200000:
    clientDiscount = totalgross * 0.15
    nameClientType ="VIP"
else:
    clientDiscount = totalgross * 0.1
    nameClientType = "VIP"

totalgross -= clientDiscount 

#Taxes calculation    
iva = totalgross*0.19
totalnet = totalgross + iva

# Type of purchase
typeOfPurchase = None
if totalnet < 50000:
    typeOfPurchase = "Small"
elif 50000<=totalnet<=150000:
    typeOfPurchase = "Medium"
else:
    typeOfPurchase = "Big"

os.system("clear")
print(f"The name of the client is: {name}")
print("==========")
print(f"The name of the product is: {product}")
print("==========")
print(f"The subtotal is: {subtotal}")
print("==========")
print(f"The discount is: {discount}")
print("==========")
print(f"The total gross is: {totalgross}")
print("==========")
print(f"The IVA is: {iva}")
print("==========")
print(f"The total net is: {totalnet}")
print("==========")
print(f"Thanks for your purchase {name}")
print("==========")
print(f"You are a {nameClientType} client")
print("==========")
print(f"Your purchase was {typeOfPurchase}")
