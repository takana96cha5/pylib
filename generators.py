# 事実上無限に長いリストを扱う時にジェネレータは便利

# フィボナッチ数列のように原理的に無限に続く漸化式を扱う
from typing import Generator

def fib_generatator() -> Generator[int, None, None]:
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

# nextを呼ぶたびに都度計算されるのでまるで無限長の数列を扱っている気分になる
fib = fib_generatator()
print(next(fib), next(fib), next(fib), next(fib), next(fib), next(fib), next(fib), next(fib), next(fib), next(fib), next(fib), next(fib), next(fib), next(fib), next(fib), next(fib), next(fib), next(fib), next(fib), next(fib), next(fib), next(fib), next(fib), next(fib))

# 無限に近い長さの配列を扱うとめっちゃメモリを使う
infinit_lsit = [num for num in range(0, 123456789)]
# print(sum(infinit_lsit))
# > 7620789313366866

# ジェネレータ式にすると、必要な時に値を必要な分だけ取得できる
# 非同期のプログラミングで別の処理の後に戻ってきたりとか
infinit_generator = (num for num in range(0, 123456789))
# > generator(...)
# 上の計算は実は全然メモリを使っていない

# 実は  jsの非同期処理で使う async await は generator の応用

# －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－

# 特定の要素を抜き出す

# 次のようなリストがあったとする
users = [
    {'id': 1, 'name': 'tom', 'email': 'tom@gmail.com', 'age': 23 },
    {'id': 2, 'name': 'ken', 'email': 'ken@gmail.com', 'age': 52 },
    {'id': 3, 'name': 'jun', 'email': 'jun@gmail.com', 'age': 11 },
    {'id': 4, 'name': 'bob', 'email': 'bob@gmail.com', 'age': 36 },
    {'id': 5, 'name': 'ted', 'email': 'ted@gmail.com', 'age': 44 },
]

# ジェネレータ式の応用で、年齢が25歳の人を一人だけ取得する、いなければ初期値の None を返す この書き方だと一発で辞書のデータを取得できる
user = next((user for user in users if user.get('age', 0) == 25), None)
