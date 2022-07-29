# 内包表記

# ORM で取得した値と仮定
users = [
    {'id': 1, 'name': 'tom', 'email': 'tom@gmail.com', 'age': 23 },
    {'id': 2, 'name': 'ken', 'email': 'ken@gmail.com', 'age': 52 },
    {'id': 3, 'name': 'jun', 'email': 'jun@gmail.com', 'age': 11 },
    {'id': 4, 'name': 'bob', 'email': 'bob@gmail.com', 'age': 36 },
    {'id': 5, 'name': 'ted', 'email': 'ted@gmail.com', 'age': 44 },
]

# 30歳以歳の人の email リストを取得

# forを使った書き方
emails = []
for user in users:
    if user['age'] < 30:
        emails.append(user['email'])
print(emails)

# リスト内法表記
young_user_email = [user['email'] for user in users if user['age'] < 30]
print(young_user_email)

# 辞書内包表記
# 辞書にすると、idをkeyにして、時間計算量O(1)でアクセスできる
user_key_by_id = {user['id']: user for user in users}
print(user_key_by_id)

# セット内包表記
# 一意な名前の集合を取得する
name_set = {user['name'] for user in users}
print(name_set)
