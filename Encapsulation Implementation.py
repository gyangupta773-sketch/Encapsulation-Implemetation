class Computer:

    def __init__(self):
        self.__maxprice = 650   # private variable

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price   # correct private variable


c = Computer()
c.sell()

# Change the price directly (this will NOT change the real private variable)
c.__maxprice = 1000
c.sell()

# Using setter function (
c.setMaxPrice(1000)
c.sell()


class Laptop:

    def __init__(self):
        self.__maxprice = 900   # private variable

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    @property
    def maxprice(self):
        return self.__maxprice


l = Laptop()
l.sell()