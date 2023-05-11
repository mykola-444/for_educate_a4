from collections import OrderedDict


class Market:
    def __init__(self):
        self.items_list = {}

    def add_items(self, item_name, item_price):
        self.items_list[item_name] = item_price

    def get_list(self):
        # for i in sorted(self.items_list):
        #    print((i, self.items_list[i]))
        dict1 = OrderedDict(sorted(self.items_list.items(), key=lambda w: w[0]))
        print(dict1)
        return dict1


class NewMarket(Market):
    def remove_items(self, item_name):
        del market.items_list[item_name]


market = Market()
market.add_items("Melon", 17)
market.add_items("Banana", 10)
market.add_items("Cherry", 25)
market.add_items("Ananas", 20)
print(market.items_list)
assert market.get_list() == {"Banana": 10, "Ananas": 20, "Melon": 17, "Cherry": 25}

new_market = NewMarket()
new_market.remove_items('Cherry')
assert market.get_list() == {"Banana": 10, "Ananas": 20, "Melon": 17}
