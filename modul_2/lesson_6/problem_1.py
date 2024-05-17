from datetime import datetime


def log(func):
    def wrapper(*args, **kwargs):
        print(f"- called function: {func.__name__} at {datetime.now().strftime('%H:%M:%S')}")
        result = func(*args, **kwargs)
        print(f"- finished function: {func.__name__} at {datetime.now().strftime('%H:%M:%S')}")
        return result

    return wrapper


@log
def hello():
    print("hello")


if __name__ == '__main__':
    hello()
