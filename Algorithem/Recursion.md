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