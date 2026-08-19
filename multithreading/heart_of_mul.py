'''
1.Race Condition
2.Synchronization
3.Lock
4.RLock
'''
#Why we need synchronization?
'''
balance = 1000
Thread-1 -- withdrawl 500
Thread-2 -- withdrawl 700

Both are accessing the same  variable without proper control
Incorrect balance
Wrong transactions
data corrupt

to avoid the above we will use:
synchronization: this is a process of contolling access the shared resources so that only one thread modifies at a time

Lock:
hared
resoures:
any variable,file,database,object

Example:
count = 0
if multiples threads modifies count simultaneously

#Race Condition:
occurs when multiple threads access and modify shared data simultaneously causing unpredictable
outputs


'''
count = 0
count +=1
print(count)
#write with threads
import threading
count = 0
def increament():
    global count
    count +=1
threads = []
for i in range(1000):
    t = (threading.Thread(target=increament))
    threads.append(t)
    t.start()
for t in threads:
    t.join()
print(count)   

'''
998
994
998

'''
'''
critical section:
code section where shared resources are accessed is called critical section
count +=1 -->critical section

To avoid the race condition?
one thread should enter the critical section at a time
solution:lock

what is lock?
synchronization Mechanism
that allows only one thread to execute a critical section at a time

Thread A acquires Lock
other Threads will wait
Thread A releases lock
next thread gets lock

import threading
lock = threading.Lock()

#to apply lock
lock.acquire()

# to release
lock.release()


'''
import threading
count = 0
lock = threading.Lock()
def increament():
    global count
    for i in range(10000):
        lock.acquire()
        count +=1
        lock.release()
t1 = threading.Thread(target=increament)
t2 = threading.Thread(target=increament)
t1.start()
t2.start()   
t1.join()
t2.join()
print(count)
#bank example 
class Bank:
    def __init__(self):
        self.balance =1000
    def withdraw(self,amount):
        if self.balance>= amount:

            self.balance -= amount    

import threading
class Bank:
    def __init__(self):
        self.balance = 1000
        self.lock = threading.Lock()
    def withdraw(self,amount):
        with lock:
            if self.balance>=amount:
                self.balance -=amount
                print(amount,"Withdrawl")
            else:
                print("Insufficient Balance")
bank = Bank()
t1 = threading.Thread(target = bank.withdraw,args =(700,))
t2 = threading.Thread(target = bank.withdraw,args =(500,))
t1.start()
t2.start()
t1.join()
t2.join()
print(bank.balance)

'''
Deadlock:
where the threads wait forever fo locks
Thread 1
lock A
waiting for lock B

hread 2:
lock B
waiting for lock A

Thread 1--->waiting lock A
Thread 2--->waiting lock B
deadlock

RLock: Recursive Lock
A thread can aquire the same lock multiple times

why RLock:
Normal Lock
acquire once
release once

if same thread acquires again deadlock


'''
# import threading

# lock = threading.Lock()
# def outer():
#     lock.acquire()
#     inner()
#     lock.release()
# def inner():
#     lock.acquire()
#     print("Inner")
#     lock.release()
# outer()
'''
Outer () acquired the lock
inner () trying to acquire the same lock
lock is already head above
wait forever

'''
lock = threading.RLock()
def inner():
    with lock:
        print("inner")
def outer():
    with lock:
        print("outer")
        inner()
outer()
