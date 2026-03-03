import tkinter as tk

window= tk.Tk()
window.title("Mini tienda")
window.geometry("1200x1200")

    # Type of client section
lbTypeOfClients= tk.Label(window, text="Types of clients\n0. Irregular\n1. Regular\n2. VIP")
lbTypeOfClients.pack()

askClientType = tk.Entry(window)
askClientType.pack()

messageTypeOfclient = tk.Label(window, text="")
messageTypeOfclient.pack()
clientType = askClientType.get()

def validateTypeOfClients():
    try:
        clientType = int(clientType)
        if 0<=clientType<=2: 
            messageTypeOfclient.config(text="Valid client type")
            nameSection.pack()
        else:
            messageTypeOfclient.config(text="Insert a number between 0 and 2")

    except ValueError:
        messageTypeOfclient.config(text="Insert a valid number")

buttonTypeOfClient = tk.Button(window, text="Continue", command=validateTypeOfClients)
buttonTypeOfClient.pack()

    #Name Section
nameSection = tk.Frame(window)
labelName = tk.Label(nameSection, text="Please insert the name of the client: ")
labelName.pack()
askname = tk.Entry(nameSection)
askname.pack()
messageName = tk.Label(nameSection, text="")
messageName.pack()
name = askname.get()

def validateName():
    if name == "":
        messageName.config(text="Name is required")
    else:
        messageName.config(text="The name is valid")
        productSection.pack()
    
buttonName = tk.Button(nameSection, text="Continue", command=validateName)
buttonName.pack()

    #Product Section
productSection = tk.Frame(window)
LabelProduct = tk.Label(productSection, text="Please insert the name of the product: ")
LabelProduct.pack()
askProduct = tk.Entry(productSection)
askProduct.pack()
messageProduct = tk.Label(productSection, text="")
messageProduct.pack()
product = askProduct.get()

def validateProduct():
    if product == "":
        messageProduct.config(text="Product name is required")
    else:
        messageProduct.config(text="The product name is valid")
        priceSection.pack()
    
buttonProduct = tk.Button(productSection, text="Continue", command=validateProduct)
buttonProduct.pack()

    #Price Section
priceSection= tk.Frame(window)
LabelPrice = tk.Label(priceSection, text="Please insert the price of the product: ")
LabelPrice.pack()
askPrice = tk.Entry(priceSection)
askPrice.pack()
messagePrice= tk.Label(priceSection, text="")
messagePrice.pack()
price = askPrice.get()

def validatePrice():
    try:
        price = float(price)
        if price<= 0:
            messagePrice.config(text="Please insert a valid price")
        else:
            messagePrice.config(text="The price is valid")
            quantitySection.pack()
    except ValueError:
        messagePrice.config(text="Please insert a valid price")

buttonPrice = tk.Button(priceSection, text="Continue", command=validatePrice)
buttonPrice.pack()

    #Quantity Section
quantitySection = tk.Frame(window)
labelQuantity = tk.Label(quantitySection, text="Please insert the quantity of the prouct: ")
labelQuantity.pack()
askQuantity = tk.Entry(quantitySection)
askQuantity.pack()
messageQuantity = tk.Label(quantitySection, text="")
messageQuantity.pack()
quantity = askQuantity.get()

def validateQuantity():
    try:
        quantity = float(quantity)
        if quantity<= 0:
            messageQuantity.config(text="Please insert a valid quantity")
        else:
            messageQuantity.config(text="The quantity is valid")
    except ValueError:
        messageQuantity.config(text="Please insert a valid quantity")

buttonQuantity = tk.Button(quantitySection, text="Continue", command=validateQuantity)
buttonQuantity.pack()



window.mainloop()
