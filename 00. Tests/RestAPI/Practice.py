import re


def reverse_number(num):
    new_num = 0
    while num > 0:
        keep = num % 10
        new_num = new_num * 10 + keep
        num = num // 10
    return new_num


def combine_even_and_odd_list(first_list, second_list):
    combined = [x for x in first_list if x % 2 != 0] + [x for x in second_list if x % 2 == 0]
    print(combined)


def calculate_tax(num, tax=0):
    if num <= 10000:
        print(tax)
        return tax

    elif num <= 20000:
        num -= 10000
        tax += num * 0.1
        calculate_tax(num, tax)

    else:
        tax += (num - 20000) * 0.2
        calculate_tax(num - (num - 20000), tax)


def multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i}*{j}={i * j}", end=" ")

        print('\n')


def downward_half_pyramid(n):
    for i in range(n):
        for j in range(n - i):
            print('*', end="")
        print()


def the_pow_function(num, power):
    result = 1
    for i in range(power):
        result *= num

    print(result)


def print_two_decimal_number(n):
    print("%.2f" % n)


def pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


def multiplication_number(n):
    for i in range(11):
        print(f"{n} * {i} = {i * n}")


def iterate(foo_list):
    for i in foo_list:
        if i > 100:
            break
        elif i % 5 == 0:
            print(i)

    result = [x for x in foo_list if x % 5 == 0 and x < 100]
    return result


def count_digit(n):
    sum_number = 0
    while n > 0:
        sum_number += n % 10
        n //= 10
    return sum_number


def another_pattern(n):
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()


def another_pattern1(n):
    for i in range(1, n + 1):
        for j in range(1, n - i + 1):
            print(j, end=" ")
        print()


def reverse_list(foo_list):
    result = []
    for i in range(len(foo_list), 0, -1):
        result.append(foo_list[i - 1])

    return result


def prime_number(n):
    for number in range(2, n + 1):
        for j in range(2, number):
            if number % j == 0:
                break
        else:
            print(number)


def is_prime(n, i=2):
    if n <= 2:
        return True if n == 2 else False
    if i >= n:
        return True
    if n % i == 0:
        return False
    return is_prime(n, i + 1)


def prime_number_rec(n):
    for number in range(n):
        if is_prime(number):
            print(number)


def final_pattern(n):
    for i in range(n):
        for j in range(i):
            print("*", end=" ")
        print()
    for i in range(n):
        for j in range(n - i):
            print("*", end=" ")
        print()


def number_of_args(*args):
    for i in args:
        print(i)


def multiply_return(foo, bar):
    return foo - bar, foo + bar


def outer_calculation(foo, bar):
    def inner_calculation():
        return foo + bar

    return inner_calculation() + 5


def recursive_sum_calculator(n):
    if n == 0:
        return 0
    return n + recursive_sum_calculator(n - 1)


def generate_even_list(start, end):
    return [x for x in range(start, end) if x % 2 == 0]


def largest_number(foo_list):
    local_max = 0
    for i in foo_list:
        if i > local_max:
            local_max = i
    return local_max


def repeat_in_string(foo_str: str) -> dict:
    result = dict()
    for char in foo_str:
        result[char.lower()] = result.get(char.lower(), 0) + 1
    return result


def reverse_string(foo_str: str) -> str:
    result = str()
    for i in range(len(foo_str) - 1, 0, -1):
        result += foo_str[i]
    return result


def last_position_of_word(foo_str: str, word: str):
    return re.finditer(word, foo_str)


while next(last_position_of_word("hossein and ali are hossein", "hossein")):
    pass

# print(next(last_position_of_word("hossein and ali are hossein", "hossein")))
