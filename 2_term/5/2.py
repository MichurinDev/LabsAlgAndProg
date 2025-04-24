# 9. Создать текстовый файл, содержащий некоторую информацию. Используя стек, создать 
# другой текстовый файл, в котором строки были бы записаны в обратном порядке.

from stack import Stack

stack = None

with open('input.txt', encoding='utf-8') as f:
    lines = f.readlines()
    stack = Stack(len(lines))
    for line in lines:
        stack.push(line)

with open('output.txt', 'w', encoding='utf-8') as f:
    for _ in range(stack.size):
        el = stack.pop()
        f.write(el)

print('Готово!')
