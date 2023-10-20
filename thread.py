# single threads

import threading as th
n=int(input("enter range of numbers:"))

def print_num():
    for i in range(1,n):
        print(f"Number: {i}")

td = th.Thread(target=print_num)
td.start()
td.join()


#Multithreading

import threading as th
n=int(input("enter range of numbers:"))

def print_num():
    for i in range(1,n+1):
        print(f"Thread 1: {i}")

def print_let():
    for letter in 'ABCDE':
        print(f"\nThread 2 : {letter}")

th1 = th.Thread(target=print_num)
th2 = th.Thread(target=print_let)

th1.start()
th2.start()
th1.join()
th2.join()

#fibonacci series in threading



