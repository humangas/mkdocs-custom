```
$ pip install -U git+https://github.com/humangas/mkdocs-custom.git
$ mkdocs-custom install
```


# mkdocs-custom
[MkDocs](http://www.mkdocs.org/)は、非常にシンプルなFlat File CMSです。  
デフォルトでも十分ですが、以下の気になった点を修正・補完してすぐに使えるようにしたものがコレです。

- 日本語検索対応
- [便利そうなJSライブラリの使い方サンプルをまとめた（説明のみ）](http://humangas.github.io/mkdocs-custom/)
- 便利そうなJSライブラリを予めセット（基本はCDNでやる）

ただし、`theme: readthedocs`でないと上手く動かないことが多かったです。その辺は自分で調整してください。


# Instration
```
$ pip install -U git+https://github.com/humangas/mkdocs.git@custom
```

# Usage
mkdocsと全く同じですが、ざっと書いておきます。

```
# プロジェクト作成
mkdocs new <project name>

# docs/配下にコンテンツ作成
# 静的ファイルにビルド
mkdocs build --clean

# 静的ファイルをブラウザで表示
mkdocs serve
```

# このサンプルをローカルで試す
buildして、Webサーバ起動して、ブラウザで見るが面倒なので簡易スクリプト化しました。
でも、一発だけやれば良くて、一度Webサーバ起動した後に、docs配下を編集すると保存タイミングで自動ビルドされます。
```
$ git clone https://github.com/humangas/mkdocs-custom.git
$ cd mkdocs-custom
$ bash build_local-test.sh
```

# サンプルの更新（自分用）
docs配下を修正し、それをgh-pagesにUPする時、手順が多く面倒なので簡易スクリプト化しました。
```
$ git clone https://github.com/humangas/mkdocs-custom.git
$ cd mkdocs-custom
$ bash build_gh-pages.sh
```
