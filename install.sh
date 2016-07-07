# 日本語検索対応ローカライズしたmkdocsをインストール

pip install git+xxixx

#markdown, grphvizの拡張はいれるかどうかは検討、入れる場合は、pip install もするけど、それはcloneした後に、requiremtns.txtからやる

# mkdocs+ custom版のjsが組み込まれたベースをインストール
git clone XX

# サンプルは、gh-pagesに書いておくので、そっちのほうにソースサンプルはいれる
# ソースサンプルはsrcだな

# READMEには、curl install.sh | bashでインストールしろだけ書く
# ドキュメントは、gh-pagesに飛ばす
# cdnのソースの有りかはそっちに書く
# ネットつながる環境のはずなので、そっちでもいいが、サンプルではソースも入れておく
# mkdocs.ymlには、cdn版にしといて、自分でいれる版は、mkdocs.yml-download-srcとかにしといてサンプル扱いにする
# -> そうすれば、ソース修正は、gh-pagesのサンプル版だけで良くて、使い方がわかれば、正直extara_jsは不要になる。
# -> ついでに、マニュアルにあんま書いていないそこのサンプルだけ書いとけばいい
# あとは、やり方を載せておけばよし




