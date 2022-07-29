
# デコレータで処理を囲む

# おしゃれなログを出したい...

from functools import wraps

def logger(separator: str = '-'):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # 事前処理
            print(10 * separator)
            result = func(*args, **kwargs)
            # 事後処理
            print(result)
            print(10 * separator)
            return result
        return wrapper
    return decorator


@logger('-')
def simple_sum1(x: int, y: int) -> int:
    return x + y

@logger('+')
def simple_sum2(x: int, y: int) -> int:
    return x + y

if __name__ == '__main__':
    simple_sum1(10, 29)
    simple_sum2(10, 29)

