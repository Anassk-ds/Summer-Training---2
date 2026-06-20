'''
What is a program?
A program is a set of instructions
stored on a disk

print("hello")

storing on a disk???

python hello.py
hello

what is process?
when a program starts executing it becomes
a process
running?
python hello.py
hello

OS --Operating System

Chrome:
vs code:
spotify:
each one is a seperate process

Characterstics:
1.Independent
2.Seperate memory:
chrome:1.8gb, vs-code-500mb
3.Heavy weight:
Memory allocations
resource allocation
cpu Scheduling
what is a thread?
A thread is smallest unit of execution inside a process

Restaurant == Process
worker 1 - Taking the orders
worker 2 - Cooking
worker 3 - Billing
worker 4 - Cleaning

Visually:
Process:
Chrome:
    +thread1
    +thread2
    +thread3

Process             Thread
1.Independent          Part of process
2.Heavy weight          Light weight
3.Seperate memory       Share memory
4.Slow                  Fast
5.Expensive             Cheap
6.Communication         Difficult easy


why threads are faster?
Threads will share the memory
Process needs seperate memory allocation

Concurrency?
Teacher checking the notebooks
student A
student B
student C

Concurrency
A
B
C
A
B
C
one at a time 
rapidly switching
appears simultaneously

CPU -- only one

Parallelism:
cashier 1 --> customer 1
cashier 2 --> customer 2
cashier 3 --> customer 3
truly simultaneous

CPU1 --> Task a
CPU2 --> Task b
CPU3 --> Task c

A
B
A
B
A
B

paralleism:
cpu1 - AAA
Cpu -2 - BBB

Onechef cooking
soup
noodles
fried rice

Parallelism:
Chef 1 - soup
Chef 2 - noodles
Chef 3 - fried rice

python threads will use ---Concurrency
due to GIL -Global interpreter lock
'''
#Creation of threads:
import threading

#Function created (do's nothing)
def display():
    print("Hello")

#Thrad object(creation)
t = threading.Thread(target=display)
#start thread()
print(t)


#Multiple Threads
import threading

def task():
    print("Thread Running")

t1 = threading.Thread(target = task)
t2 = threading.Thread(target = task)
t3 = threading.Thread(target = task)

t1.start()
t2.start()
t3.start()
'''
Main Thread
    + t1
    + t2
    + t3
    all executes independently

'''
#Threads with loops
def numbers():
    for i in range(5):
        print(i)
t = threading.Thread(target = numbers)
t.start()

#Two threads with diff task
def even():
    for i in range(0,10,2):
        print("Even:",i)
def odd():
    for i in range(1,10,2):
        print("Odd:",i)

t1 = threading.Thread(target = even)
t2 = threading.Thread(target = odd)
t1.start()
t2.start()

'''
OS scheduler decides:
which thread to runs first?
'''
import threading
print(threading.current_thread())

#Naming of threads:
import threading
def task():
    print(threading.current_thread().name)

t = threading.Thread(target=task,
                     name="Student_Thread")
t.start()

#passing arguments
def square(n):
    print(n*n)

t = threading.Thread(target = square,
                     args = (5,))

t.start()

#to delay the threads
import time
time.sleep(3)

import threading
import time
def task():
    for i in range(5):
        print(i)
        time.sleep(1)
    
t = threading.Thread(target=task)
t.start()

'''
#retry mechanism:
while True:
    try:
        connect()
    except:
        time.sleep(5)    
'''