from collections import deque

class Queue:
    def __init__(self):
        self._elements = deque()
        
    def enqueue(self, element):
         self._elements.append(element)
         
    def dequeue(self):
        return self._elements.popleft()
    
# from queues import Queue

# create object
# fifo = Queue()

# access methods by putting item on queue
# fifo.enqueue(1)
# fifo.enqueue(2)
# fifo.dequeue(3)

# remove the first item on queue
# fifo.dequeue(1)
# fifo.dequeue(2)
# fifo.dequeue(3)
