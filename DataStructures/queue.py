from linked_list import node

class queue(object):
    def __init__(self):
        self.data = None
        self.last_node = None

    def is_empty(self):
        return self.data is None

    def enqueue(self, new_data):
        if self.data is None:
            self.data = node(new_data)
            self.last_node = self.data
        else:
            self.last_node.next = node(new_data)
            self.last_node = self.last_node.next

    def dequeue(self):
        if self.is_empty():
            return None
        return_value = self.data.data
        self.data = self.data.next
        return return_value

if __name__ == '__main__':
    test_queue = queue()
    for i in xrange(10):
        test_queue.enqueue(i)
    while not test_queue.is_empty():
        print test_queue.dequeue()
