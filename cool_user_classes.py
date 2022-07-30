# イケてるクラス
# オブジェクト指向はプログラムを主語と動詞で表現するスタイル
# ある情報をいかにして別のデータ構造に知らせるかというメッセージングの手段　SOLID原則

from bisect import bisect_right
from datetime import date, timedelta
from time import time
from urllib.parse import uses_relative

# 普通に実装したクラス(イケてないクラス)
class User:
    def __init__(self, id: int = 0, email: str = '', first_name: str = '', last_name: str = '', birthday: date = date.today()):
        self.id = id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self._birthday = birthday
    
    def name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def set_name(self, _name: str) -> None:
        if ' ' not in _name:
            raise Exception('invalid fullname error')
        self.first_name, self.last_name = _name.split(' ')

    def age(self) -> int:
        timedelta = date.today() - self._birthday
        return timedelta.days // 365
    
    def birthday(self) -> date:
        return self._birthday
    
    def set_birthday(self, birthday: date) -> None:
        self._birthday = birthday

    def log(self) -> None:
        print(f'User<id: {self.id}, email: {self.email}, name: {self.name()}, age: {self.age()}>')

# _____________________________________________________________

# pythonicなイケてるクラス
from datetime import date
from dataclasses import dataclass

@dataclass
class User:
    """"イケてるユーザークラス"""
    id: int = 0
    email: str = ''
    first_name: str = ''
    last_name: str = ''
    _birthday: date = date.today()

    @property
    def name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    @name.setter
    def name(self, _name: str) -> None:
        if ' ' not in _name:
            raise Exception('invalid fullname error')
        self.first_name, self.last_name = _name.split(' ')

    @property
    def age(self) -> int:
        timedelta = date.today() - self._birthday
        return timedelta.days // 365

    @property
    def birthday(self) -> date:
        return self._birthday
    
    @birthday.setter
    def birthday(self, birthday: date) -> None:
        self._birthday = birthday
    
    def __repr__(self) -> str:
        return f'User<id: {self.id}, email: {self.email}, name: {self.name()}, age: {self.age()}>'
        
    
user = User()
user.id = 1
user.email = 'sample@sample.com'
user.first_name = 'john'
user.last_name = 'smith'
user.birthday = date(2000, 1, 23)
print(user)