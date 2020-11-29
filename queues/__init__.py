from queue import Queue as queue
from queue import SimpleQueue


from .exceptions import *
from .basequeue import *
from .priority_queue import PriorityQueue
from .circular_queue import CircularQueue
from .linked_queue import LinkedQueue
from .queue_on_list import ListQueue
from .queue_on_pseudo_stack import *
from .lifo import *
from .functions import *
from .exceptions import QueueError

__all__ = [
    'queue',
    'reverseQueue',
    'sortQueue',
    'Queue',
    'PriorityQueue',
    'StackQueue',
    'LifoQueue',
    'SimpleQueue',
    'Deque',
    'CircularQueue',
    'LinkedQueue',
    'ListQueue',
    'PSQueue',
    'QueueError',
    'PseudoStackQueue'
]
# ========================================================================