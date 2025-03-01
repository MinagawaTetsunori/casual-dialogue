# casual-dialogue
- Googleスプレッドシートで作成したチャットボットの対話フローを即試せるコード
- 対話フローの記述方法はcasual-dialogueオリジナルの構成に従う
### 動作確認済み環境
- Python 3.11
- Windows11
- Googleスプレッドシート(2025/1/20 時点での環境)

## 1. 対話フローの作成
Googleスプレッドシートに下図のようなシートを作成
![Image](https://github.com/user-attachments/assets/86c98689-9832-4444-a573-866fef547680)
- `event_id`...`branch`(後述)で分岐するために必要な番地
- `speaker`...誰の発話か分類
  - `bot`...ボット発話、必ず`event_id`内で先頭に1つだけ設ける
  - `user`...ユーザ発話の選択肢、複数設けることができる
- `utt`...utterance(発話)の略、発話する内容の本文
- `branch`...整数の内容によって処理が変わる
  - 1以上...指定`event_id`に遷移する、`bot`の場合はuserに発言権を渡さずに飛ぶ
  - -1...実行終了
  - 0...`bot`にのみ有効、発言権を渡す前提ならこれが入る

## 2. シート内容をTSV形式で貼り付け
- シート内容を全選択後、適当なtsvファイルへコピペして実行ファイルと同じディレクトリに置く
- `tsvs/sample_flow.tsv`内を削除して上書きしてもいい
## 3. 実行
- `tests/sample_code.py`を`tests`ディレクトリ内で実行
- 自作した対話フローファイルを使用したい場合は`tests/sample_code.py`内で`sample_flow.tsv`の表記を自作ファイル名に書き換える
- 選択肢が番号付きで表示されるため、半角数字で入力
```
-------------------------
bot:
こんにちは

user:
1. あいさつする
2. 無視する

choice : 2
-------------------------
bot:
ションボリ
-------------------------
bot:
こんにちは

user:
1. あいさつする
2. 無視する

choice : 1
-------------------------
bot:
ニッコリ
```
