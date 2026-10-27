class Node:
    def __init__(self, value=1, next=None):
        self.value = value
        self.next = next

    def setNext(self, next=None):
        self.next = next