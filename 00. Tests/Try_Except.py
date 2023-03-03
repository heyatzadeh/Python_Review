import sys
from timeit import timeit

# try:
#     age = int(input("Age:"))
# except ValueError as exce_Error:
#     print("Value Error Here")
#     print(exce_Error)
#     print(sys.exc_info()[0])
#     print(sys.exc_info()[1])
#     print(type(exce_Error))
# else:
#     print('Another Error Accord')

# ----------------------------------------------------------------

# items = ['ali', 0, 2]
#
# for item in items:
#     try:
#         r = 0 / item
#     except Exception as e:
#         print(e.__class__)

# ----------------------------------------------------------------

# try:
#     x = int(input("inter a number: "))
#     z = 10 / x
# except (ValueError, ZeroDivisionError) as ex:
#     print(type(ex))
# else:
#     print(sys.exc_info()[0])

# ----------------------------------------------------------------

# array = ["ali", 0, "0"]
#
# for item in array:
#     try:
#         file = open("some_random_file.txt")
#         10 / int(item)
#     except (ValueError, ZeroDivisionError) as e:
#         print(e.__class__)
#     else:
#         print("No Error")
#     finally:
#         file.close()
#         print("in final")

# ----------------------------------------------------------------

# array = ["ali", 0, "0"]
#
# for item in array:
#     try:
#         with open("some_random_file.tx") as note:
#             print("note Opened")
#         10 / int(item)
#     except (ValueError, ZeroDivisionError) as e:
#         print(e.__class__)
#     except Exception as e:
#         print(e.__class__)
#     else:
#         print("No Error")
#     finally:
#         print("in final")

# ----------------------------------------------------------------

# def validate_age(age):
#     if age < 1:
#         raise ValueError("Age is not less than one!")
#     return age
#
#
# try:
#     validate_age(0)
# except ValueError as e:
#     print(e)
# else:
#     print("No Error!")

# ----------------------------------------------------------------

test_run1 = """
array = [10, 10, 10]

for item in array:
    try:
        10 / int(item)
    except Exception as e:
        pass
    else:
        pass
    finally:
        pass
"""
print("Test 1: ", timeit(test_run1, number=100000))

test_run2 = """
array = [10, 10, 10]

for item in array:
    10 / int(item)
"""
print("Test 1: ", timeit(test_run2, number=100000))
