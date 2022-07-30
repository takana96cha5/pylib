
# デコレータで処理を囲む

# おしゃれなログを出したい...
from logging import exception
from my_decorator import logger

@logger('-')
def simple_sum1(x: int, y: int) -> int:
    return x + y

@logger('+')
def simple_sum2(x: int, y: int) -> int:
    return x + y

if __name__ == '__main__':
    simple_sum1(10, 29)
    simple_sum2(10, 29)

# with句で処理を囲む

from contextlib import contextmanager

@contextmanager
def exception_logger(separator: str = '-'):
    try:
        # 事前処理
        print(10 * separator)
        yield
    except Exception as e:
        print(f'何らかの例外が発生: {e}')
    finally:
        # 事後処理
        print(10 * separator)

if __name__ == '__main__':
    with exception_logger('*'):
        print(1/0)

# ファイルのハンドリングは　 　with で実装されている

# databaseと通信する場合にもデコレータは使える、事前処理でトランザクションを開く　例外が発生したらロールバックをかける　正常ならコミット　最終的にセッションは必ず閉じる　みたいな感じで

