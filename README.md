# lispy

## 概要
PythonをLisp風に書いてみた

## ルール
* ワンライナーでも動作するように書き，改行は可読性のために行う
* ワンライナーにおいて`exec`はチートすぎるので使わない（`eval`はOK）
* ファイルはモジュールに分けてもよいが，それぞれワンライナーでも動作するようにする
* Lisp風の機能を実装するモジュールは`lispy.py`とし，これ自体もLisp風に書く
* Lispと似たような関数を実装するが，戻り値などは完全に同じにはしない（面倒）

## Example
| File | 概要 |
|:--- |:--- |
| marubatu | マルバツゲーム |
| fibonacci.py | フィボナッチ数列の再帰関数 |
| fizzbuzz.py | FizzBuzz |
| to_oneliner.py | 改行を削除してワンライナー化する関数 |
