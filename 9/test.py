import re

pattern = r'^([1-9]{1}[0-9]{2}-){2}[1-9]{1}[0-9]{2} [0-9]{2}$'
line = input("Введите номер СНИЛС: ")

print(bool(re.match(pattern, line)))
