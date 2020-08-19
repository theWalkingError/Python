# Декоратор - функция, которая принимает в качестве аргуемента другую функцию


def decorator(func):
    def wrapper():
        print("До начала времен...")
        func()
        print("После окончания времен...")
    return wrapper


def decorator_2(func):
    def wrapper():
        print("Брехня 1")
        func()
        print("Брехня 2")
    return wrapper


@decorator_2
@decorator
def main_func():
    print("Мы где-то тута")


main_func()
