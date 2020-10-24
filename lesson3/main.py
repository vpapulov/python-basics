from functools import lru_cache

NEW_FILTER_MODE_ODD = "odd"
NEW_FILTER_MODE_EVEN = "even"
NEW_FILTER_MODE_PRIME = "prime"


def execution_time(func):
    from time import time
    from functools import wraps
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(func, "execution time = ", end_time - start_time)
        return result

    return wrapper


def trace(func):
    from functools import wraps
    @wraps(func)
    def wrapper(*args, **kwargs):
        if wrapper.level == 0:
            print(">>> {0}({1})".format(func.__name__, args[0]))
        print("____" * wrapper.level, "--> {0}({1})".format(func.__name__, args[0]))
        wrapper.level += 1
        result = func(*args, **kwargs)
        wrapper.level -= 1
        print("____" * wrapper.level, "<-- {0}({1}) == {2}".format(func.__name__, args[0], result))
        return result

    wrapper.level = 0
    return wrapper


@execution_time
def new_power(*numbers, power=2) -> list:
    from itertools import repeat
    return list(map(pow, numbers, repeat(power)))


#    return list(map(lambda x: x ** power, numbers))
#    return [n**power for n in numbers]

def new_filter(numbers: list, mode) -> list:
    if mode == NEW_FILTER_MODE_ODD:
        return list(filter(lambda n: n % 2 == 0, numbers))
    elif mode == NEW_FILTER_MODE_EVEN:
        return list(filter(lambda n: n % 2 == 1, numbers))
    elif mode == NEW_FILTER_MODE_PRIME:
        return list(filter(is_prime, numbers))
    else:
        return numbers


def is_prime(number) -> bool:
    if number <= 1:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


@trace
@lru_cache(maxsize=1000)
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    print("new_power:", new_power(123, 456, power=5))

    lst = list(range(50))
    print("list = ", lst)
    print("new_filter odd:", new_filter(lst, NEW_FILTER_MODE_ODD))
    print("new_filter even:", new_filter(lst, NEW_FILTER_MODE_EVEN))
    print("new_filter prime:", new_filter(lst, NEW_FILTER_MODE_PRIME))

    print("fib(3):", fib(3))
