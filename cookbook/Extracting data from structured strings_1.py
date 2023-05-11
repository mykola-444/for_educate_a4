from decimal import Decimal

import delorean
from parse import parse

LOG = '[2018-05-06T12:58:00.714611] - SALE - PRODUCT: 1345 - PRICE: $09.99'
FORMAT = '[{date}] - SALE - PRODUCT: {product} - PRICE: ${price}'
FORMAT1 = '[{date:ti}] - SALE - PRODUCT: {product:d} - PRICE: ${price:05.2f}'
result = parse(FORMAT, LOG)
result1 = parse(FORMAT1, LOG)
print(result)
print(result1)


class PriceLog(object):
    def __init__(self, timestamp, product_id, price):
        self.timestamp = timestamp
        self.product_id = product_id
        self.price = price
        print(timestamp, product_id, price)

    def __repr__(self):
        return '<PriceLog ({}, {}, {})>'.format(self.timestamp,
                                                self.product_id,
                                                self.price)

    @classmethod
    def parser1(cls, text_log):
        '''
        Parse from a text log with the format
        [<Timestamp>] - SALE - PRODUCT: <product id> - PRICE: $<price>
        to a PriceLog object
        '''

        def price(string):
            return Decimal(string)

        def isodate(string):
            return delorean.parse(string)

        FORMAT = ('[{timestamp:isodate}] - SALE - PRODUCT: {product:d} - PRICE: ${price:price}')
        formats = {'price': price, 'isodate': isodate}
        result = parse(FORMAT, text_log, formats)
        return cls(timestamp=result['timestamp'],
                   product_id=result['product'],
                   price=result['price'])

log1 = '[2018-05-06T14:58:59.051545] - SALE - PRODUCT: 827 - PRICE: $22.25'
PriceLog.parser1(log1)
