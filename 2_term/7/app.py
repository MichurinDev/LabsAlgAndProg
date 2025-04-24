# Дэк:
# 9. Создать дек для символов. Максимальный размер дека вводится с экрана. Создать 
# функции для ввода, вывода и определения размера дека. Добавлять символы в дек 
# поочередно справа и слева. В случае совпадения добавляемого символа с элементом на 
# другом конце дека выводить размер дека.

class Dek:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size

    def enqueue_left(self, elem) -> str:
        if self.if_full():
            return "Full"

        self.queue = [elem] + self.queue
        return "Ok"

    def enqueue_right(self, elem) -> str:
        if self.if_full():
            return "Full"

        self.queue = self.queue + [elem]
        return "Ok"

    def dequeue_right(self):
        if self.size() != 0:
            self.queue = self.queue[:-1]

    def dequeue_left(self):
        if self.size() != 0:
            self.queue = self.queue[1:]

    def size(self):
        return len(self.queue)
    
    def if_full(self):
        return self.size() == self.max_size

    def top(self):
        if self.size() != 0:
            return self.queue[0]
        return None

    def bottom(self):
        if self.size() != 0:
            return self.queue[-1]
        return None
    
    def print(self):
        if self.size() == 0:
            print('Дек пуст')
        while self.size() != 0:
            print(self.top())
            self.dequeue_left()


max_size = int(input('Введите максимальный размер дека: '))
dek = Dek(max_size)

while True:
    action = input('Введите действие: 1 - добавить слева, 2 - добавить справа, 3 - убрать слева, 4 - убрать справа, 5 - определить размер дека, 6 - вывод, :q - выход: ')
    if action == ':q':
        break

    if action == '1':    
        elem = input('Введите символ: ')
        print(dek.enqueue_left(elem))
    elif action == '2':
        elem = input('Введите символ: ')
        print(dek.enqueue_right(elem))
    elif action == '3':
        dek.dequeue_left()
    elif action == '4':
        dek.dequeue_right()
    elif action == '5':
        print(dek.size())
    elif action == '6':
        dek.print()
