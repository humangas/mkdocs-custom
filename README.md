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
