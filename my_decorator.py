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
