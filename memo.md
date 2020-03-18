# はじめに
書く場所がなかったものを書き留めています。

# 2020/2/23
    Django
        django-admin startproject xxx
        django-admin startapp yyy

        

# 2020/1/3
    activate状態 -> deaactivate
    pyc
    sys.pathの初期化における参照先は？
    math.cos, math.pi
    log moduleは？ -> logging
    import sys.os
    パッケージとは？
    dir()は？ -> module定義の名前
    Tab保管

    from time.it import Timer
    import unittest

    from array import array

    from collections import deque

    from bisect

    from heapq import heapify, heappop, heappush

# 2019/12/19
    Array in Python
        List, Tuple, Set
            slice of listで参照渡しとして同じエレメントを見ている
            なので例えば以下の場合は全部同じゼロのエレメントを見ている
            
            counter = [0] * 8

            shallow copy
                同じelementを参照するlistとしてコピーするので参照渡しになる
            deep copy
                別のエレメントとして値を保存するので値渡しになる


        Dynamic Array
            Pythonのarrayはdataが増えると自動でarrayのcellを拡張してくれる

            Length:   0; Size in bytes:   72
            Length:   1; Size in bytes:  104
            Length:   2; Size in bytes:  104
            Length:   3; Size in bytes:  104
            Length:   4; Size in bytes:  104
            Length:   5; Size in bytes:  136





# 2019/12/18
    Number Factor
        与えられた入力に対して、整数を組み合わせてそれになるのは何パターンあるか？

        例えば n=5　で入力が 1, 3, 4ならば次のように分解する
        この結果から答えは6種類となる。
        つまり、それぞれの1, 3, 4のパターンに対する最適解を出して
        それらの合計が答えになる。
        こう行った要素分解ができることがDvide and Conquerの1種となる

        5 - 1 = 4 {1, 1, 1, 1}, {1, 3}, {3, 1}, {4}
        5 - 3 = 2 {1, 1}
        5 - 4 = 1 {1}

        例えば8で1, 3, 4ならば、このように小さい問題に分解していくことができる
        8 --- 7 --- 6(5, 3, 2), 4, 3
           +- 5 --- 4, 2, 1
           +- 4 --- 3, 1, 0

    House Thief
        泥棒が最大の価値を出す盗み方は何か？
        制限として隣り合った家からは盗みができない
        input: {6, 7, 1, 30, 8, 2, 4}
        will steal: 7, 30, 4

        これも小さい問題に分割する。
        考え方としては,
        今のindexを取った時 + 一つとばした先の最大評価を選択
        もしくは今を取らなかった時の次の配列からの最大評価の
        どちらか高い方が最適解。
        これを再帰的に繰り返すと次のように分解できる
        そうすると同じ問題が多く取ることができる

        {6..4}
        - {6} + {1..4}
            - {1} + {8..4}
                - {8} + {4}
                - {2, 4}
            - {30..4}
                - {30} + {2, 4}
                - {8..4}
                    - {8} + {4}
                    - {2, 4}
        - {7..4}
            - {7} + {30..4}
            - {1..4}

    Convert One String to Another
        二つのstringが与えられ、いくつのcharを変更すれば同じ問題になるか？という問題
        次のようの問題が与えられたそれぞれ最適解があるが、それは全体を見ているからわかる
        ただ各問題には共通したルール(F)がある。

        table, tgable // delete F(2, 3)
        table, tble // add F(3, 2)
        table, tcble // replace F(3, 3)

    Zero/One Knapsack
        Fractionalではないので、取るか取らないかを選ぶ
        value: {31, 26, 72, 17}
        weight: {3, 1, 5, 2}
        cap: 7

        これもhouse thiefと同じ考え方をする
        つまり小さいく最大価値を求めて行って、大きい価値を選択して行けばいい

        {31..17} // return 98(26, 72)
        - {31} + {26..17, w(7 - 3) // return 43
            - {26} + {72, 17, w(4 - 1)} // return 43(26 + 17)
                - {72} + {17, w(3 - 5)} // break
                - {17, w(3 - 2)} // return 17
            - {72, 17, w(4)} // return 17
                - {72} + {17, w(4 - 5)} // break
                - {17, w(4 - 2)} // return 17
        - {26..17, w(7)} // return 98
            - {26} + {72, 17, w(7 - 1)} // return 98(26 + 72)
                - {72} + {17, w(6 - 5)} // return 72
                    - {17, w(1 - 2)} // return break
            - {72, 17, w(7)} // return 89
                - {72} + {17, w(7 - 5)} // return 89(17 + 72)
                    - {17, w(2 - 2)} // return 17
                - {17, w(7 - 2)} // return 17

    Longest Common Subsequence
        stringが二つ与えられ、sentenceが特定のcharを削除したら
        もう１方のシーケンスと同じ文字になる最大値は何か？

        s1: elephant, s2: eretpat -> delete r, t -> eepat

        これの考え方もHouse Thiefと同じ
        まずs1[0] == s2[0] を比較して、==なら次のsequence
        s1[1] == s2[1]を比較してnotならs1[2] == s2[1] or s1[1] == s2[2]の場合がある
        これを繰り返していくことで最終的に全ての文字列を比較できるので、
        s1[i] == s2[j]でcount1もしくはstringとして追加して積み上げれば答えになる。

    Longest Palindromic Subsequence
        与えられた文字列から回文になる最大の長さは何か？という問題
        ELRMENMET -> EMEME

        これもlonget common subsequenceと同じ考え方
        前後から進んでいけばいい。
        s1[0] == s[-1] の比較を上と同じアルゴリズムで続ければいい
        s[1] == s[-1] or s[0] == s[-2]て感じ

    Longest Palindromic Substring
        これは最長のpalindromicをだす

        ABCYRCFBTUA
        subsequence: ABCYCBA
        substring:  A whatever

        ABCBDならsubstring BCBである
        これらを求める時には両はしから同様にイコール評価するが、
        カウントする前提として残った配列が回文であることが前提になる
        なのでそれを再帰的に掘っていき評価うsる

    Min Cost to reach last cell in 2d array
        要は際低コストでの迷路探索である
        スタートが左上でゴールが右下のような例
        これであれば右下のゴールにたどり着くには上からか左からかでないと辿れない
        なのでこれを再帰的に解析していく

        int findMinCost(int cost, int row, int col)
            if(row == -1 || col == -1)
                return MAX_VALUE
            if row == 0, col ==0)
                reutrn cost[0][0]
            minCost1 = findMinCost(cost, row-1, col)
            minCost2 = findMinCost(cost, row, col-1)
            int minCost min(minCost1, minCost2)
            currentcellcost = cost[row][col]

            return minCost + curretnCellCost

    Number of paths to last cell with given cost
        迷路の探索問題で最小の値になるコストが複数あった場合にどのようにカウントするか？
        前提として最小コストがわかっている状態。
        この場合であれば各セルにたどり着くのに指定のコストでどうすればたどり着けるか？を繰り返せば答えになる


    Dynamic Programming
        すでに計算された結果を再利用することで全体の計算量を削減する手法
        Divide and Conquerと相性がいい
            なぜならFibonacciみたいに同じ計算を繰り返すことが多いからである

        Top-down, Bottom-up Approach
            これはメモ化したセルを上からもしくは下から参照することを開始して
            徐々に足りないセルを埋めていく方法

            Top/Downで比較するとTopの方がイメージがしやすいのでインプリがしやすい
            ただしスピードはbaseまで掘っていかないといけないのでTop-Downの方が遅い
            また再帰的に見ていくのでstackするmemory spaceが必要(ただいうほどではない）
            なので、早くインプリするならtop-downだし、
            効果の高いもの出ないとダメならbottom-up

            ただbottom-upはデータがどのように導出されているくかをわかった上でないと書くことは難しい。そのためtop-downからbottom-upにしていくことを考えるといい


    Number Factor Problem
        これも構造化されたデータで、同じ結果を利用するため、DPの効果がある
        これは大きい数字から0に向かって再帰的に導出される
        つまり0から目的の数字まで計算して行けば結果的に導出される

    House Thief Problem
        同様にdpを使うことができる
        この場合は左の配列から再帰的に進んでいって右から答えが返ってくる
        なのでbottom-upをするなら右の配列から最大値を計算していくことで導出される

    Convert One String to Another
        これも同じで、文字の比較をしている「結果」がDPとなる
        この場合はbottom-upにするには右下から左上に上がっていくデータ構造になる

    Zero One knapsack
        できなくはないが、あまり効果はない。

    Longest Common Subsequence, Longest Palindromic Substring/Subsequence
        Convert Oneと同じで文字のセル比較がTrue/Falseで残せる

    Min Cost to reach last cell in 2d array, Number of paths to last cell with given cost
        指定のセルにたどり着くまでの最小値という意味ではDPの効果がある

    


# 2019/12/17
    Greedy Algorithem
        局所最適解を求めていき、最終的に全体最適解に導くこと
        例えばソートであれば全体の配列を半分にしてそれぞれにソートして
        まとめていくことのイメージに近い

    Activity Selection Problem
        start, endが記載されたアクティビティの羅列から、最大に実行できるアクティビティを求める問題
        簡単には全パターンを試すと答えは出るが現実的ではない
        この時endという点にだけ注目すれば最適な答えが出る
        なぜならstartするにはendが来ないと開始できない。
        startが極端に遅い場合はendも極端に遅い。つまりendでsortすれば
        段階的にstart, endを処理することができる。

        このことからendをsortすれば全パターン試さずに
        １パターンという局所最適解が常に全体の最適解になることを貪欲法の一例として示される

    Coin Change Problem
        特定の金額を支払いたいときに最小のコインの枚数で支払える条件を求める問題

        貪欲法で言われるのは一番金額の高い硬貨から支払っていけば最適解にたどり着くこと
        ただし条件として候補となる硬貨が隣の金額で割り切れること。
        つまり倍数であることが条件となる。

    Fractional Knapsack Problem
        itemにvalueとweightのパラメータがあり、ナップサックの最大Wを超えないように
        最大のvalueを求める方法
        これはFractionalなので分数として分解できる状態（つまり割合で選べる)

        まずitem単位にvalue/weightで同じ単位での価値の違いを求める(Density)


    Divide and Conquer
        問題を小さい形に分解できるなら、一つずつ最適解を求めて行って、
        最終的に結合することで最適な結論に至るという考え方
        e.g. Fibonacci, MergeSort


# 2019/12/16
    Graph
        DFS for SSSP
            最後までいってから戻ってしまうため、近い頂点があっても気づくことができない
        
        Dijkstra for SSSP
            コストの計算をし、より小さい値があれば更新をする
            各頂点は１回だけ評価する。評価する際には全体から最小であれば評価を開始する
            miniHeapを使うことで、最小値から常にスタートすることができる
            ただしこれはweighted がpositiveの場合のみ。
            なぜならnegativeだと無限に最小値になる方法がありループしてしまうから。
            厳密にはnegativeの値でループできてしまうグラフの場合。

            Dijikstra(G)
                Set the distance of all the vertices as inifinite and source vertex as 0
                save all the vertics in miniheap
                do until miniheap is not empty
                    current vertex = extract from miniHeap
                        for each neighbour of curretnVertex
                            if currentVertex's distance + currentEdge < neighbor's distance
                                update neighbor's distance and parent

        BellmanFord for SSSP
            全てのケースに対応できる
            negative cycleを検知する仕組みを入れて、その時に全ての結果を出力する

            BellmanFord(G):
                set all the vertex distance to infinite and source as 0
                for 1 to V-1:
                    for each edge(u, v): // if current of V is greater than current weight of U + current edge
                    if d(V) > d(u) + w(u, v)
                        d(V) = d(u) + w(u, v)
                        update parent of V
                
                for each edge(u, v) // v-1で最適化されているので、１回iterationして数字が変わるなら、それはnegative cycleが含まれるという判断
                    if d(V) != d(u) + w(u, v)
                        then report exsitance of negative-weight cycle

                print all vertex

            iterate回数は必ずV-1となる
                一番遠いシチュエーションは最初のEdgeは評価ずみで考えると、
                V-V-V-V-Vと一直線にした状態なのでV-1となる。
                またそれまでの間にコストは最適化されるから。

        BFS vs Dijkstra vs BellmanFord
            BFSはunweightedしか使えない、Dijkstraはnegatvie cycleに対応しない
            BellmanFordは全てに使える

            BFSはunwrighted graphに使える
            Dijkstraはweighted graphに使える
            Negative CycleにはBellmanFordが使える

            なぜなら下に行くほどアルゴリズムが大変なので、上の方がコストは低い
            またVFS, DijkstraはO(V^2)で、BellmanFordはO(VE)ではある。
            ただ割りにあった構築の方がいい。

        APSP ... All Pairs Shotest Path First
            今までは一つのソースからゴールまでの最短距離を計測した
            しかしAll pairsとあるように全ての頂点からそれぞれに対してのコストを計算する場合、今まで学んだBFS, Djikstra, Bellman Fordでは頂点の数だけ試す必要がある。
            次のアルゴリズムはそれに対する対応策となる。

            Floyd Warshall
                matrixを作成し下記のアルゴリズムの概念でイテレーションを繰り返す

                if D[u][v] > D[u][via X] + D[via X][v]

                初期のmatrixでは隣り合ったコストは与えられるので、それを埋める。
                隣り合っていないのverticsはコストがわからないので、
                via Xが機能する。[a][c] [c][d]と取ることでc経由でa-dのコストがわかる
                このvia Xは全てのnodeをいれて結果を出すため、計算量は自ずと大きくなる
                for u
                    for v
                        for via X

                動作する条件は各ノードに必ず到達できる方法がある場合

            FloydWarshall(G)　... O(v^3)
                initialize a tabe of size V x V: D with inf
                copy D from G
                for k=0 to n-1 // run the loop as many time as number of vertices
                    fro i=0 to n-1 // run the loop such that we visit each cell in 2D array in row wise fashion
                        for j=0 to n-1
                            if D[i][j] > D[i][k] + D[k][i] then
                                D[i][j] = D[i][k] + D[k][j]
                    return D

            ただしgraphにネガティブサイクルがある場合は動作しない
                これはDijkstraと同じでループをすることで永遠と低い数値を更新してしまうから

        BFS vs Dijiktra vs Bellman FOrd vs FloydWarashall for APSP
            BFSはunweighted向け。O(V^3)だが実装が簡単だから。
            Dijkstraは適さない
            BellmanFordはWeighted Graph(negative cycleがある場合)はこれしかない
            FloydWarashallはWeighted Graph(no negative cycle)はこれ。実装が簡単だから。

        Disjoint Set
            素集合を作るためのアルゴリズムでMSTに使える
            これによってunionを頂点同士の接続とみなし、unionないに同じ頂点が現れるとループと判定できる
            ・makeset : initializeで頂点の分のセルを確保する
            ・findset : 与えた二つの頂点が同じunionに所属しているか確認する
            ・Union : 与えた二つの値を一つのunionに変更する

        Minimum Spanning Tree
            ループしているようなグラフの場合に、そのVehiciesに対して全体から一番最小コストのエッジだけを選択していく方法
            ただしこれは最小コストだけのエッジを選ぶので、全体の道順から考えて最適でないコスト計算結果になる場合がある
            アルゴリズムのアイデアは２種類ある

            Kruskal
                greedy algorithem(貪欲法)
                エッジ全体から最小の値から順番にリンクを選んでいく。
                この時エッジ同士を結んでループになるならば選択をしないという仕組み
                結果最小コストのリンクだけを選んで、ループしないという結果になる

                MST-Kruskal(G)
                    for each vertex: Makeset(X)
                    sort each edge in no-decreasing order by weight // sortなどすることで最小値からループを回せる
                    for each edge(u, V) do:
                        if findSet(u) != findSet(x)
                            Union(u, v)
                                cost = cost + edge(u, v)                

                まずmakesetでinitializeして、各頂点を評価する
                評価した同士をunionとしてくっつけていき、同じ頂点が同じunionに入ろうとしたらループとしてスキップする
                その結果、ループなしで接続することができる

            Prim's
                各Vehicleに到達した時に接続している頂点全てのedgeの更新有無を確認する貪欲法

                MST-PrimS(G)
                    create a PriorityQueue(Q)
                    Insert all the vertices into Q such that key value of starting vertex is 0 and others in infinite

                    while Q is not empty
                        curretnVertex = dequeue(Q)
                        for every adjacent unvisited Vertex of currentVertex
                            if current weight of this adjacent vertex is more than current edge, then update adjacent vertex distance and paretn
                        mark curretnVertex as Visited
                    print all the vertices with weights

            Prims vs Kruskal
                edgeに注目して確認をしていく
                一方は頂点に注目して確認をしていくという構造の違いぐらい。

    Magic Framework
        Problem Statement
            Greedy Choice
            Optimal substrcture -> apply Divide and Conquer
                                -> Overlapping subproblem
                                -> Apply Dynamic programming
            Apply Brute Force
            
# 2019/12/15
    AVL Tree ... Adelson-Velskii and Landis' tree
        balanced BST
        一つのノードから見たときに左右のchildの下にある木の高さが最大でも1以下の差である状態
        これがバランスが取れた状態で、左のchildの高さが2で右のchildの高さが0なら崩れている
        仮にchildがない場合は-1として考える。
        バランスが取れていない場合はローテーションが必要となる。

        Create
            作成 ... BSTと同じ
        Search
            O(logn) ... BSTと同じ
        Traverse
            O(logn) ... BSTと同じ(ただしlevel-orderでは全部探すのでO(n))
        Insert
            rotatioが前提(rotationがないとBSTと同じ)
            LL ... Left Left condition
                unblanceになる理由がleft left にあるならrightに昇格するようrotationする

                right Rotate(currentDisbalancedNode)
                    newRoot = currentDisbalancedNode.left
                     # balanceの取れてないnodeの左のnodeを昇格させる
                    currentDisbalancedNode.left = currentDisbalancedNode.Left.Right
                     # 右にrotateされるバランスの取れていないのnodeのleftに
                     # 次に昇格させるnodeの右側を結ぶ
                    newRoot.Right = currentDisbalancedNode
                     # 新しく昇格するnodeの右側にバランスの取れてなかったnodeを結ぶ
                     # 最後にそれぞれのheightをcheckしてバランスが取れていることを確認する
            LR ... Left Right condition
                unbalaneになる理由がleft rightにあるなら
                left-rightのnodeを上に昇格させて、元のnodeをleftに降格させる
                そうするとleft-left conditionになるので一番上を右にrotationさせる

            RR ... Right Right condition
                left-left conditionの逆と考えればいい
            RL ... Right Left condition
                left-right conditionの逆と考えればいい
        Dlete
            no child ... 消すだけ
            delete 1child ... 下のnode/leafを昇格させる
            delete 2child ... 次のsuceeedとswapさせる

            また削除したときにバランスが崩れたらLL, LR, RR, RLを駆使してrotationを行う

    Binary Heap
        Bniari treeの１種
        特徴はlognで最小値、もしくは最大値を探すことができること
        
        Heap Property
            Min-Heap
                parentに対してchildの二つの数字が大きい状態。つまりrootは最大値になる
            Max-Heap
                min-heapの逆。つまりはrootは最小値になる。
        Complete Tree
            全てのレベルのが揃っているか最後のレベルは左に詰めている状態

        arrayやlinked listではinsertをする際にO(n)になってしまう（0~nまで検索する必要があるから）
        
        Insertion
            insertは一番下の左づめでBSTが作れるように挿入する
            その後追加したleafは自分にparentと比較して、
            min-heapであれば自分の方が小さければswapをくり返して昇格していく

        rootの取り出し
            最大値や最小値としてrootが抜けた後は、treeの最後の数字をrootに挿入する
            その後、その数字が適していないければchildと繰り返してswapしていく
            arrayで作成することでcellの最後をO(1)で見つけて変更できるが、
            referenced baseだとlog(n)で探す必要があるのでやめた方がいい。

    Trie(トライ)
        char or stringによるsearch tree
        これによって文字の予測をするといったこともできる
            文字入力の履歴や予測、補完など。
        多くは文字の確認などができる

    Hashing
        特定数値に対してhashを取得して結果を保存することで
        同じhashになるならばその答えは同じになるだろうという考え方
        しかし、hashが重なることで異なる答えが同じtableに保存されることもある
        そのときには二つの方法で解決する
        ・chaining
            linked listとしてdataを同じtableに連結して保存すれば良い
            hash結果があまりに重なるとllが大きくなってしまう危険はあるが
            hash table sizeの苦労はない
        ・open addressing
            データを違うhash keyに入れ替えを行う
            ・Linear probing
                空いてなかったら次の空いているセルに入れる
            ・Quadric probbing
                空いてなかったらセルのセル + 1^2, 2^2, 3^2, 4^2, の場所に配置する
                Linearよりはばらける結果になりやすい
            ・Double Hashing
                重複したらもう一つのhash algorithemで異なるhash keyを求める
            この場合はhash tableが埋まってしまうと埋める場所がなくなるので、
            一般的には今のhash tableのsizeを２倍にして、今のをcopyして用意する仕組みになる。

    Sorting
        Sortにはいくつかの検討ポイントがある
        ・In-Place ... 同じ配列空間の中でソートを行う
            Bubble Sort
        ・Out-of-Place ... 違うメモリで配列結果を保存していく
            Merge Sort
        ・Stable ... 入力データの順番を崩さすにはソートを行う
            Insertion Sort
        ・Un-Stable ... 入力データの順番を崩してソートを行う
            Quick Sort
        
        Bubble Sort ... O(n^2)
            最初の二つのデータを比較して小さい方を左側に。大きい方を右側にする。
            これを繰り返すと必ず一番みぎが大きい数字になる。
            そのため次は一番最後の手前までの順番を同じことを繰り返すと、結果ソートされる。

            使えるケースは、、、
            ・すでにソートされたデータである場合*
            ・追加のメモリが取れない場合
            ・簡単な実装がいい場合
            ・時間の問題を無視できる場合

        Selection Sort ... O(n^2)
            配列を全てソートして最小値を抽出して一番左に挿入する
            次に左から一つみぎから橋までのセルをソートして最小値を左に持っていくを繰り返す

            使えるケースは、、
            ・追加のメモリが取れない場合
            ・簡単な実装がいい場合
            ・時間の問題を無視できる場合

        Insertion Sort ... O(n^2)
            最初のセルをソート済みとし、次のセルの数値をソート済み配列と比較し
            正しい位置に挿入を行っていく

            使えるケースは、、
            ・追加のメモリが取れない場合
            ・簡単な実装がいい場合
            ・データが継続的に入力されてくる場合*
            ・時間の問題を無視できる場合

        Bucket Sort ... O(nlogn) >> O(n) + O(nlogn) + O(n)
            bucketを作成する
                このbucketはデータの数の平方根によって決める(sqrt(num))
            各bucketには次のルールでデータを振り分けする
                (value * number of bucket) / max value in array
                例えば３つbucketがあると、自ずと小中大の３種類として振り分けられる
            各ソートのなかでデータをソートを行う
                sortはquick sortを使えばlognになる。これをn回繰り返すのでnlogn
            そしてマージを行う
                各バケットがランクで正しく分配されている前提なのでマージしても問題ない

            使えるケースは、、
            。データがばらついている場合。偏りがあると一つのbucketに入りすぎて意味がない。
            ・bucketによる追加のメモリが気にならない場合

        Merge Sort ... O(nlogn)
            データの二分割を繰り返し、データが一つになるまで行う
            その後次のデータと組み合わせてソートを行いくっつけていく
            このときLとRのセルを一つずつ取り出して小さい方からセルとして選んでいく
            
            mergeSort(A, l, r):
                if r > l
                    middle m= (l+r)/2
                    mergeSort(A, l, m)
                    mergeSort(A, m+1, r)
                    merge(A, l, m, r)

            merge(A, p, m, r):
                create tmp array L and R and copy A, p, m, into L and A, m+1, r into R
                i = j = 0
                loop:k = pto r
                    if L[i] < R[j]
                        A[k] = L[i]; i++
                    else
                        A[k] = R[j]; j++

            使えるケースは、、
            。stable sortで欲しいとき
            ・平均的にnlognの実行時間がいいとき
            ・ただLとRのtmp listが必要なのでspaceの懸念はある

        Quick Sort ... O(nlogn)
            pivotという起点を決めて、その数字より大きい数字をみぎ、小さい数字を左と分ける
            これを左右それぞれの残りの数値にpivotを元に分類することを繰り返せば必ずソートされる
            数字をソートする際には左端からpivotと比較して、
            小さい数字を左にinsertを繰り返す、このときiとして端を保存しておくことで
            swapを繰り返す。
            最後までソートできたたらpivotに出会うのでpivotをiの位置と交換する
            pivotは一番右端を利用するのが基本。

            QuickSort(A, p, q)
                if(p < q)
                    r = patition(A, p, q)
                    QuickSort(A, p, r-1)
                    QuickSort(A, r+1, p)

            Partition(A, p, q)
                pivot = q
                i = p-1
                for (j = p to q)
                    if (A[j] <= A[pivot])
                        increment i and swap(A[i], [j])

            使えるケースは、、
            。unstable sortでもいいとい（つまり同じ数字のデータがあるときは適さない）
            ・平均的にnlognの実行時間がいいとき
            ・余計なspaceを取りたくないとき         

        Heap Sort ... O(nlogn)
            Heap BTを使ったソートの方法
            min-heapであればrootが必ず最小値なのでそれを一つずつ抜き出せばいい。
            max-heapであればreverseされたソート結果になる

            使えるケースは、、
            。unstable sortでもいいとい（つまり同じ数字のデータがあるときは適さない）
            ・余計なスペースを使いたくないとき

        Sorting Chart
            要件に応じた取捨洗濯が重要
            ミッションクリティカルならTimeが大事。
            データ構造の維持が大事ならSatble。
            メモリが足りないならSpaceが大事

                        Time        Space   Stable
            Bubble      O(n^2)      O(1)    Yes
            Selection   O(n^2)      O(1)    No
            Insertion   O(n^2)      O(1)    Yes
            Bucket      O(nlogn)    O(n)    Yes*
            Merge       O(nlogn)    O(n)    Yes
            Quick       O(nlogn)    O(n)*   No
            Heap        O(nlogn)    O(1)    No

    Graph
        VとEによって表されるデータ構造
        Vはvertices(頂点)でEはEdgeの省略。要はVは場所を示し、Eは場所から場所の間のリンクを示す。

        unweighted/weighted Graph
            edgeに対してコストがあること
            weightedには正負があるのでpositiveだけか、negaiveも含まれるかで分類される
        Undirected/directed Graph
            V->Vと１方向しかいけなかったり、両方向行けたりといった制限がある状態
        cyclyic graph
            ループする箇所があること
        Tree or DAG(Directed Acyclic Graph)
            これは特定のスタート地点からだと同じ場所に戻ってこれない場合に作れるtree構造

        グラフを作成するには二つの方法がある
            Array matrix
                グラフを示す時には二次元マップを作るといい
                例えば A-Bで行き来できるならばフラグを1にするなど。
                わかりやすいのはこっちだがarrayなので拡張が難しい。
            List
                これは特定の地点それぞれに対して、繋がっている場所をリストとしてアペンドさせる
                データが追加されたり削除されることが多いならばlistの方が適しているが難解。

        BFS algorithem ... Breadth First Search // 幅優先探索
            queueのデータ構造を使う
            訪れる候補をqueueにためて、１訪れる可能性が隣にあればそれもqueueにつめていく

            BFS(G) 
                while all the verticies are not explored, do
                    enqueue(any vertex)
                    while Q is not empty
                        p = dequeue
                        if p is unvisited
                            prit p and mark p as visited
                            enqueue(add adjacent unvisited verticies of p)
            
        DFS algorithem ... Depth First Search // 深さ優先探索
            stackのデータ構造を使う

            DFS(G)
                while all the vertices are not explored, do
                    push(any vertex)
                    while Stack is not empty
                        p = pop
                        if p is unvisited
                            print p and mark p as visited
                            push(all unvisited adjacent vertices of p)    
        BFS VS DFS
            ゴールが深いところにあるならDFS
            ゴールがスタートの近くにあるならBFS
                要件に応じて選び分けれるのがベスト
            両方とも計算量はO(E+V)になる        

        Topological Sort
            dataの依存性を見つけるときのアルゴリズム
            A > B > C ならCにはBが必要で、BにはAが必要ということ。
            このときはCからstackで埋める。なぜならAやBは最後まで行かない限り
            何に依存しているかがわからない。Z > Aかもしれない。
            ただケツから行けば確実にAが最後だとわかる。

            topologicalSort(G)
                for all the nodes
                    if this Vertex is not visited
                        topologicalVisit(node)
                pop stack

            topologicalisit(currentNode)
                for each neighbour of currentNode
                    if neighbor is not visited
                        topologicalVisit(neighbour)
                mark currentNode as visited and push node in stack

        Singile Source Shortest Path(SSSP)
            目的のゴールまでにどれぐらいのコストでたどり着けるのか？

            BFS for SSSP
                各verticesまでのコストを計算する
                ただこれはunweighted-undirectedかunweighted-directedの２種類でしか動かせない
                なぜならBFSはnodeに訪れたことを記録して道を探すため、
                shortpathが他にあってもそれを探索することができない
            
            DFS


# 2019/12/12
    Tree - Array
        Create
            cellへの配置は下記で考えると治る
            ・Left Child - cell[2x]
            ・Right child - cell[2x+1]
            セルサイズは不変のためサイズは注意する
        Insert
            ram cellを確認して、空いているセルの位置に入れる
            例えば9が空いているなら、parentセル 4のchildになる
        Search
            arrayであればメモリが連続しているので、探せばいいだけ。
            linked listでは各ノードはleft, rightのセルしか知らないので
            該当のデータにたどり着くまで探していく必要がある
        Traverse
            In-order
                InorderTraversal(Index)
                    if index > lastUsedIndex
                        return
                    else
                    InorderTraversal(index * 2)
                    print current index.value
                    InorderTraversal(index * 2 + 1)
            Pre-order
                preTraversal(Index)
                    if index > lastUsedIndex
                        return
                    else
                    print current index.value
                    preTraversal(index * 2)
                    preTraversal(index * 2 + 1)
            PostOorder
                postraversal(Index)
                    if index > lastUsedIndex
                        return
                    else
                    postTraversal(index * 2)
                    postTraversal(index * 2 + 1)
                    print current index.value
            Level-order
                levelOrder(Index)
                    loop: 1 to lastUserdIndex
                        print current index.value
        Delete
            LLと同じで一番深いせると消したいセルを交換して、深いセルを削除する
            深いセルはセルの一番最後なのですぐ見つけれる

    Binary Search Tree(BST)
        自分より左のchildには小さい数字を、右のchildには大きい数字を配置する構造
        BSTはInsert, Delete, Searchの面でLLがO(n)に対してO(logn)を出せる

        Create
            作るだけ

        Search
            これはO(log n)で、なぜなら繰り返すごとにn/2を実施するので(n/2)^kの結果になる
            これは k = log2nとなり、実施する回数のkの解法としてO(log n)となる
            このときlog2の2は基数は定数であるため無視することにする

            BST_Search(root, value):
                if(root is null)
                    return null
                else if (root == value)
                    return root
                else if(value < root)
                    BST_Search(root.left, value)
                else if (value > root)
                    BST_Search(root.right, value)

        Traverse
            Pre-Order, In-Oreder, Post-order, Level-Orderの考え方それぞれ適用できる

        Insert
            Searchと同じアルゴリズムで下に下っていって、NULLの場所に配置すればいい
            これも同じようにn/2を繰り返すのでO(logn)となる

            BST_Insert(curretnNode, valutToInsert)
                if(currentNode is null)
                    create a node, insert valutoinsert
                else if(valutoinsert <= current node val)
                    currentNode.left = VST_Insert(currentNode.left, valueToInsert)
                else
                    currentNode.right = BST_Insert(curretnNode.right, valuTOInsert)
                return curretnNode

        Delete
            Searchと同じ形でDelete Nodeを探す
            Leafならそれで削除できるが、Nodeだと削除するとchildも削除されるので、
            childが昇格することでバランスを取るようにする
            次にどれを選ぶかというとsucsessorsを使う
            これは全体を見たときに削除したいノードの次の数値のノードに当たる


# 2019/12/11
    Tree
        階層構造であること
        各データは二つにデータが分割される（理想）
        root nodeがあり分割されている

    Terminologies
        Root: Node with no parent
        Edge: Link from Parent to Child
        Leaf: Node with no children
        Sibiling: Children of same parent
        Ansector: means Parent, grand-Parent, great grand parent, and so on for a given a node
        Depth of node: Length of the path from root to node
        Height of node: Length of the path from that node to the deepest node.
        Height of tree: Same as height of root node.
        Depth of tree: Same as depth of root node.

    Binarty Tree
        binary treeはzero, one or two childをもつ構造
        binary treeはこれらのデータ構造の仲間で、BTの理解が根底にある
            BST, Heap Tree, AVL, Red-Black, Syntax, Tree, Huffman Coding Tree, etc

    Types of BT
        Strict Binary Tree: If each node has either 2 children or not
            tree構造
        Full Binary Tree: if each non leaf node has 2 children and all leaf nodes are at same level
            全てのleefが同じ深さをもつ状態
    
        Complte Binarty Tree:if all levels are completly filled except possibly the last level and the las level has all keys as left as possible
            一番最後のリーフが左から埋まっている状態

    x = parent cell number
        Left Child cell = [2x]
        Right Child cell = [2x + 1]

    BT - LL
        Create
            Binarty Tree用のメモリセルを確保するだけ(可変)
        Insert
            Insertを実行するときはTraverseと同じ動きを辿ってnullのポジションにデータを入れる
        Delete
            root nodeを削除したい場合
                一番木で深くにあるものと交換して削除する
                直接消してしまうのは木を維持するために上に１個ずつ持ち上げないといけないから
                要はchildがないleafを移動させてる問題少ないから。
        Search
            考え方はtraversalと同じで、見つけたらreturnする
        Travese
            Pre-order(深さ優先探索1)
                Root, Left Subtree, Right Subtreeの考え方を取ればいい。
                端的にいうと一番左に進んでいって、段階的に右に進む
                r(()()())(()())
                この順番はスタックと同じ。

                preorder Traversal(root)
                    if (root equls null)
                        return error message
                    else
                        print root
                        preorderTraversal(root.left)
                        preorderTraversal(root.right)

                このコードを見ればわかるように再帰関数でleft subtreenにいくことを優先している
                つまり限りなく左に進み、returnで戻る時に右を参照する。
                もし右を参照して左の要素があるなら左に進んでそこまでいく。。というのを繰り返す。

                この時recursiveで後回しになったぶんはスタックされていると考えてもわかりやすい。

            In-Order(深さ優先探索2)
                Left Subtree, Root, Right Tree
                (()())r(()())

                inOrderTraversal(root)
                    if (root equals null)
                        return
                    else
                        inOrderTraversal(root.left)
                        print(root)
                        inOrderTraversal(root.right)

                難しく見えるが関数で考えると用は順番を変えてるだけ

            Post-order(深さ優先探索3)
                Left Subtree, Right Subtree, Rootの順番で探索する
                (()())(()())r

                postOrderTraversal(root)
                    if (root equals null)
                        return
                    else
                        postOrderTraversal(root.left)
                        postOrderTraversal(root.right)    
                        print(root)            

            Level Order Traversal(幅優先探索)
                レベルの順番で調査をしていくからレベルオーダー

                levelOrderTraversal(root)
                    create a queue(Q)
                    enqueue(root)
                    while(Queue is not empty)
                        enqueue() the child of first element
                        dequeue() and print

                root のchildは次のlevel。次のlevelのchildはLとRで二つだが
                Lのchildを入れてもRが残ってるので、queueに順番に溜められる
                R, L1, R1, LL2, LR2, RL2, RR2 って感じ


# 2019/12/10
    Queue
        順番待ちのこと
        First in First out(FIFO)

    Implementation
        Array
            LiniearQueue
            CircularQueue（LinkedListみたいに前のセルの参照という意味じゃないよ。）

        Linked List
            LiniearQueue
            xCircularQueue
                使わない。なぜならqueueはheadから出ていくので、一つ前のdataを参照する必要がない


    プロセス(Array-LIEAR)
        CreateQueue
            queueしたいセルの数を決めて確保すれば良い
        enQueue
            topofqueueのvalを持たせて末尾をカウントしていけばいい
        deQueue
            beigining of queueをdequeueのたびにカウントしていけば良い
            そしてbeiginingが末尾にたどり着いたら-1に値を戻すことでqueueの位置をループできる
            ただこれはbeginingが追いかけている間は無駄なのセルのスペースがどんどん増えるのでよくない構造
        peekInQueue
            出力を出すだけ。
        isEmpty
            begiggning = -1ならis empty
        isFull
            topofqueueがラストセルならfull
        deleteQueue
            arrayをnullで削除するだけ

    プロセス(Array-CIRCULAR)
        array-Linear queueだとセルがdequeue処理で無駄が起きるのでその対策
            方法としてdequeueするたびに左にdataを移動させる方法があるがこれだとO(n)になるのでやめた方がいい

        CreateQueue
            queueしたいセルの数を決めて確保すれば良い
        enQueue
            topofqueueのvalを持たせて末尾をカウントしていけばいい
            ただしtopofqueueが末尾まで言ったらカウンターを０に値を戻す。
            要はtop of queueがbeggining of queueを追いかける状態
        deQueue
            beigining of queueをdequeueのたびにカウントしていけば良い
            そしてbeiginingが末尾にたどり着いたら０に値を戻すことでqueueの位置をループできる
            bigiggning of queueもtop of queueを追いかける状態
        peekInQueue
            出力を出すだけ。
        isEmpty
            begiggning = -1ならis empty
        isFull
            topofqueueがラストセルならfull
        deleteQueue
            arrayをnullで削除するだけ

    プロセス(LinkedList-LINEAR)
        CreateQueue
            head, tailを作る。メモリ確保は動的なのでこれで。
        enQueue
            headとtailにnode cellを書き込む。セルが増えるごとにtailは更新されて、各ノードは次の参照セルが追加される。
        deQueue
            Head Queueを更新していけばいい
        peekInQueue
            出力を出すだけ。
        isEmpty
            Head,Tailの位置を調べればいい
        isFull
            linkedLinkなのでなし
        deleteQueue
            LLをnullで削除するだけ

    ではQueueでArrayとLinkedListどっちを選んだ方がいいか？
        結論はArray。大きい理由が最初からメモリを確保しないでいいのでQueueの構造にあっている

    いつ使うべきか？
        Queueの処理をしたいとき。
        ただし間にデータを入れれないのでそれが要求されないとき
        またランダムアクセスの要件にある場合は選べない。

# 2019/12/9
    Stack
        Stackは腕輪みたいなもの
    
        Last In Fast Out(LIFO)
            データをpushした場合に、最後のpushしたデータからpopされる
            Webブラウザの履歴などはまさにそう
                site1 -> site2 -> site3といったら履歴は3 -> 2 -> 1と戻る

        オペレーション 
            Create Stack
                Array or LinkedListによりデータ構造を決定し、処理方法をStack扱いで行う
                Arrayは簡単に実装ができるが、sizeの調整がで機内
                LinkedListは柔軟なサイズ調整ができるが、実装は少し面倒。

            Push/Pop
                stackの頂点を情報として保持する(top of stack)
                要はpushしてstackするてっぺんの位置を保持する
                これによってpopするときに指示ができる

                LinkedListのときはHeadがpushされた新しいノードのセルに更新されていく
                popされたときは一つ前のノードにセルを更新していく
                ちなみにTailは不要なので存在しない

            isEmpty/isFull
                dataがない場合はtop of stackがそこにあるので下限が作れる、てっぺんも同じ。
                なので最初の確保できたdataのサイズ-1が限界のindexとなる。

            Delete
                Stack自体はLinked List or arrayが削除(null)されれば消去される

                LinkedListの場合はheader = nullによって削除することで
                全てのセルの参照さきがいなくなるので消去できる
        When to Use
            DataをLIFOで扱いたいとき。
            データを途中に追加したり、ランダムアクセスするときには向いていない。


# 2019/12/8
    Linked List
        Linked Listは電車みたいなもの

        ArrayとListの違いはListは各データの間に次のセルを示すデータを持っているので、
        途中のセルが削除されても問題ないが、Arrayの場合は次のデータと接続している前提なので、
        削除することができない
        またメモリアクセスする際に、データを検索するときは最初のセルから辿っていきチェックする
        そのため、Arrayはランダムアクセスができるの反してできないといった違いがある

        Componenct
            Node ... データと次に接続するセル番号を持っている。最後のノードは終点なので次のセル番号はない
            Head ... Linked Listの始点であるセルを示す
            Tail ... linked Listの最後を示す
        
        Types
            Single Linked List ... dataと次のセルの参照先があり、一つ前のセルの参照先を持たない
            Circular Single Linked List ... 上記に合わせて最後のセルのノードに始点のセルを参照先で持たせている.
                ゲームのプレイヤーがループするとか。
            Double Linked List ... dataと一つ前と次のセルの参照先を持つ。始点と終点は参照前後がないのでNULL.
                ミュージックプレイヤーで前の曲、次の曲って押したい時とか。
            Circular Double Linked List ... 上記の始点と終点にループになるよう参照先を持たせる。
                例えばAlt + tabでアプリケーション画面を左右やループして切り返したい時とか。

        Linked Listは次の参照するセルを保持するのでRAMはバラバラに保存することができる
        Arrayは参照先を持たないためその列で確保する必要があるが、ランダムアクセスができる
        始点がわかるので + x　とすればアクセスできるため）
        一方でLinked Listの場合は参照セルを一つずつ辿らないと答えにつかない

        Create
            まずNode-1にdataを追加するセルを確保して、dataを追加
            次にHeadとTailをそのセル番号を参照先として保存する  

            create a head, tail, pointer
            create a blank Node
            node.value = nodeValue
            node.next = null
            head = node
            tail = node
        
        Inserting
            シチュエーションは３つ、始点と終点と途中にinsertする場合
            始点 ... headの参照セルを変える
            始点 ... tailの参照セルを変える
            中間 ... 一つ前のセルの参照先を変える 

        Delete
            Node-1を消すと、以降のセルへの参照方法がなくなるので全てがガベージコレクションになる
            対策として、Headの参照するセルをNode-2で書き換えれば大丈夫
            最後のNode-Nを消した場合はTailと一つ前のNodeの参照セルが変更される
            ちなみに最後のNodeしか残ってない状態でLast Nodeを消すとのFast Nodeを消すのは
            行為は同じに感じるが少し違いがある。なぜなら終点であるということで計算量がO(n)になる。
            途中を消す場合はセルを一つ先に飛ばせば良い。
            そうすると削除対象はガベージコレクションとして消去される
            
            LinkedList自体が削除されるのではhead, tailがnullになる時
            この瞬間に全てのdataに対して参照ができなくなるのでガベージコレクション扱いになる

    Circular Single LL
        SLLとの違いはTailのNodeの参照先がループりしていること
        最初にNodeを作ったときは、NULLではなく自分自身を参照している
        言い換えるとNodeが一つなら自分を参照させることでループ構造をつくる

    Double LL 
        SLLと考え方は同じで、違いは戻るための参照セルが付与されること
        SLLとの違いはDLL自体の削除でTailとHeadを削除しても
        Node1, Node2同士が互いに参照し合っているため削除されない
        そのため全てのNodeの参照を片側を統一して削除する
        具体的にはprev側の方。これは最初のNodeではNULLのため統一できるから。
        これによってNodeが疎結合になりガベージコレクションとして削除できる。

    Circular Double LL
        CSLLとDLLが合体したと思えばいい。
        これもCDLLの削除の時の注意としてDLLのようにprevを消すだけではだめ。
        なぜならTAIL-NODEがHEAD-NODEを参照しているので削除ができない
        なのでTAILのNEXTセルの参照をNULLにしてから
        全てのPREVのセルをNULLにすれば良い

    TimeComplecity LinledList vs Array)
        Particulars             Array   LinkedList
        Create                  O(1)    O(1)
        Ins at 1st position     O(1)    O(1)
        Ins at last position    O(1)    O(1)
        Ins at Kth position     O(1)    O(1)
        Del from 1st position   O(1)    O(1)
        Del from last position  O(1)    O(n) / O(1)
        Del from Kth position   O(1)    O(n)
        Sear in unstored data   O(n)    O(n)
        Sear in sorted data     O(logn) O(n)
        Access nth element      O(1)    O(n)
        Traverse                O(n)    O(n)
        Del entire Array/LL     O(1)    O(n) / O(1)

# 2019/12/7
    array
        Dimentional(one, two, three ...)

        one dimensional Arr[4]
            10, 20, 30, 40
        two dimensional Arr[3][4]
            10, 20, 30, 40
            100, 200, 300, 400
            1000, 2000, 3000, 4000
        
        arrayは連続していることを前提としているため、memoryを確保する際も連続したcellを確保する
        multi dimesionalの場合も一列で確保されることに注意。これは行列の作り方を考えるとわかりやすい
        [10,20], [30,40], [50,60] -> 10, 20, 30, 40, 50, 60という列で確保される

    オペレーション
        Declaring, Instantiating, Initializing e.g. int a[]={10, 20, 30, 40, 50}
            Declareで確保するRAMの名前を宣言して名前のセルを確保する
            InstantiatingでRAMから必要な行数分のセルを確保する
            Initilizingは確保したセルに必要な変数を代入すること
        Inserting
            確保しているセルに指定した数値を代入すること
        Traversing
            arrayのdataを移動すること
        Accessing
            指定したcellにアクセスすること
        Searching
            i=0 から増加させて指定したvalueの有無を確認すること
        Deleting
            指定sたlocationのdataを削除。削除といっても消去ではなく-2^31のような極端な数値に変わる

    When to Use?
        data typeが同じものを保存したい時
        random access dataの場合（要はindexを指定できる場合の方が良い）

# 2019/12/06
    Recursion
        同じオペレーションが異なる入力によって繰り返される状態
        繰り返されるにあたって、その出力が小さくなっていく状態
        基本の状態が必要で、それが終了する条件となる

    Treeで目的の値を検索していくという例ならば下記のような考え方。

    search(root, valueToSearch)
        if(root equals null) return null
        else if(root.value equls valueToSearch) return root
        else if(valueToSearch < root) search(root.left, valueToSearch)
        else search(root.right, valueToSearch)

    どういったデータ構造で使うか？
        Stack, Tree(Travarsal, Searching, Insertration, Deletion), Sorting(Quick Sort, Merge Sort), 
        Divide and Conquer, Dynamic Programming, etc

    Recursive case
        同じ形式で計算を繰り返すことができる要素
    Base case
        繰り返すことができない要素。要は終了するポイント。

    公式チックにすると標準の形式はこうなる

    SampleRecursion (parameter){
        if(base case is satisfied)
            return some base case value
        else
            SampleRecursion(modified parameter)
    }

    Recursiveのデータ構造はStack構造、つまりLIFOが起きているといっていい。
    BaseCaseにたどり着くまではpushでためており、たどり着いたらpopで最後から取り出しながら実行している。

    Sampleとして階乗(Factorial)なんかはわかりやすい

    Factorial(n):
        if n equals 0
            return 1
        return(n * factorial(n-1))

    Factorial(3) -> 3 * ?, Facotrial(2) -> 2 * ?, Factorial(1) -> 1 * ?, Factorial(0) -> return 1
    3*2                  <- 2*1                 <- 1*1                  <- 1

    次のサンプルとしてはFibonacciを使うのもいい

    fib(n)
        if n is less than 1
            return error message
        else if n is equal to 1 or 2
            return n-1
        else
            return fib(n-1) + fib(n-2)

    fib(4) = fib(3) + fib(2), fib(3) = fib(2) + fib(1) , fib(2) = 1, fib(1) = 0, fib(3) = 1, fib(4) = 2

    Recursive VS Iteration
    - Space Fileter? No, Yes    Stackをするのでメモリが必要になる
    - Time efficient? No, Yes   計算をする必要があるため
    - Ease of code/Problem? Yes, No     共通した計算式を導くためコードもシンプルになり、問題解決もシンプルにすることができる

    使った方がいいケースは？
        共通した計算式に落とし込める時。要はサブプロブレムとして分解できる時。
        timeとspaceのoverheadが許容できる時
        綺麗なコードや解決方法を行いたいとき
    
    一方で、複雑さよりもスピードが大事なシステムの時(airbagなど)には適さない。


    Algo Run Time
        Algorithemの良し悪しを判断する軸として効率という観点を持ち込むもの
        主には効率とは入力に対して答えを出すための計算量という意味で捉えるとイメージしやすい。

        Omega：less than/lowerを意味し、少なくとも入力に対してかかる計算の時間をさす。最低限必要な値なのでリソースもわかる。
        Big-O: more than/upperを意味し、多くても入力に対してかかる計算の時間をさす。最大現必要な値と考えればいい。
        Theta: averageを意味し、omegaとbig-oの真ん中にある。 

        O(1), O(logn), O(n), O(nlogn), O(n^2), O(n^3), O(2^n)
    
    例えば次のようなバイナリサーチでの計算方法を考える

    BinarySearch(int findNumber, int arr[], start, end):    ... T(n)
        if(start equals end)    ... T(1)
            if(Arr[start] equals findNumber)
                return start
            else return error message that number doesn't exists in the array

        mid = findMid(arr[], start, end)
        if mid > findNumber
            BinarySearch(int findNumber, int arr[], start, mid) ... T(n/2)
        else if mid < findNumber
            BinarySearch(int findNumber, int arr[], mid, end) ... T(n/2)
        else if mid = findNumber
            return mid

    まず関数をT(n)とした時に、その中の処理は上記のようになる
        eq1. T(n) = T(n/2) + 1
            この1は定数倍の物を指している。T(n/2)はnを/2して、ifでどちらかを選ぶため
        eq2. T(n/2) = T(n/4) + 1
        eq3. T(n/4) = T(n/8) + 1
        base. T(1) = 1

    これを展開していく
        T(n) = T(n/2) + 1
            = (T(n/4) + 1) + 1
            = (T(n/8) + 1) + 2
            = T(n/8) + 3

        これを関数に一般化すると次になる
        T(n) = T(n/2^k) + k
        
        n/2^k = 1とすると、T(1) = 1が代入できるので、kを求める
            n = 2^k
            k = log2n
        kを式に代入するとこうなる。log2の基数である2は定数倍なので考慮しない。
        T(n) = T(1) + logn
            = 1 + logn
        以上を持って下記と計算量が証明される
        T(n) = logn