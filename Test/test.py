def func():
    for i in range(10):
        yield i


if __name__ == '__main__':
    lst = func()
    print(list(lst))

    