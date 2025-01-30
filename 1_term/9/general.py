import re
# Быть целым числом.
num = '123'
pattern = '^-?[0-9]+$'
print(bool(re.match(pattern, num)))

# Быть вещественным числом.
num = '123.0932'
pattern = '^-?[0-9]+(\.[0-9]+)?$'
print(bool(re.match(pattern, num)))

# Быть правильным телефонным номером (например, 37-81-40).
num = '3-81-40'
pattern = '^[0-9]{1,2}-[0-9]{1,2}-[0-9]{1,2}$'
print(bool(re.match(pattern, num)))

# Быть правильным телефонным номером с кодом города (например (231) 5-94-00).
num = '(231) 5-94-00'
pattern = '^\([0-9]{3}\) [0-9]{1,2}-[0-9]{1,2}-[0-9]{1,2}$'
print(bool(re.match(pattern, num)))

# Не содержать цифр.
s = 'hello@'
pattern = '^[^0-9]*$'
print(bool(re.match(pattern, s)))

# Не содержать букв.
s = '123@'
pattern = '^[^a-zA-Z]*$'
print(bool(re.match(pattern, s)))
