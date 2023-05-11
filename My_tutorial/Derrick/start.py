import requests, json

responce= requests.get( 'https://26607.wayscript.io' )
print(responce.json().get('date'))

api_key = 'MJKCIOBHIT6BESWBRNXM6ZUPGUVGPBYW'

header = {'X-TOKEN': api_key}
responce= requests.get( 'https://calendly.com/api/v1/users/me/event_types', headers=header)
print(responce.json())
print(responce.json().get('data')[0].get('attributes').get('color'))
