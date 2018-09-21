class Stack:
    def __init__(self, original=None):
        if type(original) is Stack:
            self.elements = original.elements[:]
        else:
            self.elements = []
        self.size = len(self.elements)

    def push(self, element):
        self.elements.append(element)
        self.size += 1

    def top(self):
        try:
            return self.elements[self.size-1]
        except IndexError:
            print("The stack is empty")
            return None

    def pop(self):
        try:
            self.elements.pop(self.size-1)
            self.size -= 1
        except IndexError:
            print("The stack is empty")

    def __str__(self):
        return str(self.elements) + " <- top"
