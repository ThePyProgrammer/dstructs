from .basequeue import Queue

__all__ = [
    'LifoQueue',
    'StackQueue'
]


class LifoQueue(Queue):
    """Variant of Queue that retrieves most recently added entries first, i.e. a Stack"""

    def _qsize(self):
        return len(self.queue)

    def _put(self, item):
        self.queue.append(item)

    def _get(self):
        return self.queue.pop()


class StackQueue(LifoQueue): pass