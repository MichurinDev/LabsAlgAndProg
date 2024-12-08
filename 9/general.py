import re
# Быть целым числом.
num = '123'
pattern = r'^-?\d+$'
print(bool(re.match(pattern, num)))

# Быть вещественным числом.
num = '123.0932'
pattern = r'^-?\d+(\.\d+)?$'
print(bool(re.match(pattern, num)))

# Быть правильным телефонным номером (например, 37-81-40).
num = '3-81-40'
pattern = r'^\d{1,2}-\d{1,2}-\d{1,2}$'
print(bool(re.match(pattern, num)))

# Быть правильным телефонным номером с кодом города (например (231) 5-94-00).
num = '(231) 5-94-00'
pattern = r'^\(\d{3}\) \d{1,2}-\d{1,2}-\d{1,2}$'
print(bool(re.match(pattern, num)))

# Не содержать цифр.
s = 'hello@'
pattern = r'^[^0-9]*$'
print(bool(re.match(pattern, s)))

# Не содержать букв.
s = '123@'
pattern = r'^[^a-zA-Z]*$'
print(bool(re.match(pattern, s)))
