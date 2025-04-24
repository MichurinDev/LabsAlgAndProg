# Очередь:
# 9. Создать очередь для символов. Максимальный размер очереди вводится с 
# экрана. Создать функции для ввода, вывода и определения размера очереди. 
# Вводить символы с экрана в очередь. В случае совпадения вводимого символа с 
# последним элементом очереди выводить размер очереди.


class Queue:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size

    def enqueue(self, elem) -> str:
        if self.if_full():
            return "Full"

        self.queue = [elem] + self.queue
        return "Ok"

    def dequeue(self):
        if self.size() != 0:
            self.queue = self.queue[:-1]

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
            print('Очередь пуста')
        while self.size() != 0:
            print(self.bottom())
            self.dequeue()


max_size = int(input('Введите максимальный размер очереди: '))
queue = Queue(max_size)

while True:
    action = input('Введите действие: 1 - добавить, 2 - убрать, 3 - определить размер очереди, 4 - вывод, :q - выход: ')
    if action == ':q':
        break

    if action == '1':
        elem = input('Введите символ: ')
        print(queue.enqueue(elem))
    elif action == '2':
        queue.dequeue()
    elif action == '3':
        print(f'Размер очереди: {queue.size()}')
    elif action == '4':
        queue.print()
