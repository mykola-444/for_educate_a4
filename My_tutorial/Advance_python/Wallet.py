class Purse:
    def __init__(self, currency, name='Unknown'):
        if currency not in ('USD', 'EUR'):
            raise ValueError
        self.__money = 0.00
        self.currency = currency
        self.name = name

    def top_up_balance(self, how_many):
        self.__money = self.__money + how_many
        return how_many

    def top_down_balance(self, how_many):
        if self.__money - how_many < 0:
            print("Not enough money")
            raise ValueError('Not enough money')
        self.__money = self.__money - how_many
        return how_many

    def info(self):
        print(self.__money)

    def __del__(self):
        print('Wallet del')


x = Purse('USD')
y = Purse('EUR', 'Mykola')
y.top_up_balance(10)
x.top_up_balance(y.top_down_balance(7))

x.info()
y.info()
