def func1(value):
    '''this function caclucates factorial'''
    factorial = 1
    for k in range(1, value + 1):
         factorial *= k
    return k


def func2(value):
    '''this function calculates second power of value'''
    square = value * value
    return square



if __name__ == '__main__':
    print(func1(5))
    print(func2(3))

