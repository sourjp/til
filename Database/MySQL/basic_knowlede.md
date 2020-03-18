# 標準SQL
    どのソフトウェアでも標準利用ができるものが標準SQL

# SQLの種類
    DDL - Data Definition Language(データ定義言語)
        CREATE  ：データベースやテーブルなどを作成する
        DROP    ：データベースやテーブルなどを削除する
        ALTER   ：データベースやテーブルなどの構成を変更する

    DML - Data Manipluration Language(データ操作言語)
        SELECT  :テーブルから行を検索する
        INSERT  :テーブルに新規行を登録する
        UPDATE  :テーブルの行を更新する
        DELETE  :テーブルの行を削除する

    DCL - Data Control Language(データ制御言語)
        COMMIT  :データベースに対して行なった変更を確定する
        ROLLBACK:データベースに対して行なった変更を取り消す
        GRANT   :ユーザに操作の権限を与える
        REVOKE  :ユーザから操作の権限を奪う

# 文法について
    必ず最後は；で終了する
    大文字・小文字の区別はない

# DATABASEの構造
    DATABASEという全体の枠があり、そこにTABLEが配置される
    各TABLEにはカラム・列単位にデータの種類を定義し、
    row・行単位にデータが設定されている

# 覚えるDATAの型
    ソフトウェアによって異なるため、詳細はドキュメント
    標準的には次を覚える
    ・INTEGER
        整数型
    ・CHAR(X)
        文字数もしくはbyte数を定義するため固定長文字列と呼ばれ、足りないと半角スペースで埋められる
        注意点はbyte数だと、文字コードによって変わる(ASCIIなら1byteだし、utf-8なら3byteなど)
        Xで量の制約を課す
    ・VARCHAR(X)
        可変長文字列。stringと覚えると楽。
    ・DATE
        ソフトウェアによるが年月日が基本で、あとは時分秒まで含まれる

# 覚える制約
    テーブルにデータを入力する際の制約
    ・NOT NULL
        必ずデータを埋める必要がある
    ・PRIMARY KEY
        主キーとも呼ばれる。一つだけ指定でき、これを指定すればその行のデータを全て取得できる。
        つまり必ず一意であることが求められる

# コメントアウト
    一文でのコメントアウトは「-- xxx」
    複数行では「/* xxx */」

# 真理値
    TRUE, FALSE, UNKNOWN の３種類がSQLでは用意されている
    これはNULLのデータに対してWHEREを用いた場合に、判断ができないのでUNKNOWNという結果になる
    このようにデータとして処理が難しいためNULLはTABLE定義にNOT NULLを含めて避けた方が良い

# 関数
    COUNT   ：テーブルのレコード数（行数）を数える
    SUM     ：テーブルの数値列のデータを合計する
    AVG     ：テーブルの数値列のデータを平均する
    MAX     ：テーブルの任意列のデータの最大値を求める
    MIN     ：テーブルの任意列のデータの最小値を求める

# SQL分の順番
    SELECT -> FROM -> WHERE -> GROUP BY -> HAVING -> ORDER BY
    
    内部的に動作の順番は FROM -> WHERE -> GROUP BY -> HAVING BY -> SELECT -> ORDER BYと行った流れになる
    この順番があることで、SELECTでASによる別名をコラムに付与したとしても、GROUP BYでは選択できない。(SELECT処理があとだから)
    そのためORDER BYならASによる指定した名前が使える

    e.g.
    SELECT <COLUMN1>, AVG(<COLUMN2>) FROM <TABLE> GROUP BY <COUMN1> HAVING AVG(<COLUMN2>) >= 2500;

# ビュー機能
    ビューはテーブルのデータを持つのではなく、SELECT文を保持させておくもの
    つまりテーブルを別途記録しているわけではなく読み出されるびたにSELECTを実行し結果を返している
    ビューで作成したTABLEを参照すると、元々のSELECT文を実行し、そこからVIEW TABLE向けのSELECTが実行される
    多段VIEWも構築できるが、パフォーマンスの問題があるため推奨されない
    またVIEW TABLE作成時はORDER BYは使えない。
    情報の出力や集約はviewでできるが集約の場合はTABLEの変更はできない、、
    結局VIEWはSELECTを実施しているので、本来のTABLEにどのような反映をすればいいのかわからないため

# サブクエリ
    ビュー機能はTABLEとして保持するが、サブクエリの場合は使い捨てになる

# スカラサブクエリ
    必ず１行一列だけの戻り値を返すクエリ
    例えばWHERE区に集約関数は利用できないが、スカラサブクエリを代わりとして使うことができる(AVGなど)
    単一のデータを返すと言う特徴から、どの場所に当てはめることができる
    一方で複数の結果を消すクエリにしてしまうと、それはただのサブクエリであり複数の答えを返してしまうので使えない

# 相関サブクエリ
    クエリとして出力した結果、相関して出力を返したい場合に使う

    
INSERT INTO SampleMath(m, n, p) VALUES (500, 0, NULL);
INSERT INTO SampleMath(m, n, p) VALUES (-180, 0, NULL);
INSERT INTO SampleMath(m, n, p) VALUES (NULL, NULL, NULL);
INSERT INTO SampleMath(m, n, p) VALUES (NULL, 7, 3);
INSERT INTO SampleMath(m, n, p) VALUES (NULL, 5, 2);


INSERT INTO SampleMath(m, n, p) VALUES (NULL, 4, NULL);
INSERT INTO SampleMath(m, n, p) VALUES (8, NULL, 3);
INSERT INTO SampleMath(m, n, p) VALUES (2.27, 1, NULL);
INSERT INTO SampleMath(m, n, p) VALUES (5.555,2, NULL);
INSERT INTO SampleMath(m, n, p) VALUES (NULL, 1, NULL);
INSERT INTO SampleMath(m, n, p) VALUES (8.76, NULL, NULL);

COMMIT;
NULL); NULL); NULL);
   