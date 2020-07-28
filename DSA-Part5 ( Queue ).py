import time
import threading
from collections import deque
class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    
    def front(self):
        return self.buffer[-1]

# --------------------------------------------------------------- #
# Printing Binary Numbers

def ProduceBinaryNumbers(n):
    numbers = Queue()
    numbers.enqueue('1')

    for i in range(n):
        front = numbers.front()
        print( i+1 ,":",front)
        numbers.enqueue(front + "0")
        numbers.enqueue(front + "1")
        numbers.dequeue()

ProduceBinaryNumbers(30)

input("\nPress Any Other Button To Start Producer-Consumer Problem\n")
# --------------------------------------------- #
# Producer-Consumer Problem


def PlaceOrders(orders):
    for n in orders:
        q.enqueue(n)
        print("Placing Order for", n)
        time.sleep(0.5)

def ServeOrders():
    while not q.is_empty():
            print("Serving",q.dequeue())
            time.sleep(2)

if __name__ is '__main__':
    q = Queue()
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1 = threading.Thread(target=PlaceOrders,args=(orders,))
    t2 = threading.Thread(target=ServeOrders)
    t1.start()
    time.sleep(1)
    t2.start()
