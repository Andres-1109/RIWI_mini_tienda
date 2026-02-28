
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

subtotal = price * quantity
total = 0
discount = 0
if subtotal>= 50000:
    discount = subtotal*0.05
    total = subtotal - discount
else:
    total = subtotal

os.system("clear")
print(f"The name of the client is: {name}")
print("==========")
print(f"The name of the product is: {product}")
print("==========")
print(f"The subtotal is: {subtotal}")
print("==========")
print(f"The discount is: {discount}")
print("==========")
print(f"The total is: {total}")