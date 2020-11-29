from queue import Queue as queue
from collections import deque
import math
from .exceptions import QueueError

__all__ = [
    'QueueError',
    'Queue',
    'Deque'
]


class Deque(deque): pass


class Queue(queue):
    def __init__(self, *args, maxsize=0):
        super().__init__(maxsize)
        self.isEmpty = self.empty
        self.add = self.append = self.insert = self.enqueue = self.push = self.delete = self.put
        self.pop = self.next = self.dequeue = self.deque = self.get
        self.size = self.__len__ = self.qsize
        self.index = self.queue.index
        self.count = self.queue.count
        for i in args: self.put(i)

    def __repr__(self):
        return str(self)

    def __int__(self):
        for i in self: self.put(int(self.get()))
        return self

    def __del__(self):
        del self.queue

    @property
    def front(self):
        try:
            return self.queue[0]
        except:
            raise QueueError("This queue is empty.")

    @property
    def peek(self):
        return
    def peek(self):
        return self.front

    def __bool__(self):
        return not self.empty()

    def __iter__(self):
        return iter(list(self.queue))

    def __next__(self):
        try:
            return self.get()
        except:
            raise StopIteration

    def __eq__(self, other):
        return list(other.queue) == list(self.queue)

    def __ne__(self, other):
        return list(other.queue) != list(self.queue)

    def __lt__(self, other):
        return list(other.queue) > list(self.queue)

    def __gt__(self, other):
        return list(other.queue) < list(self.queue)

    def __le__(self, other):
        return list(other.queue) >= list(self.queue)

    def __ge__(self, other):
        return list(other.queue) <= list(self.queue)

    def __contains__(self, item):
        return item in list(self.queue)

    def __getitem__(self, key):
        return self.queue[key]

    def __setitem__(self, key, value):
        self.queue[key] = value

    def __delitem__(self, key):
        del self.queue[key]

    def __reversed__(self, key=lambda x: x):
        return self.copy().reverse()

    def extend(self, *args):
        for i in args: self.push(i)
        return self

    def __pos__(self):
        return self

    def __neg__(self):
        copy = self.copy()
        for i in range(len(copy)):
            self.push(self.get() * (-1))
        return copy

    def __abs__(self):
        copy = self.copy()
        for i in range(len(copy)):
            self.push(abs(self.get()))
        return copy

    def __round__(self):
        copy = self.copy()
        for i in range(len(copy)):
            self.push(round(self.get()))
        return copy

    def __floor__(self):
        copy = self.copy()
        for i in range(len(copy)):
            self.push(math.floor(self.get()))
        return copy

    def __ceil__(self):
        copy = self.copy()
        for i in range(len(copy)):
            self.push(math.ceil(self.get()))
        return copy

    def __trunc__(self):
        copy = self.copy()
        for i in range(len(copy)):
            self.push(math.trunc(self.get()))
        return copy

    def __iadd__(self, value):
        if type(value) in [Queue, list, tuple, dict]:
            self.maxsize += value.maxsize if type(value) == Queue else 0
            self.extend(*value)

        else:
            self.push(value)

        return self

    def __add__(self, value):
        copy = self.copy()
        if type(value) in [Queue, list, tuple, dict]:
            copy.maxsize += value.maxsize if type(value) == Queue else 0
            copy.extend(*value)

        else:
            copy.push(value)
        return copy

    def __radd__(self, value):
        if type(value) in [Queue]:
            copy = value.copy()
            copy.maxsize += value.maxsize
            copy.extend(*self)
        else:
            copy = self.copy()
            copy.push(value)
        return copy

    def __imul__(self, value):
        try:
            for i in range(len(self)): self.queue[i] *= value
        except Exception as e:
            QueueError(e)

        return self

    def __mul__(self, value):
        copy = self.copy()
        try:
            for i in range(len(copy.queue)): copy.queue[i] *= value
        except Exception as e:
            QueueError(e)
        return copy

    def __rmul__(self, value):
        copy = self.copy()
        try:
            for i in range(len(copy.queue)): copy.queue[i] *= value
        except Exception as e:
            QueueError(e)
        return copy

    def __idiv__(self, value):
        try:
            for i in range(len(self.queue)): self.queue[i] /= value
        except Exception as e:
            QueueError(e)

        return self

    def __div__(self, value):
        copy = self.copy()
        try:
            for i in range(len(copy.queue)): copy.queue[i] /= value
        except Exception as e:
            QueueError(e)
        return copy

    def __itruediv__(self, value):
        try:
            for i in range(len(self.queue)): self.queue[i] //= value
        except Exception as e:
            QueueError(e)

        return self

    def __truediv__(self, value):
        copy = self.copy()
        try:
            for i in range(len(copy.queue)): copy.queue[i] //= value
        except Exception as e:
            QueueError(e)
        return copy

    def __imod__(self, value):
        try:
            for i in range(len(self.queue)): self.queue[i] %= value
        except Exception as e:
            QueueError(e)

        return self

    def __mod__(self, value):
        copy = self.copy()
        try:
            for i in range(len(copy.queue)): copy.queue[i] %= value
        except Exception as e:
            QueueError(e)
        return copy

    def __ipow__(self, value):
        try:
            for i in range(len(self.queue)): self.queue[i] **= value
        except Exception as e:
            QueueError(e)

        return self

    def __pow__(self, value):
        copy = self.copy()
        try:
            for i in range(len(copy.queue)): copy.queue[i] **= value
        except Exception as e:
            QueueError(e)
        return copy

    def __rpow__(self, value):
        copy = self.copy()
        try:
            for i in range(len(copy.queue)): copy.queue[i] = value ** copy.queue[i]
        except Exception as e:
            QueueError(e)
        return copy

    def __iand__(self, value):
        try:
            for i in range(len(self.queue)): self.queue[i] &= value
        except Exception as e:
            QueueError(e)

        return self

    def __ior__(self, value):
        try:
            for i in range(len(self.queue)): self.queue[i] |= value
        except Exception as e:
            QueueError(e)

        return self

    def __ixor__(self, value):
        try:
            for i in range(len(self.queue)): self.queue[i] ^= value
        except Exception as e:
            QueueError(e)

        return self

    def __ilshift__(self, value):
        try:
            for i in range(len(self.queue)): self.queue[i] >>= value
        except Exception as e:
            QueueError(e)

        return self

    def __irshift__(self, value):
        try:
            for i in range(len(self.queue)): self.queue[i] <<= value
        except Exception as e:
            QueueError(e)

        return self

    def rotate(self, rotation=None):
        if rotation != None:
            for i in range(rotation):
                self.put(self.get())
            return self
        else:
            return self.reverse()

    def __and__(self, value):
        return bool(self) & bool(value)

    def __rand__(self, value):
        return bool(self) & bool(value)

    def __or__(self, value):
        return bool(self) | bool(value)

    def __ror__(self, value):
        return bool(self) | bool(value)

    def __xor__(self, value):
        return bool(self) ^ bool(value)

    def __rxor__(self, value):
        return bool(self) ^ bool(value)

    def __lshift__(self, value):
        return bool(self) << bool(value)

    def __rlshift__(self, value):
        return bool(self) >> bool(value)

    def __rshift__(self, value):
        return bool(self) >> bool(value)

    def __rrshift__(self, value):
        return bool(self) << bool(value)

    def copy(self):
        copy = Queue(maxsize=self.maxsize)
        for i in self.queue:
            copy.push(i)

        return copy

    def __call__(self, index):
        return self[index]

    def __str__(self):
        val = ', '.join([str(i) for i in self.queue])
        return f"Queue({val})"

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_val, trace):
        while self: self.get()
        del self

    def reverse(self):
        '''Recursive Function to reverse a queue.'''

        # Base case
        if (self.isEmpty()):
            return

        data = self.get()  # Dequeue current item (from front)
        self.reverse()  # Reverse remaining queue
        self.put(data)  # Enqueue current item (to rear)
        return self

    def FrontToLast(self, qsize):
        '''Function to push element in last by
        popping from front until qsize becomes 0'''

        # Base condition
        if qsize <= 0:
            return self

        self.put(self.get())  # pop front element and push this last in a queue
        return self.FrontToLast(qsize - 1)  # Recursive call for pushing element

    def pushInQueue(self, temp, qsize):
        '''Function to push an element in the queue
        while maintaining the sorted order'''

        # Base condition
        if self.empty() or qsize == 0:
            self.put(temp)
            return self

        # If current element is less than
        # the element at the front
        elif temp <= self.front():
            self.put(temp)  # Call stack with front of queue

            # Recursive call for inserting a front
            # element of the queue to the last
            return self.FrontToLast(qsize)

        else:
            self.put(self.get())  # Push front element into last in a queue

            # Recursive call for pushing
            # element in a queue
            return self.pushInQueue(temp, qsize - 1)

    def sort(self):
        '''Function to sort the given
        queue using recursion'''
        '''
        # Base Case
        if self.empty(): return

        temp = self.get() # Get the front element which will be stored in this variable throughout the recursion stack  
        self.sort() # Recursive call
        self.pushInQueue(temp, self.size()) # Push the current element into the queue according to the sorting order  '''
        self.queue = Deque(sorted(self.queue))
        return self