# xserver_log_separater

XSEVERのログファイルをサブドメインごとのファイルに分割します。

## 説明

サーバーパネルの`アクセス解析->アクセスログ`からダウンロードできるログファイルはドメイン単位です。  
そのため複数のサブドメインを運用している場合、それらは1つのファイルにまとめられてしまいます。  
これではサブドメインごとのログを別々に見ることができません。  
`separater.py`は、XSERVERからダウンロードしたログファイルをサブドメイン単位に分割し、別々のファイルに保存し直すことでこの問題を解決します。

## 環境

- Python 3.6+

## 使用方法

```
$ git clone https://github.com/mikiya1130/xserver_log_separater
$ cd xserver_log_separater
$ python separater.py /../example.com.access_log
$ ls output
```

## その他

入力ファイルパスと出力ディレクトリは引数に指定可能です。
```
$ python separater.py input_path output_dir
```
省略した場合は、それぞれスクリプト内の変数input_pathと変数output_dirの値が利用されます。

## ライセンス

Unlicense
