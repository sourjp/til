# Pickle
通常データをファイルに書き込むのであれば file opneして書き込めば良いが、
stringが対象になる
dictやtupleなど文章ではない型を保存したい場合はpickle moduleを使うことで
binary dataとして保存できる

```.py
import pickle

test = {'t1': 1}
with open('test.bin', mode='wb') as f:
    pickle.dump(test, f)

```

読み込むときは loadを使う

```.py 
with open('test.bin, mode='rb') as f:
    data = pickle.load(f)
    print(data)
    # {'t1': 1}
```