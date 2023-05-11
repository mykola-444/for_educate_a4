import re
import turtle

import requests
from bs4 import BeautifulSoup

response = requests.get('https://httpbin.org/forms/post')
page = BeautifulSoup(response.text)
form = page.find('form')

print({field.get('name') for field in form.find_all(re.compile('input|textarea'))})


# {'delivery', 'topping', 'size', 'custemail', 'comments', 'custtel','custname'})


def go_snowy(len):
    if len < 50:
        turtle.forward(len)
    else:
        go_snowy(len / 3)
        turtle.left(60)
        go_snowy(len / 3)
        turtle.right(120)
        go_snowy(len / 3)
        turtle.left(60)
        go_snowy(len / 3)

turtle.speed(200)
go_snowy(200)
turtle.right(120)
go_snowy(200)
turtle.right(120)
go_snowy(200)
