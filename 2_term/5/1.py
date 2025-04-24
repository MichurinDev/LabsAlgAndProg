# Стэк:
# 20. Создать стек для символов. Максимальный размер стека вводится с экрана. Создать 
# функции для ввода и вывода элементов стека. Ввести эталонный символ. Вводить символы 
# с экрана в стек до встречи эталонного. Вывести все элементы стека. Задачу решить с 
# использованием механизма указателей.

from stack import Stack

size = int(input('Введите размер стека: '))
stack = Stack(size)
trigger_symbol = input('Введите эталонный символ: ')

while True:
    command = input(f"Добвить/убрать ({trigger_symbol} для выхода): ")
    if command == 'убрать':
        stack.pop()
    elif command == 'добавить':
        el = input('Введите элемент: ')
        stack.push(el)
    elif command == "trigger_symbol":
        stack.print_stack()
