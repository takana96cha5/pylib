# 以下のような email があったりなかったりなリストがあったとき

users = [
    {'id': 1, 'name': 'tom', 'email': 'tom@yahoo.co.jp', 'age': 23 },
    {'id': 2, 'name': 'ken', 'age': 52 },
    {'id': 3, 'name': 'jun', 'email': 'jun@gmail.com', 'age': 11 },
    {'id': 4, 'name': 'bob', 'email': 'bob@gmail.com', 'age': 36 },
    {'id': 5, 'name': 'ted', 'age': 44 },
]

# gmailを使っている人の数を調べたい
same_email_concat = len([user for user in users if 'gmail.com' in user['email']])
# > KeyError: 'email'

# emailの登録がない人は除外する(例外を吐かせない)
same_email_concat = len([user for user in users if 'gmail.com' in user.get('email', '')])

# -----------------------------------------------------------------------------------------------

# 不等式を直感的に書く

# ORM で取得した値と仮定
users = [
    {'id': 1, 'name': 'tom', 'email': 'tom@gmail.com', 'age': 23 },
    {'id': 2, 'name': 'ken', 'email': 'ken@gmail.com', 'age': 52 },
    {'id': 3, 'name': 'jun', 'email': 'jun@gmail.com', 'age': 11 },
    {'id': 4, 'name': 'bob', 'email': 'bob@gmail.com', 'age': 36 },
    {'id': 5, 'name': 'ted', 'email': 'ted@gmail.com', 'age': 44 },
]

# 数学的な不等式の書き方ができる
for user in users:
    if 25 <= user.get('age', 0) <= 35:
        print(user)
