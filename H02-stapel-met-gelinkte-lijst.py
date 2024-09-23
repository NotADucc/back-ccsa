class StackList:
    
    class Knoop:
        def __init__(self, data=None, volgende=None):
            self.data = data
            self.volgende = volgende
    
    def __init__(self):
        self.head = None

    def empty(self):
        return self.head is None

    def push(self, data):
        temp = self.Knoop(data, self.head)
        self.head = temp
        
    def peek(self):
        return self.head.data

    def pop(self):
        val = self.head.data
        self.head = self.head.volgende
        return val
    