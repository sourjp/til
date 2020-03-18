''' Configparserの代わりにYAML形式で保存する場合

pip install pyyaml

import yaml

YAMLファイルを読み込む際には脆弱性の観点からLoaderオプションを使うことを推奨
また読み込み時に型が全てStringであることに注意

https://github.com/yaml/pyyaml/wiki/PyYAML-yaml.load(input)-Deprecation

'''

import yaml

with open('parse.yaml', 'w') as yaml_file:
    yaml.dump({
        'Server': {
            'ip': '192.168.0.1',
            'port': 3306
        },
        'User1': {
            'id': 1,
            'name': 'user1',
            'attend': False
        }
    }, yaml_file)

with open('parse.yaml', 'r') as yaml_file:
    config = yaml.load(yaml_file, Loader=yaml.BaseLoader)
    print(config['Server']['ip'])
    print(config['Server']['port'], type(config['Server']['port']))
    print(config['User1']['attend'], type(config['User1']['attend']))
