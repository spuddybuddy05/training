class menuItems:
    def __init__(self, name, price):
        self.name=name
        self.price=price


    def displayItem(self):
        print (self.name, " costs $", self.price)

one = menuItems ("Chicken Alfredo", 14.99)
two = menuItems ("Spaghetti with Meatballs", 12.99)
three = menuItems ("Baked Ziti", 17.99)
four = menuItems ("Baked Carbonara", 54.99)

one.displayItem()
two.displayItem()
three.displayItem()
four.displayItem()