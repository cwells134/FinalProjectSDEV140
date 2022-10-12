from tkinter import *  # import tkinter
from PIL import ImageTk, Image  # import PIL

# Creating initial
top = Tk()
top.title("Item Selection")
top.geometry("500x200")

# initialize item variable, used for input validation and item selection
item = 0


# functions for item selection buttons
def headache():
    global item
    item = 1


def fidget():
    global item
    item = 2


# function for confirm button
def confirm():
    Label(cart, text="Your order has been sent!").grid(row=3, column=2)


# displays second window/cart, individual item cost and total
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
        cartItem1 = ["Headache Pillow", quantity, 7]
    else:
        labelItem = Label(cart, text="Fidget Pillow")
        labelItem.grid(row=0, column=0)
        labelQuantity = Label(cart, text=quantity)
        labelQuantity.grid(row=0, column=1)
        labelPrice = Label(cart, text="$4")
        labelPrice.grid(row=0, column=2)
        total = quantity * 4
        cartItem1 = ["Fidget Pillow", quantity, 4]
    labelTotal = Label(cart, text=f"Your total is: ${total}")
    labelTotal.grid(row=1, column=3)
    buttonCancel = Button(cart, text="Cancel or Change", command=cart.destroy)
    buttonCancel.grid(row=2, column=1)
    buttonConfirm = Button(cart, text="Confirm Order", command=confirm)
    buttonConfirm.grid(row=2, column=3)
    return cartItem1


# function to run error if options not selected and open new window with cart
def addToCart():
    if item == 0:
        Label(top, text="Please select an item.").grid(row=5, column=1)
    elif not entryQuantity.get().isdigit():
        Label(top, text="Please enter a quantity as a digit.").grid(row=5, column=1)
    else:
        global cart
        cart = Tk()
        cart.title("Cart")
        cart.geometry("500x200")
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
buttonCart.grid(row=6, column=3)
buttonCancel = Button(top, text="Cancel", command=top.destroy)
buttonCancel.grid(row=6, column=1)

# Images for the GUI cart and cancel
img = Image.open("cart.jpg")
img = img.resize((50, 50))
imgCart = ImageTk.PhotoImage(img)
label3 = Label(top, image=imgCart)
label3.grid(row=6, column=4)

img2 = Image.open("cancel.jpg")
img2 = img2.resize((50, 50))
imgCancel = ImageTk.PhotoImage(img2)
label4 = Label(top, image=imgCancel)
label4.grid(row=6, column=0)

top.mainloop()
