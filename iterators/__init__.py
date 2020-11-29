from more_itertools import flatten

class _BaseIterator(object):
    def __init__(self, *args):
        self.queue = list(args[::-1])
        self.next = self.__next__
        self.peek = self.front

    def __iter__(self): return self
    def __next__(self):
        try: return self.queue.pop()
        except: raise StopIteration

    def has_next(self): return bool(self.queue)
    def front(self): return self.queue[-1]

    def __len__(self): return len(self.queue)
    def __contains__(self, item): return item in self.queue

    def __getitem__(self, key): return self.queue[-1-key]      
    def __setitem__(self, key, value): self.queue[-1-key] = value
    def __delitem__(self, key): del self.queue[-1-key]




class ZigZagIterator(_BaseIterator):
    def __init__(self, v1, v2):
        super().__init__(reversed(i) for i in (v1,v2) if i)

    def __next__(self):
        v = self.queue.pop(0)
        ret = v.pop()
        if v: self.queue.append(v)
        return ret

    def __len__(self): return len(flatten(self.queue))
    def __contains__(self, item): return item in flatten(self.queue)
    
    def front(self): return self.queue[0][-1]



class Series(_BaseIterator):
    def __init__(self, *args):
        if len(args) == 1:
            start, step = 0, 1
            stop = args

        if len(args) == 2:
            step = 1
            start, stop = args

        else:
            start, stop, step = args
        super().__init__(*range(start, stop+1, step))



class Count(_BaseIterator):
    """Iterator that counts upward forever."""

    def __init__(self, start=0):
        super().__init__()
        self.num = self.start = start

    def __next__(self):
        num = self.num
        self.num += 1
        return num

    def __len__(self): return self.num+1-self.start
    def __contains__(self, item): return type(item) == int and item >= self.start

    def front(self): return self.num



class PowTwo(_BaseIterator):
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max = 0):
        self.max = max
        self.n = 0

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration
