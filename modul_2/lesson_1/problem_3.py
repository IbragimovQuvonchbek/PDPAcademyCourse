class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0


def test_queue():
    q = Queue()

    assert q.size() == 0
    assert q.is_empty() == True

    q.enqueue(1)
    assert q.size() == 1
    assert q.is_empty() == False

    q.enqueue(2)
    q.enqueue(3)
    assert q.size() == 3
    assert q.dequeue() == 1
    assert q.size() == 2

    assert q.dequeue() == 2
    assert q.size() == 1

    assert q.dequeue() == 3
    assert q.size() == 0
    assert q.is_empty() == True

    assert q.dequeue() == None

    print("All tests passed.")


if __name__ == '__main__':
    test_queue()
