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

import threading as th

def fibonacci(n):
    if n<=0:
        return[]
    elif n==1:
        return[0]
    elif n==2:
        return[0,1]
    else:
        fib_list = [0,1]
        for i in range(2,n):
            fib_list.append(fib_list[i-1]+fib_list[i-2])
        return fib_list
def calculate_fib(n):
    result = fibonacci(n)
    print(f"fibonacci series of {n} is {result}")

if __name__ == "__main__":
    n=int(input("enter the number of fibonacci terms  to generate:"))
    t = th.Thread(target=calculate_fib,args=(n,))
    t.start()
    t.join()
    print("Done!")