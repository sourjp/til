# はじめに
ここがわかりやすい  
https://qiita.com/takamii228/items/80c0996a0b5fa39337bd

# Git Branchが最新状態か確認する

git branch --containes=HEAD


#  branchを作成する
git checkout -b feature/{branchname}

branch規則はポリシーに従う

# branchでの作業終了後に最新状態に適用
git fetch

git rebase origin/master

# branchにpushする
git push origin feature/{branchname}

# PRを投げる
gitからPRサイトにcompare対象に自分のbranchを選んでPRを投げる