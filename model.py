def func1(value):
    factorial = 1
    for k in range(1, value+1):
         factorial *= k
    return k


if __name__ == '__main__':
    print(func1(5))
