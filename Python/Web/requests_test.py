import requests


payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=payload)
print(r.status_code)
print(r.text)
print(r.json())
# r = requests.get('http://httpbin.org/get', params=payload, timeout=0.001)


r = requests.post('http://httpbin.org/post', data=payload)
print(r.status_code)
print(r.text)
print(r.json())


r = requests.put('http://httpbin.org/put', data=payload)
print(r.status_code)
print(r.text)
print(r.json())


r = requests.delete('http://httpbin.org/delete', data=payload)
print(r.status_code)
print(r.text)
print(r.json())
