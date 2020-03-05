# DATABASEの作成
    CREATE DATABASE <DATABASE NAME>;

# 指定したDATABASEにアクセスする方法
    # mysql -u root -p -D shop

# TABLEの作成
    CREATE TABLE <TABLE NAME>
    (<Col1> <DATA TYPE> <LIMITATION>,
     <Col2> <DATA TYPE> <LIMITATION>,
     <Col3> <DATA TYPE> <LIMITATION>,
     ...    
     <LIMITATION1 OF TABLE>, <LIMITATION2 OF TABLE>);

# TABLEの削除
    DROP TABLE <TABLE NAME>:

# 列を追加する
    ALTER TABLE <TABLE NAME> ADD COLUMN <DEFINITION OF COLUMN>;
    - <DEFINITION OF COLUMN> -> shohine_name VARCHAR(20)

# 列を削除する
    ALTER TABLE <TABLE NAME> DROP COLUMN <COLUMN NAME>;

# TRANSACTIONを開始する
    START TRANSACTION;

# TRANSACTIONを確定する
    COMMIT;

# DATAを挿入する
    INSERT INTO <TABLE NAME> VALUES (ROW1, ROW2, ROW3, ...);

# TABLE名を変更する
    RENAMTE TABLE <BEFOR TABLE NAME> to <AFTER TABLE NAME>;

# TABLEの確認
    SELECT <COLUMN NAME>, ... FROM <TABLE NAME>;

# COLUMN NAMEをASによる別名設定
    SELECT <COLUMN NAME> AS <TEMPORARY COLUMN NAME>, ... FROM <TABLE NAME>;
    - <AS NAME> を'' or ""(e.g. '商品名') で日本語にできる

# 出力に定数を追加
    SELECT <ADDITIONAL ROW DATA> AS <TEMPORALRY COLUMN NAME>, ... FROM <TABLE NAME>;

# 重複出力を止める
    SELECT DISTINCT <COLUMN NAME> FROM <TABLE NAME>;
    - DISTINCは必ず先頭にくる
    - 複数のCOLUMN NAMEがあるときは各ROWの全てのCOLUMNが重複している場合にまとめる

# 行/ROWを指定する方法
    SELECT <COLUMN NAME> FROM <TABLE NAME> WHERE <ROW CONDITION>;
    - 内部動作は、まずWHEREでROWを絞って、SELECTでCOLUMNを削る
    - ROW CONDITION:
        =          : column1 = 100, column2 = '商品'
        <> (否定)   : column1 <> 500 (column1の500以外のデータ) 
        >=, >, <=, < : 比較演算子として用いる。また文字比較の場合は数字含めて辞書順(CHAR(3) > CHAR(22) など)
        IS NOT NULL : column1 IS NOT NULL
        IS NULL     : column2 IS NULL

# 演算をする方法
    SELECT <COLUMN NAME> <CALCURATION> FROM <TABLE NAME>; 
    - CALCURATION:
        + : column1 + column2
        - : (column1 - column2) * 2
        * : column1 * 2
        / : column1 / 10 (/0はNULL)
        ただし、NULLが含まれる計算は全てNULL

# NOT演算子
    SELECT <COLUMN NAME> FROM <TABLE NAME> WHERE NOT <ROW CONDITION>
    - WHERE条件の否定をするが、演算子を変えればいいだけなのでなるべく使わない方がいい
    - SELCT column1 FROM table1 WHERE NOT column2 < 100(これは、column2 >= 100と同じ意味)

# AND / OR演算子
    SELECT <COLUMN NAME> FROM <TABLE NAME> WHERE <ROW CONDITION> AND/OR <ROW CONDITION>
    - AND / ORで条件をより複雑にできる
    - 注意点として、AND / ORを両方使うとANDが優先されるため ( )を使う方が良い
        - ... WHERE rule1 AND rule2 OR rule3
            これは (rule1 AND rule2) OR rule3 のWHEREになってしまう
        - ... WHERE rule1 AND (rule2 OR rule3)
            これは (rule1 AND rule2) OR (rul1 AND rule3) のWHEREにすることができる

# COUNT関数
    SELECT COUNT(<COLUMN NAME>), ... FROM <TABLE NAME>;
    - COUNT(*)でデータの量がわかる
    - COUNTの時は表の最大値をだす、指定した場合はNULLの数は引いて出す

# SUM関数
    SELECT SUM(<COLUMN NAME>), ... FROM <TABLE NAME>;
    - *はNG
    - NULLは計算前に除外されるのでUNKNOWNにはならない

# AVG関数 
    SELECT AVG(<COLUMN NAME>), ... FROM <TABLE NAME>;
    - *はNG
    - この時NULLがデータにある場合は、全体の個数から引いて割り算を行う。（８個中２個がNULLなら、6でABGを出す）

# MAX/MIN関数 
    SELECT MAX(<COLUMN NAME>), MIN(<COLUMN NAME>) ... FROM <TABLE NAME>;
    - *はNG
    - NULLは無視
    - MAX/MINはINTEGERではなくても、STRINGやDATEでもOK。なぜなら辞書順にするなど順序を定義できるから

# 関数とDISTINTの組み合わせ
    SELECT COUNT(DISTINCT <COLUMN NAME>) FROM Shohin;

# GROUP BYによる分割
    SELECT <COLUMN1> GROUP BY <COLUMN1>
    - SELECT分で指定したCOLUMN名で、テーブルの表示の分割を行う。例えばCOLUMN1がデータ８個で3種類なら、3種類に集約して表示する。
    - GROUP BYの場合はNULLも一つのデータとしてカウントする
    - GROUP BYで指定したCOLUMNのみ、SELECTで指定できる。GROUP BYで分割した時に、関係ないCOLUMNでは表示内容が定まらないため

    SELECT <COLUMN1>, COUNT(*) GROUP BY < COLUMN1>

# HAVINGによるフィルタリング
    SELECT <COLUMN>, ... FROM <TABLE> GROUP BY <COLUMN> HAVING <RULE>
    - WHEREはレコードに対するフィルタリングであるため、GROUP BYによるフィルタリング後は対象とならない
    - HAVINGはSELECTで出力される結果に対してFILTERINGを行える
    - HAVING を利用することで集約キーのフィルタリングはWHEREと同じようにフィルタリングできるが、それはWHEREでするべき
      先にWHEREで絞ったほうがレスポンスがいいし、目的にそう(HAVINGはGROUP BYのフィルタリングだから)

        e.g.
        SELECT <COLUMN> FROM <TABLE> ORDER BY <COLUMN>;
        SELECT <COLUMN> FROM <TABLE> GROUP BY <COLUMN> HAVING <COLUMN> = '<rule>';

# ORDER_BYによるSORT
    SELECT <COLUMN> FROM <TABLE> ORDER BY <COLUMN>;
    - デフォルトではORDERで指定したCOLUMNで昇順にならぶ
    - ASCが昇順の意味だが、デフォルト動作なのであまり使わない

    SELECT <COLUMN> FROM <TABLE> ORDER BY <COLUMN> DESC;
    - 指定したCOLUMNで降順にならぶ
    - NULLは先頭か末尾かのルールはない

    - また、ORDER BYではSELECTで指定していないものも使える
    - 他にも関数、例えばCOUNT(*)を使って並び替えもできる
