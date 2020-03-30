# なにそれ？
簡単にいうとCSSをプログラムチックにかけるようにした書式
代表的な部分は変数化や、階層構造があげられる
例えば次のようなscssファイルがあった場合、それを次のcssファイルに書き換える

この時CSSファイルは成果物であるため操作しない
操作する対象はSCSSファイルのみとする

```test.scss
$cWhite: white;
$cBlack: black;

#container {
    text-align: center;
}
.btn {
    background-color: $cWhite;
    color: black;
    border: 1px solid $cBlack;
    padding: 10px 40px;
    margin: 10px 40px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s;

    &:hover {
        background-color: black;
        color: white;
    }
}
```

```style.css
#container {
  text-align: center;
}

.btn {
  background-color: white;
  color: black;
  border: 1px solid black;
  padding: 10px 40px;
  margin: 10px 40px;
  font-weight: 600;
  cursor: pointer;
  -webkit-transition: all 0.3s;
  transition: all 0.3s;
}

.btn:hover {
  background-color: black;
  color: white;
}
/*# sourceMappingURL=style.css.map */
```