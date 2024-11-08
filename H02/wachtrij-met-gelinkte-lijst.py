class QueueList:
    
    class Knoop:
        def __init__(self, data=None, volgende=None):
            self.data = data
            self.volgende = volgende
    
    def __init__(self):
        self.head = None
        self.tail = None

    def empty(self):
        return self.head is None

    def enqueue(self, data):
        if self.empty() :
            self.head = self.Knoop(data)
            self.tail = self.head
        else :
            self.tail.volgende = self.Knoop(data)
            self.tail = self.tail.volgende
        
    def front(self):
        return self.head.data

    def dequeue(self):
        val = self.head.data
        self.head = self.head.volgende
        if self.empty() :
            self.tail = None
        return val
        
    def invert(self) :
        head = self.head
        prev = None
        while head is not None :
            temp = head.volgende
            head.volgende = prev
            prev = head
            head = temp
        self.head, self.tail = self.tail, self.head