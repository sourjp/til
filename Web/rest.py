import urllib.request
import json


url = 'http://httpbin.org/get'
with urllib.request.urlopen(url) as f:
    #print(f.read())
    #print(f.read().decode('utf-8'))
    r = json.loads(f.read().decode('utf-8'))
    print(type(r))
    print(r)
    #print(r['headers']['Host'])

print('---')
payload = {'key1': 'value1', 'key2': 'value2'}
url2 = 'http://httpbin.org/get' + '?' + urllib.parse.urlencode(payload)
#print(url2)
with urllib.request.urlopen(url2) as f:
    r = json.loads(f.read().decode('utf-8'))
    print(type(r))
    print(r)

print('---')
payload2 = json.dumps(payload).encode('utf-8')
req = urllib.request.Request(
    'http://httpbin.org/post', data=payload2, method='POST')

with urllib.request.urlopen(req) as f:
    r = json.loads(f.read().decode('utf-8'))
    print(type(r))
    print(r)


print('---')
payload3 = json.dumps(payload).encode('utf-8')
req2 = urllib.request.Request(
    'http://httpbin.org/put', data=payload3, method='PUT')

with urllib.request.urlopen(req2) as f:
    r = json.loads(f.read().decode('utf-8'))
    print(type(r))
    print(r)


print('---')
payload4 = json.dumps(payload).encode('utf-8')
req3 = urllib.request.Request(
    'http://httpbin.org/delete', data=payload4, method='DELETE')

with urllib.request.urlopen(req3) as f:
    r = json.loads(f.read().decode('utf-8'))
    print(type(r))
    print(r)



'''
GET     参照
POST    新規
PUT     更新
DELETE  削除
'''