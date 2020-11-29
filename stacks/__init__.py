from .linked_stack import LinkedStack
from .stack_using_dll import Stack as ST  # DLLStack
from .exceptions import StackError
from .stack import Stack
from collections import deque
from Lib.dstructs import StackQueue

__all__ = ['LinkedStack', 'DLLStack', 'Stack', 'Deque', 'QueueStack']


class QueueStack(StackQueue): pass
class Deque(deque): pass
class DLLStack(ST): pass
