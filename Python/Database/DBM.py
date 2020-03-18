import dbm
import os 

os.chdir('./Database')

with dbm.open('cache.db', 'c') as db:
    db['key1'] = 'value1'
    db['key2'] = 'value2'
    # only string, not int

with dbm.open('cache.db', 'r') as db:
    print(db.get('key1'))