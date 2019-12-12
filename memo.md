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