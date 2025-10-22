class QueueUsingStack:
    def _init_(self):
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
        return self.s2.pop()  # ✅ Pop from end of s2

q = QueueUsingStack()
q.enqueue(10)
q.enqueue(20)
print(q.dequeue())
