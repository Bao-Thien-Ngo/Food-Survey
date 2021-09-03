from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('650x400')
root.title("Menu Survey")
Pizza = IntVar()
Chicken = IntVar()
Curry = IntVar()


frame1 = LabelFrame(root, text='Which food do you want for lunch?', bg='silver')
frame1.grid(row=1,column=2)

frame2 = LabelFrame(root, text='Choose your favorite toppings', bg='white')
frame2.grid(row=5, column=1)

frame3 = LabelFrame(root, text='Choose your favorite chicken dish', bg='white')
frame3.grid(row=5, column=2)

frame4 = LabelFrame(root, text='Choose your favorite curry dish', bg='white')
frame4.grid(row=5, column=3)


def on_closing():
    if messagebox.askokcancel("Quit", "Thank you for your opinion. Do you want to quit?"):
        root.destroy()


def clicked(value, frame):
    lab = Label(frame, text="You select " + value).pack()
    b2 = Button(frame, text="Exit", command=on_closing).pack()


def pizza_options():
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
            Radiobutton(frame2, text=choice, variable=pizza, value=option, command=lambda: clicked(
                pizza.get(), frame2)).pack(anchor=NW)
    else:
        pass


def dishes():
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
            Radiobutton(frame3, text=choice, variable=chicken, value=option, command=lambda: clicked(
                chicken.get(), frame3)).pack(anchor=NW)
    else:
        pass


def curries():
    dish = [
        ('Red Curry', 'Red Curry'),
        ('Yellow Curry', 'Yellow Curry'),
        ('Green Curry', 'Green Curry'),
        ('Jungle Curry', 'Jungle Curry'),
    ]

    if Curry.get() == 1:
        curry = StringVar()
        curry.set('Red Curry')
        for choice, option in dish:
            Radiobutton(frame4, text=choice, variable=curry, value=option, command=lambda: clicked(
                curry.get(), frame4)).pack(anchor=NW)

    else:
        pass


PizzaButton = Checkbutton(frame1, variable=Pizza,
                          text="Pizza",
                          onvalue=1,
                          offvalue=0,
                          command=pizza_options).grid(row=0, column=1, padx=5, pady=5)

ChickenButton = Checkbutton(frame1, text="Chicken",
                            variable=Chicken,
                            onvalue=1,
                            offvalue=0,
                            command=dishes).grid(row=0, column=2, padx=5, pady=5)

CurryButton = Checkbutton(frame1, text="Curry",
                          variable=Curry,
                          onvalue=1,
                          offvalue=0,
                          command=curries).grid(row=0, column=3, padx=5, pady=5)


root.mainloop()
