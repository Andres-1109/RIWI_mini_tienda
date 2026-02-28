
import os


name = str(input("Please insert the name of the client: "))
product = str(input("Please insert the name of the product: "))     
while True:
    try:
        price = float(input("Please insert the price of the product: "))
        break
    except ValueError:
        print("Please insert a valid price")        
while True:
    try:
        quantity = float(input("Please insert the quantity of the prouct: "))
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

#Taxes calculation    
iva = totalgross*0.19
totalnet = totalgross + iva

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