import requests

r = requests.get('http://127.0.0.1:5000/employee/sourjp')
print(r.text)

r = requests.post('http://127.0.0.1:5000/employee', data={'name': 'sourjp'})
print(r.text)

r = requests.put('http://127.0.0.1:5000/employee', data={'name': 'sourjp', 'new_name': 'souren'})
print(r.text)

r = requests.delete('http://127.0.0.1:5000/employee', data={'name': 'sourjp'})
print(r.text)