__author__ = "Omkar Pathak"

import math

from .exceptions import StackError


class Node:
    # Constructor which assign argument to node's value
    def __init__(self, value):
        self.value = value
        self.next = None

    # This method returns the string representation of the object.
    def __str__(self):
        if type(self) == str: return f"'{self}'"
        return str(self)

    #  __repr__ is same as __str__
    __repr__ = __str__


class Stack:
    """ A stack is an abstract data type that serves as a collection of
    elements with two principal operations: push() and pop(). push() adds an
    element to the top of the stack, and pop() removes an element from the top
    of a stack. The order in which elements come off of a stack are
    Last In, First Out (LIFO).

    https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
    """

    def __init__(self, *args, limit=0):
        if len(args) - 1 and type(args[0]) not in [list, tuple, dict]: args = tuple(Node(i) for i in args)
        self.list = list(args)
        self.limit = limit
        self.isEmpty = self.empty = self.is_empty
        self.add = self.append = self.insert = self.put = self.delete = self.push
        self.get = self.next = self.remove = self.pop
        self.qsize = self.size = self.__len__
        self.front = self.peek
        self.minimum = 10000000000000000000000
        self.maximum = -10000000000000000000000
        self.top = None

    def __str__(self): return 'Stack('+', '.join([str(i) for i in self]) + ')'
    __repr__ = __str__
    def __len__(self): return len(self.list)

    def __int__(self):
        self = Stack(int(i) for i in self)
        return self

    def __next__(self):
        try:
            return self.pop()
        except:
            raise StopIteration

    def __iter__(self): return self.copy()

    def push(self, data):
        """ Push an element to the top of the stack."""
        if self.limit == 0:
            if len(self.list) >= self.limit:
                raise StackError('Stack is full')
        data = Node(data)
        self.list.append(data)
        return self

    def extend(self, *args):
        for i in args: self.push(i)
        return self

    def __pos__(self):
        return self

    def __neg__(self):
        copy = Stack([-i for i in self], limit=self.limit)
        return copy

    def __abs__(self):
        copy = Stack([abs(i) for i in self], limit=self.limit)
        return copy

    def __round__(self):
        copy = Stack([round(i) for i in self], limit=self.limit)
        return copy

    def __floor__(self):
        copy = Stack([math.floor(i) for i in self], limit=self.limit)
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
        if type(value) in [Stack, list, tuple, dict]:
            self.limit += value.limit if type(value) == Stack else 0
            self.extend(*value)

        else:
            self.push(value)

        return self

    def __add__(self, value):
        copy = self.copy()
        if type(value) in [Stack, list, tuple, dict]:
            copy.limit += value.limit if type(value) == Stack else 0
            copy.extend(*value)

        else:
            copy.append(value)
        return copy

    def __radd__(self, value):
        if type(value) in [Stack]:
            copy = value.copy()
            copy.limit += value.limit
            copy.extend(*self)
        else:
            copy = Stack([value]+list(self))
        return copy

    def __imul__(self, value):
        try:
            for i in range(len(self)): self[i] *= value
        except Exception as e:
            raise StackError(e)

        return self

    def __mul__(self, value):
        copy = self.copy()
        try:
            for i in range(len(copy)): copy[i] *= value
        except Exception as e:
            raise StackError(e)
        return copy

    def __rmul__(self, value):
        copy = self.copy()
        try:
            for i in range(len(copy)): copy[i] *= value
        except Exception as e:
            raise StackError(e)
        return copy

    def __idiv__(self, value):
        try:
            for i in range(len(self)): self[i] /= value
        except Exception as e:
            raise StackError(e)

        return self

    def __div__(self, value):
        copy = self.copy()
        try:
            for i in range(len(copy)): copy[i] /= value
        except Exception as e:
            raise StackError(e)
        return copy

    def __itruediv__(self, value):
        try:
            for i in range(len(self)): self[i] //= value
        except Exception as e:
            raise StackError(e)

        return self

    def __truediv__(self, value):
        copy = self.copy()
        try:
            for i in range(len(copy)): copy[i] //= value
        except Exception as e:
            raise StackError(e)
        return copy

    def __imod__(self, value):
        try:
            for i in range(len(self)): self[i] %= value
        except Exception as e:
            raise StackError(e)

        return self

    def __mod__(self, value):
        copy = self.copy()
        try:
            for i in range(len(copy)): copy[i] %= value
        except Exception as e:
            raise StackError(e)
        return copy

    def __ipow__(self, value):
        try:
            for i in range(len(self)): self[i] **= value
        except Exception as e:
            raise StackError(e)

        return self

    def __pow__(self, value):
        copy = self.copy()
        try:
            for i in range(len(copy)): copy[i] **= value
        except Exception as e:
            raise StackError(e)
        return copy

    def __rpow__(self, value):
        copy = self.copy()
        try:
            for i in range(len(copy)): copy[i] = value ** copy[i]
        except Exception as e:
            raise StackError(e)
        return copy

    def __iand__(self, value):
        try:
            for i in range(len(self)): self[i] &= value
        except Exception as e:
            raise StackError(e)

        return self

    def __ior__(self, value):
        try:
            for i in range(len(self)): self[i] |= value
        except Exception as e:
            raise StackError(e)

        return self

    def __ixor__(self, value):
        try:
            for i in range(len(self)): self[i] ^= value
        except Exception as e:
            raise StackError(e)

        return self

    def __ilshift__(self, value):
        try:
            for i in range(len(self)): self[i] >>= value
        except Exception as e:
            raise StackError(e)

        return self

    def __irshift__(self, value):
        try:
            for i in range(len(self)): self[i] <<= value
        except Exception as e:
            raise StackError(e)

        return self

    def rotate(self, rotation=None):
        if rotation is not None:
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
        copy = Stack(*list(self), limit=self.limit)
        return copy

    def __call__(self, index):
        return self[index]

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_val, trace):
        while self: self.get()
        del self

    def peek(self):
        """ Peek at the top-most element of the stack."""
        if self:
            return self[-1]
        return

    def is_empty(self):
        """ Check if a stack is empty."""
        return not bool(self)


if __name__ == "__main__":
    stack = Stack()
    for i in range(10):
        stack.push(i)

    print("Stack demonstration:\n")
    print("Initial stack: " + str(stack))
    print("pop(): " + str(stack.pop()))
    print("After pop(), the stack is now: " + str(stack))
    print("peek(): " + str(stack.peek()))
    stack.push(100)
    print("After push(100), the stack is now: " + str(stack))
    print("is_empty(): " + str(stack.is_empty()))
    print("size(): " + str(stack.size()))
