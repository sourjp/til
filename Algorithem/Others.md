# Others?
    未分類のアルゴリズムはこちら

# どんな種類?
## ユークリッドの互除法
    二つの数字の最大公約数を求める方程式
    A % B = Cならば、B % C = Dと余りで割り算をしていく方法
    これによると、最終的に０の結果になる。
    つまり N % N = 0 という結果になった時のNが最大公約数である。
    これは大前提として、最初のAとBの二つの数字に公約数があるという前提の結果。
    つまり０にならないということは公約数が存在しないということがわかる。

## フェルマーテスト
    素数の求め方で、素数には以下の特徴がある
    素数がPならば、 N < Pである限り　N^P mod P = Nである
    簡単にいうとPという素数より低い数字をPで割った場合にあまりは必ずNになるということ
    
    これを判定するには１, ..., P-1まで調査すれば答えが出るが、計算量が膨大になる。
    フェルマーの定理ではこの１, ... , P-1の間でランダムに選んだ数字で上記の定理通りになれば、素数である確率が高いということを示す方法。