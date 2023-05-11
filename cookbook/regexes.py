import re

print(re.search(r'LOG', 'LOGS'))
print(re.search(r'LOG', 'SOME LOGS'))
print(re.search(r'^LOG', 'LOGS'))  # only at the start of the string. Note the ^ character
print(re.search(r'LOG$', 'SOME LOG'))  # only at the end of the string. Note the $ character
STRING = 'something in the things she shows me'
match = re.search(r'thing', STRING)
print(STRING[:match.start()], STRING[match.start():match.end()], STRING[match.end():])
match1 = re.search(r'\bthing', STRING)
print(STRING[:match1.start()], STRING[match1.start():match1.end()], STRING[match1.end():])
print(re.search(r'[0123456789-]+', 'the phone number is 1234-567-890'))
print(re.search(r'[0123456789-]+', 'the phone number is 1234-567-890 ').group())
match3 = re.search(r'[0123456789-]+', 'the phone number is 1234-567-890')
print([int(n) for n in match3.group().split('-')])
print(re.search(r'\S+@\S+', 'my email is email.123@test.com').group())
print(re.search(r"(^[azA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", 'email.123@test.com'))
