from collections import deque
from heapq import heappop, heappush

class Queue:
    def __init__(self, *elements):
        self._elements = deque(elements)
    
    def __len__(self):
        return len(self._elements)
    
    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()
    
    def enqueue(self, element):
         self._elements.append(element)
         
    def dequeue(self):
        return self._elements.popleft()
    
class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()

class PriorityQueue:
    def __init__(self):
        self._elements = []
        
    def enqueue_with_priority(self, priority, value):
        heappush(self._elements, (priority, value))
        
    def dequeue(self):
        return heappop(self._elements)
    
    
    
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

#fifo = Queue(1,2,3)
#len(fifo)
#for element in fifo:
#   print(element)
#len(fifo)

#from queue import Stack
#lifo = Stack(1,2,3)

#from queues import PriorityQueue

# CRITICAL = 3
# IMPORTANT = 2
# NEUTRAL = 1

# messages = PriorityQueue()
# messages.enqueue_with_priority(IMPORTANT, "Windshield wipers turned on")
# messages.enqueue_with_priority(NEUTRAL, "Radio station tuned in")
# messages.enqueue_with_priority(CRITICAL, "Brake pedal depressed")
# messages.enqueue_with_priority(IMPORTANT, "Hazard lights turned on")

# messages.dequeue()