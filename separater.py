import sys
import os
from collections import defaultdict

# ==================== 各種設定 ====================

# 入力ログファイルのパス
input_path = './example.com.access_log'

# 出力ディレクトリ
output_dir = './output'

# 出力ファイルの拡張子(開きたいエディタに合わせると便利)
output_ext = '.txt'

# True:  wwwありに統一
# False: wwwなしに統一
www = False

# True:  出力ファイルを上書き
# False: 同名ファイルが存在する場合はスキップ
overwrite = False

# ==================================================


# 第2引数: 入力ファイルパス, 第3引数: 出力ディレクトリに設定
if len(sys.argv) >= 2:
    input_path = sys.argv[1]
if len(sys.argv) >= 3:
    output_dir = sys.argv[2]
input_file = os.path.basename(input_path)
input_ext = os.path.splitext(input_file)[1]

# ログを辞書型に整理
# {'domain': ['log', 'log', ...],
#  'domain': ['log', 'log', ...],
#  ...}
try:
    with open(input_path, buffering=1, encoding='utf-8') as f:
        d = defaultdict(list)
        for line in f:
            domain = line.split()[0]
            d[domain].append(line)
except FileNotFoundError as e:
    print(f'ファイル{e.filename}の読み込みに失敗しました。')
    print('第2引数にパスを指定するか、input_path変数の値を修正してください。')
    sys.exit(1)

# wwwの有無を統一
main_domain = os.path.splitext(input_file)[0]
www_domain = f'www.{main_domain}'
if www:
    d[www_domain] += d.pop(main_domain)
else:
    d[main_domain] += d.pop(www_domain)

# 書出し
if not os.path.exists(output_dir):
    os.mkdir(output_dir)
for domain in d:
    output_file = f'{output_dir}/{domain}{input_ext}{output_ext}'
    if overwrite or not os.path.isfile(output_file):
        with open(output_file, mode='w') as f:
            f.writelines(d[domain])
    else:
        print(f'{output_file}は存在します。上書きする場合は、overwrite変数の値をTrueに書き換えてください。')
