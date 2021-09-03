from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("500x500")
root.title("Menu Survey")
Pizza = IntVar()
Chicken = IntVar()


def on_closing():
    if messagebox.askokcancel("Quit", "Thank you for your opinion. Do you want to quit?"):
        root.destroy()


def clicked(value):
    mylabel = Label(root, text="You select " + value)
    mylabel.pack(anchor=W)
    b2 = Button(root, text="Exit", command=on_closing).pack(anchor=W)


def pizza_options():
    la = Label(root, text='Choose your favorite toppings').pack()

    toppings = [
        ('Cheese', 'Cheese'),
        ('Pepperoni', 'Pepperoni'),
        ('Hawaiian Chicken', 'Hawaiian Chicken'),
        ('Veggie Lover', 'Veggie Lover'),
    ]

    if Pizza.get() == 1:
        pizza = StringVar()
        pizza.set('Cheese')
        for choice, option in toppings:
            Radiobutton(root, text=choice, variable=pizza, value=option, command=lambda: clicked(pizza.get())).pack(
                anchor=W)
    else:
        pass


def dishes():
    la = Label(root, text='Choose your favorite chicken dish').pack()
    dish = [
        ('Lemongrass Chicken', 'Lemongrass Chicken'),
        ('Basil Chicken', 'Basil Chicken'),
        ('Ginger Chicken', 'Ginger Chicken'),
        ('Chicken Hot Pot', 'Chicken Hot Pot'),
    ]

    if Chicken.get() == 1:
        chicken = StringVar()
        chicken.set('Lemongrass Chicken')
        for choice, option in dish:
            Radiobutton(root, text=choice, variable=chicken, value=option, command=lambda: clicked(chicken.get())).pack(
                anchor=W)
    else:
        pass


PizzaButton = Checkbutton(root, variable=Pizza,
                          text="Pizza",
                          onvalue=1,
                          offvalue=0,
                          command=pizza_options).pack()

# PizzaButton.place(anchor=NW)

ChickenButton = Checkbutton(root, text="Chicken",
                            variable=Chicken,
                            onvalue=1,
                            offvalue=0,
                            command=dishes).pack()
# ChickenButton.place(relx=1, x=-200, y=0, anchor=NE)

mainloop()
