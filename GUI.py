import tkinter as tk

window= tk.Tk()
window.title("Mini tienda")
window.geometry("800x800")

    # Type of client section
lbTypeOfClients= tk.Label(window, text="Types of clients\n0. Irregular\n1. Regular\n2. VIP")
lbTypeOfClients.pack()

askClientType = tk.Entry(window)
askClientType.pack()

messageTypeOfclient = tk.Label(window, text="")
messageTypeOfclient.pack()

def validateTypeOfClients():
    try:
        clientType = int(askClientType.get())
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

def validateName():
    name = askname.get()
    if name == "":
        messageName.config(text="Name is required")
    else:
        messageName.config(text="Name is valid")
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

def validateProduct():
    product = askProduct.get()
    if product == "":
        messageProduct.config(text="Product name is required")
    else:
        messageProduct.config(text="Product name is valid")
    
buttonProduct = tk.Button(productSection, text="Continue", command=validateProduct)
buttonProduct.pack()


window.mainloop()
