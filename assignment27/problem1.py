from threading import Thread

class Student(Thread):
    def __init__(self, name, m, p, c):
        super().__init__()
        self.name = name
        self.m = m
        self.p = p
        self.c = c

    def run(self):
        total = self.m + self.p + self.c
        avg = total / 3

        if avg >= 40:
            result = "PASS"
        else:
            result = "FAIL"

        print(self.name, total, result)

n = int(input())

threads = []

for i in range(n):
    data = input().split()
    name = data[0]
    m = int(data[1])
    p = int(data[2])
    c = int(data[3])

    t = Student(name, m, p, c)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Result Processing Completed")