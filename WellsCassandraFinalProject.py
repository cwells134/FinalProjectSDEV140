from tkinter import *

top = Tk()
top.title("Item Selection")
top.geometry("500x200")

# define global variables and functions called for buttons
item = 0


def headache():
    global item
    item = 1


def fidget():
    global item
    item = 2


def confirm():
    Label(cart, text="Your order has been sent!").grid(row=3, column=2)


def getPrice():
    quantity = int(entryQuantity.get())
    if item == 1:
        labelItem = Label(cart, text="Headache Pillow")
        labelItem.grid(row=0, column=0)
        labelQuantity = Label(cart, text=quantity)
        labelQuantity.grid(row=0, column=1)
        labelPrice = Label(cart, text="$7")
        labelPrice.grid(row=0, column=2)
        total = quantity * 7
    else:
        labelItem = Label(cart, text="Fidget Pillow")
        labelItem.grid(row=0, column=0)
        labelQuantity = Label(cart, text=quantity)
        labelQuantity.grid(row=0, column=1)
        labelPrice = Label(cart, text="$4")
        labelPrice.grid(row=0, column=2)
        total = quantity * 4
    labelTotal = Label(cart, text=f"Your total is: ${total}")
    labelTotal.grid(row=1, column=3)
    buttonChange = Button(cart, text="Cancel or Change Items", command=cart.destroy)
    buttonChange.grid(row=2, column=1)
    buttonConfirm = Button(cart, text="Confirm Order", command=confirm)
    buttonConfirm.grid(row=2, column=2)


# function to run error if options not selected and open new window with cart
def addToCart():
    if item == 0:
        Label(top, text="Please select an item.").grid(row=5, column=1)
    elif len(entryQuantity.get()) == 0 or entryQuantity.get().isalpha():
        Label(top, text="Please enter a quantity as a digit.").grid(row=5, column=1)
    else:
        global cart
        cart = Toplevel(top)
        cart.geometry("500x200")
        cart.title("Your Cart")
        getPrice()

# Label and buttons to select item


label1 = Label(top, text="Select Item: ")
label1.grid(row=0, column=0)
buttonHead = Button(top, text="Headache Pillow", command=headache)
buttonHead.grid(row=1, column=1)
buttonFidget = Button(top, text="Fidget Pillow", command=fidget)
buttonFidget.grid(row=1, column=2)
label2 = Label(top, text="Select Quantity: ")
label2.grid(row=4, column=0)
entryQuantity = Entry(top, bd=5)
entryQuantity.grid(row=4, column=1)
buttonCart = Button(top, text="Add to Cart", command=addToCart)
buttonCart.grid(row=5, column=3)


top.mainloop()
