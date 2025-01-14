
import functools


def fib_elem_gen():
    """Генератор, возвращающий элементы ряда Фибоначчи"""
    a = 0
    b = 1

    while True:
        yield a
        res = a + b
        a = b
        b = res


def my_genn():
    while True:
        number_of_fib_elem = yield
        fib_gen = fib_elem_gen()
        l = [next(fib_gen) for i in range(number_of_fib_elem)]
        yield l


def fib_coroutine(g):
    @functools.wraps(g)
    def inner(*args, **kwargs):
        gen = g(*args, **kwargs)
        gen.send(None)
        return gen
    return inner


class EvenNumbersIterator():
    def __init__(self, instance):
        self.instance = instance
        self.fib_gen = fib_elem_gen()
        self.fib_set = set()
        self.maximum = max(instance)
        self.insert_fib_set()

    def __iter__(self):
        return self

    def __next__(self):
        for res in self.instance:
            if res in self.fib_set:
                self.instance.remove(res)
                return res
        raise StopIteration

    def insert_fib_set(self):

        while True:
            fib_num = next(self.fib_gen)
            if fib_num > self.maximum:
                break
            self.fib_set.add(fib_num) 


if __name__ == '__main__':
    my_genn = fib_coroutine(my_genn)
    gen = my_genn()
    num = int(input())
    print(gen.send(num))

    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    fib_iterator = EvenNumbersIterator(lst)

    print("Элементы ряда Фибоначчи из списка:", list(fib_iterator))
