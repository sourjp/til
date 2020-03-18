import datetime
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['test_database']

stack1 = {
    'name': 'customer1',
    'pip': ['python', 'java', 'go'],
    'info': {'os': 'mac'},
    'date': datetime.datetime.utcnow()
}
stack2 = {
    'name': 'customer2',
    'pip': ['python', 'java'],
    'info': {'os': 'windows'},
    'date': datetime.datetime.utcnow()
}

db_stacks = db.stacks
stack_id = db_stacks.insert_one(stack1).inserted_id
print(stack_id, type(stack_id))
from bson.objectid import ObjectId
print('#############')
print(db_stacks.find_one({'_id': stack_id}))

# idはstringで見ているのではなく 'bson.objectid,Objectid'
# 要はdynamoDBのobject IDでないと検索できないのでNone
#str_stack_id = '5e4151d29feacc9011bd3e60'
#print(db_stacks.find_one({'_id': ObjectId(str_stack_id)}))
print('#############')
print(db_stacks.find_one({'name': 'customer1'}))

print('#############')
stack_id  = db_stacks.insert_one(stack2).inserted_id
for stack in db_stacks.find():
    print(stack)

now = datetime.datetime.utcnow()
for stack in db_stacks.find({'date': {'$lt': now}}):
    print(stack)

db_stacks.find_one_and_update(
    {'name': 'customer1'}, {'$set': {'name': 'YYY'}}
)
print(db_stacks.find_one({'name': 'YYY'}))

db_stacks.delete_one({'name': 'YYY'})
print(db_stacks.find_one({'name': 'YYY'}))


'''
brew services start mongodb-community

mongod --dpath .
'''