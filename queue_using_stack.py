class QueueUsingStack:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, x):
        self.s1.append(x)

    def dequeue(self):
        if not self.s2:
            if not self.s1:
                return "Empty"
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop(0)  # ❌ Wrong pop index

q = QueueUsingStack()
q.enqueue(10)
q.enqueue(20)
print(q.dequeue())  # Expected 10
