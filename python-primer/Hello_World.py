# print("Hello, World,This is my first Program!")
# print("I am learning Python Programming Languages.")

# x = 5
# y = "hello"
# z = 3.14

# Data types in Python:
# - int: for integers (whole numbers) like 5, -3, 0
# - str: for strings (text) like "hello", "Python"
# - float: for floating-point numbers (decimal numbers) like 3.14, -0.001

# print(type(x))
# print(type(y))
# print(type(z))

# value = 12
# print(value, type(value))

# value = 'Hello just reassigned the value'
# print(value, type(value))

# value = 3.14
# print(value, type(value))

# #
# def describe_variable(var):
#     if isinstance(var, int):
#         return "The variable is an integer."
#     elif isinstance(var, str):
#         return "The variable is a string."
#     elif isinstance(var, float):
#         return "The variable is a float."
#     else:
#         return "Unknown type."


# print(describe_variable(10))
# print(describe_variable("hello"))
# print(describe_variable(3.14))
# print(describe_variable([1, 2, 3]))


# # a = 5        # int
# # b = 2.5      # float
# # c = "7"      # str containing a number

# # Convert string to integer
# c_int = int(c)
# print(c_int, type(c_int))

# # Convert integer to float
# a_float = float(a)
# print(a_float, type(a_float))

# # Convert float to integer
# b_int = int(b)
# print(b_int, type(b_int))

# a = 5
# b = 2.5
# c = "7"

# print(a + b)          # ✅ 7.5  — Python handles int + float automatically
# # print(a + c)        # ❌ TypeError — can't add int + str directly
# print(a + int(c))     # ✅ 12   — convert first, then add
# print(a + b + int(c)) # ✅ 14.5 — all three together
