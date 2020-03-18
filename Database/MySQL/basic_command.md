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

    - LIMITATION
        - NOT NULL
        - DEFAULT 0 // DEFAULT設定がないCOLUMNはNULL
        - PRIMARY KEY(COLUMN)

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
    - DEFAULT設定がある場合はROWにDEFAULTとかく

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

# TABLE COPY
    INSERT INTO <TABLE1> SELECT <COLUMN> FROM <TABLE2>;
    - GROUP BYなども併用して違うTABLEのSELECT結果を、他のTABLEに挿入できる

    INSERT INTO <TABLE1> SELECT <C1>, <C2>, ... FROM <TABLE2> WHERE <RULE1>;

# DELETE
    DELETE FROM <TABLE>;
    DELETE WHERE <RULE> FROM <TABLE>;
    - TABLE自体の削除はDROP
    - DELETEはTABLEから該当の行を削除するため、SELECTのようにカラムを指定してもエラーになる

# TRUNCATE
    TRUNCATE <TABLE>;
    - TABLEのデータを全て削除する方法。
    - DELETEは処理が遅い扱いなので、全体を消すならWHEREを使いたい場合にした方が良い
    - 全体の場合はTRUNCATEが良い

# UPDATE
    UPDATE <TABLE> SET <COLUMN> = <DATA> WHERE <RULE>;
    - setで指定したカラムのデータを変更する、WHERE指定がないと全部変えちゃうので注意

    START TRANSACTION;
    UPDATE <TABLE> SET <C1> = <D1>, <C2> = <D2> WHERE <RULE>;
    COMMIT;

# VIEW
    CREATE VIEW TableName(column1, column2) AS SELECT column1, column2 FROM TableName;
    - VIEWを作成する際は後述のTABLEと同じcolumn位置にする
    - AS以降は通常のSELECT文と同じ

# SUB QUERY
    SELECT c1, c2 FROM(SELECT c1, c2 FROM table) AS as_table;
    - FROM区TABLEを作成してそれを元に返す
    - この中身がサブクエリと呼ばれる場所
    - 最後にASがないと出力結果のtableが何か定まらないためつけること

# SCALA QUERY
    SELECT c1, c2, c3 FROM t1 WHERE c1 > (SELECT AVG(c1) FROM t1);    

    - 例えば、次のよな方法ではerrorが出る
    SELECT c1, c2, c3 FROM t1 WHERE c1 > AVG(c1);
        ERROR 1111 (HY000): Invalid use of group function

# CORRELATED SUBQUERY
    SELECT c1, c2, c3 FROM t1 AS S1 WHERE c3 > (SELECT AVG(c3) FROM t1 AS S2 WHERE S1.c1 = S2.c1 GROUP BY c1);

# 算術関数
    ABS()
    MOD()
    ROUND()

# 文字列関数
    CONCAT(c1, c2) -> c1c2 // str+strのことで、Postgresなら c1 || c2 とかく
    LENGTH()
    LOWER()
    UPPER()
    REPLACE(対象文字、置換前の文字、置換後の文字)
    SUBSTRING(文字 FROM スタート文字数 FOR 文字数) // SUBSTRING(str1 FROM 3 FOR 2)なら3文字から2文字取り出す

# 日付関数
    SELECT CURRENT_DATE; で現在の日付が取れる
    SELECT CURRENT_TIME; で現在の時刻が取れる
    SELECT CURRENT_TIMESTAMP; で上二つの情報が取れる

    EXTRACTを利用することでTIMESTAMPを分解できる
        SELECT CURRENT_TIMESTAMP,
            EXTRACT(YEAR FROM CURRENT_TIMESTAMP) AS year, EXTRACT(MONTH FROM CURRENT_TIMESTAMP) AS month, EXTRACT(DAY FROM CURRENT_TIMESTAMP) AS day, EXTRACT(HOUR FROM CURRENT_TIMESTAMP) AS hour, EXTRACT(MINUTE FROM CURRENT_TIMESTAMP) AS minute, EXTRACT(SECOND FROM CURRENT_TIMESTAMP) AS second;

# 変換関数
    CAST(変換前の値 AS 変換後の型); で変換できる
    COALESCE(NULLを含んだ列, NULLの変換したい文字列)

# 述語
    LIKE
        テーブルの検索のことで、検索文字列の書き方で３種類の評価がある
        下記の例ならdddが一番先頭から、もしくはどこかで一致、もしくは最後だけ一致といった評価の仕方

        前方一致
            SELECT * FROM Sample WHERE str LIKE 'ddd%'
        中間一致
            SELECT * FROM Sample WHERE str LIKE '%ddd%'
        後方一致
            SELECT * FROM Sample WHERE str LIKE '%ddd'
    
    BETWEEN
        間のことでA AND Bとかく。これは <= >= と同じ意味なので注意。
        要はWHERE a >= 100 AND a <= 200　とWHERE a BETWEEN 100 AND 200 は同じ意味

    IS NULL, IS NOT NULL
        NULLは算術ではないため = が使えない。なのでWHEREではこれを使う
        WHERE a IS NULL;

    IN, NOT IN
        一致文字を指定したいときにORを重ねると大変なので、これを使う
        WHERE a IN (100, 200, 300);
    
        またサブクエリをINに入れることができる
        要はINのOR条件の候補として、クエリを使って出した出力結果を用いるということ

    EXISTS, NOT EXISTS
        常に相関サブクエリを引数として、データの有無を確認する

# CASE
    単純CASEと検索CASEの２種類があるが、検索CASEは単純CASEの機能を包含している

    SELECT table.
        CASE WHEN xx
             THEN yy
             WHEN xx
             THEN yy
             ELSE NULL
        END AS zz
    FROM table;

    ELSE　NULLはデフォルト動作だが明示的に書くほうが好ましい。(NULLがNOならELSE 0など。)
    CASE ... のあとはENDで終わること



