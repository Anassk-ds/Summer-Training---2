from threading import Thread, Lock

balance = 0
lock = Lock()

class Withdraw(Thread):
    def _init_(self, amount):
        super()._init_()
        self.amount = amount

    def run(self):
        global balance

        with lock:
            if balance >= self.amount:
                balance -= self.amount
                print(self.amount, "withdrawn")
            else:
                print("Insufficient Balance")

balance = int(input())
n = int(input())

threads = []

for i in range(n):
    amount = int(input())
    t = Withdraw(amount)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Final Balance:", balance)