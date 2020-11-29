from .circular_linked_list import CircularLinkedList
from .doubly_linked_list import LinkedList as dll1
from .singly_linked_list import LinkedList as sll1

__all__ = ['CLL', 'DoublyLinkedList', 'DLL', 'SinglyLinkedList', 'SLL', 'LinkedList']


class CLL(CircularLinkedList): pass
class DoublyLinkedList(dll1): pass
class DLL(dll1): pass
class SinglyLinkedList(sll1): pass
class SLL(sll1): pass


class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        self.head = Node(item, self.head)

    def remove(self):
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next
            return item

    def is_empty(self):
        return self.head is None
