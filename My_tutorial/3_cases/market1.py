from collections import OrderedDict

items_list = {}
new_dictionary = {}


class Market:
    def add_items(self, name, price):
        items_list[name] = price

    # def add_items(self):
    #     while True:
    #         prodact = input("Input goods name :")
    #         if prodact == "q":
    #             break
    #         price = input("Input price of goods :")
    #         items_list[prodact] = price

    def get_list(self):
        # for i in sorted(items_list):
        # print((i, items_list[i]))
        # print(" ")
        dict1 = OrderedDict(sorted(items_list.items()))
        print(dict1)

    def get_list_1(self):
        sortedLis1 = sorted(items_list.keys())
        for sortedKey in sortedLis1:
            for key, value in items_list.items():
                if key == sortedKey:
                    new_dictionary[key] = value
        print(new_dictionary)


market = Market()
# market.add_items()

# market.get_list_1()
market.add_items("Banana", 10)
market.add_items("Ananas", 20)
market.get_list1()
# assert market.get_list() == {"Ananas": 20, "Banana": 10}
