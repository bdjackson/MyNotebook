class node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def append_to_tail(self, new_data):
        last_node = self
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = node(new_data)

    def delete_node(self, node_itr):
        if node_itr < 0:
            return

        if self.next is None:
            print 'Error! Cannot delete last node in this way'
            return

        # special case for node_itr == 0
        if node_itr == 0:
            self.data = self.next.data
            self.next = self.next.next
            return

        previous_node = None
        this_node = self
        for itr in xrange(node_itr):
            if this_node.next is None:
                print 'Error! Invalid node'
                return
            previous_node = this_node
            this_node = this_node.next

        previous_node.next = this_node.next

    def print_list(self):
        this_node = self
        node_number = 0
        while this_node is not None:
            print node_number, ' : ', this_node.data
            this_node = this_node.next
            node_number += 1


if __name__ == '__main__':
    test_list = node(0)
    for i in xrange(1,10):
        test_list.append_to_tail(i)
    test_list.print_list()
    print

    test_list.delete_node(3)
    test_list.print_list()
    print

    test_list.delete_node(6)
    test_list.append_to_tail(99)
    test_list.print_list()
    print
