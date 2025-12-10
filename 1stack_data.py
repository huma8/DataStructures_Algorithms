#burada yapılacakları pythondaki list ile yapabilirsin. ben javadan dinlediğim için ona uygun olması için özel sınıf oluşturacağım.
#append, pop vb.

#LIFO(Last In, First out) -> Listeye en son giren en ilk çıkar.
class Stack:
    def __init__(self):
        self.data = []

    def push(self, arg):
        self.data.append(arg)

    def pop(self):
        if not self.data:
            raise IndexError("Cannot pop from an empty stack")
        return self.data.pop()

    def peek(self):
        if not self.data:
            return None
        return self.data[-1]

    def is_empty(self):
        if self.data:
            return False
        else:
            return True

    def size(self):
        return len(self.data)

stack = Stack()

stack.push("a")
stack.push("b")
stack.push("c")
stack.push("d")
stack.push("e")
print(f"{stack.data}\n")
stack.pop()
print(f"{stack.data}\n")
print(stack.peek())
print(f"Size of the Stack: {stack.size()}")
print(stack.is_empty())
stack.pop()
stack.pop()
stack.pop()
stack.pop()
print(f"Size of the Stack: {stack.size()}")
print(stack.is_empty())
