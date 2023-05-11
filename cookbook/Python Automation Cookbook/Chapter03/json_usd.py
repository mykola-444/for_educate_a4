import requests

result = requests.get('https://jsonplaceholder.typicode.com/posts')
print(result)
print(result.json()[-1])

new_post = {'userId': 10, 'title': 'a title', 'body': 'something something'}

result1 = requests.post('https://jsonplaceholder.typicode.com/posts', json=new_post)
print(result1)
print(result1.json())
print(result1.headers['Location'])

result2 = requests.get('https://jsonplaceholder.typicode.com/posts/2')
print(result2.json())

#GET and DELETE don't require data, while PATCH, PUT, and POST do require data
update = {'body': 'new body'}
result3 = requests.patch('https://jsonplaceholder.typicode.com/posts/2', json=update)
print(result3.json())
print(result3.json())

#page 89
