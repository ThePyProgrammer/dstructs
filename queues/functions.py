# =================== QUEUE FUNCTIONS ===================
def reverseQueue(q):
    '''Recursive Function to reverse a queue.'''

    # Base case
    if q.isEmpty():
        return

    data = q.get()  # Dequeue current item (from front)
    reverseQueue(q)  # Reverse remaining queue
    q.put(data)  # Enqueue current item (to rear)


def FrontToLast(q, qsize):
    """Function to push element in last by
    popping from front until size becomes 0"""

    # Base condition
    if qsize <= 0:
        return

    q.put(q.get())  # pop front element and push this last in a queue
    FrontToLast(q, qsize - 1)  # Recursive call for pushing element


def pushInQueue(q, temp, qsize):
    """Function to push an element in the queue
    while maintaining the sorted order"""

    # Base condition
    if q.empty() or qsize == 0:
        q.put(temp)
        return

    # If current element is less than
    # the element at the front
    elif temp <= q.front():
        q.put(temp)  # Call stack with front of queue

        # Recursive call for inserting a front
        # element of the queue to the last
        FrontToLast(q, qsize)

    else:
        q.put(q.get())  # Push front element into last in a queue

        # Recursive call for pushing
        # element in a queue
        pushInQueue(q, temp, qsize - 1)


def Queue_heappush(*args): return pushInQueue(*args)


def sortQueue(q):
    """Function to sort the given
    queue using recursion"""

    # Return if queue is empty
    if q.empty():
        return

    # Get the front element which will
    # be stored in this variable
    # throughout the recursion stack
    temp = q.get()

    # Recursive call
    sortQueue(q)

    # Push the current element into the queue
    # according to the sorting order
    pushInQueue(q, temp, q.size())