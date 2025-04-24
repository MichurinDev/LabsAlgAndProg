class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None for _ in range(self.size)]

    def push(self, elem):
        self.stack = self.stack[1:] + [elem]
    
    def pop(self):
        pop_el = [i for i in self.stack if i != None][-1]
        self.stack[self.stack.index(pop_el)] = None
        return pop_el

    def print_stack(self):
        for _ in range(len([i for i in self.stack if i != None])):
            print(self.stack.pop())
