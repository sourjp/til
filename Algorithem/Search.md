# Search
    データを探す方法のことで、リストから効率よく必要なデータにたどり着ける方法を考える

# どんな種類？
## 線形探索 O(n)
    線形探索はデータを左から１つずつ比較して探索すること。
    例えば[1 , 3, 5, 6, 10, 2]というリストで、2を探すなら左から順番に検索していく。

    計算量は O(n) となる。
    ただしリストのデータがバラバラであっても確実にたどり着けるため、データの入れ替えが激しかった場合は適しているかもしれない。また実装が単純なので容易。

## 二分探索 O(logn)
    データを二分割にして比較し、左右どちらか近い方をさらに二分割と、繰り返して探索すること。
    例えば[1, 2, 3, 4, 5, 6]として4を探索するならば、まず3で分割して、3 < 4 なので右側の[4, 5, 6]で探索する。真ん中は5なので5 > 4なので左側を確認すると一つしかないのでたどり着く。
    つまり、前提としてデータが「ソート」されている必要があるので注意が必要。
    ソートの計算量によっては線形探索も視野に入れていかもしれない。
    結局、検索することが多いなら探索の計算量が少ない仕組みの方がいいし、検索が少なくてデータの入れ替えが激しいならソートの計算量が少ない方法にして線形探索を導入するといいかもしれない。

    計算量は O(log n)tなる。
    これは二分割するということから log[2]n が繰り返されることがわかる。