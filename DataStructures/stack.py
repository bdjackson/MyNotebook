from linked_list import node

class stack(object):
    def __init__(self):
        self.data = None

    def is_empty(self):
        return self.data is None

    def push(self, new_data):
        if self.is_empty():
            self.data = node(new_data)
        else:
            new_node = node(new_data)
            new_node.next = self.data
            self.data = new_node

    def pop(self):
        return_value = self.data.data
        self.data = self.data.next
        return return_value

if __name__ == '__main__':
    test_stack = stack()
    for i in xrange(10):
        test_stack.push(i)
    while not test_stack.is_empty():
        print test_stack.pop()
