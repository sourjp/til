''' Configparserによるconfigfile作成 iniの場合
https://docs.python.org/ja/3/library/configparser.html

import configparser

configファイルのセクションをdictと同じように設定できる。
読み込みに注意が必要で、String型で記入されてしまうので型指定はgetを使う方がいい

getboolean()
getint()
getfloat()

'''


import configparser

config = configparser.ConfigParser()
config['Server'] = {'ip': '192.168.0.1 ',
                    'port': 3306}
config['User1'] = {'userid': 1,
                   'username': 'user1',
                   'password': 'pass1'}
config['User2'] = {'userid': 1,
                   'username': 'user1',
                   'password': 'pass1',
                   'attend': 'False'}

with open('parse.ini', 'w') as configfile:
    config.write(configfile)


config.read('parse.ini')

print(config['Server'])
print(config['Server']['ip'])

for key in config['User1']:
    print(key)

print(config['User2']['attend'], type(config['User2']['attend']))
print(config['User2'].getboolean('attend'),
      type(config['User2'].getboolean('attend')))

