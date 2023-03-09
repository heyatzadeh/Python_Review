def decorateZeroDivisionError(func):
    def inner_fuc(x, y):
        if y == 0:
            print("Unable to divide")
            return
        return func(x, y)

    return inner_fuc


@decorateZeroDivisionError
def operation(x, y):
    return x / y


print(operation(2, 20))
print(operation(2, 10))
print(operation(23, 20))
print(operation(2, 0))
print(operation(y=0, x=10))
