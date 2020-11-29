from .basequeue import *
from heapq import *
from .exceptions import PriorityQueueError


class PriorityQueue(Queue):
    '''Variant of Queue that retrieves open entries in priority order (lowest first).

    Entries are typically tuples of the form:  (priority number, data).
    '''

    def __init__(self, *args, maxsize=0):
        super().__init__(maxsize)
        self.queue = heapify(list(args))

    def __str__(self):
        return 'PriorityQueue(' + ' '.join([str(i) for i in self.queue]) + ')'

        # for checking if the queue is empty

    def isEmpty(self):
        return len(self.queue) == [] 

    '''# for inserting an element in the queue 
    def insert(self, data): 
        self.queue.append(data) 

    # for popping an element based on Priority 
    def delete(self): 
        try: 
            max = 0
            for i in range(len(self.queue)): 
                if self.queue[i] > self.queue[max]: 
                    max = i 
            item = self.queue[max] 
            del self.queue[max] 
            return item 
        except IndexError: 
            print() 
            exit()'''

    def _qsize(self):
        return len(self.queue)

    def _put(self, item):
        if self.maxsize and self.qsize < self.maxsize:
            heappush(self.queue, item)
            return self
        else: raise PriorityQueueError('Queue is full.')

    def _get(self):
        if self.qsize() > 0: return heappop(self.queue)
        raise PriorityQueueError('Underflow due to Empty Queue')