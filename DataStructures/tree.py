from queue import queue
from collections import deque
from enum import Enum

# ------------------------------------------------------------------------------
class binary_tree(object):
    """
    binary_tree

    class to represent a binary tree. Each node in the tree is represented by
    a binary_tree object, and points to it's adjacent neighbors.
    Note: There is no link backward in the tree!
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def data_for_output(self):
        if isinstance(self.data, str):
            return self.data
        if isinstance(self.data, int):
            return '%02d' % self.data
        return self.data

    def print_tree(self):
        """
        Function to print a binary tree. The function steps through the full
        tree, and constructs a string to be printed for each line.
        --
        None: This does not work well for unbalanced tree
        """
        nodes = queue()

        list_of_out_strings = [[self.data_for_output()],[]]

        nodes.enqueue(self)
        nodes.enqueue(None)

        while not nodes.is_empty():
            this_node = nodes.dequeue()
            if this_node is None:
                list_of_out_strings.append([])
                if not nodes.is_empty():
                    nodes.enqueue(None)
                continue

            if this_node.left is not None:
                list_of_out_strings[-1].append(this_node.left.data_for_output())
                nodes.enqueue(this_node.left)
            else:
                list_of_out_strings[-1].append('--')

            if this_node.right is not None:
                list_of_out_strings[-1].append(this_node.right.data_for_output())
                nodes.enqueue(this_node.right)
            else:
                list_of_out_strings[-1].append('--')

        if len(list_of_out_strings[-1]) == 0:
            list_of_out_strings.pop()
        list_of_out_strings.pop()

        num_rows = len(list_of_out_strings)
        seperator_len = 1
        for index, out_string in enumerate(reversed(list_of_out_strings)):
            modify_index = num_rows - 1 - index

            padding_len = seperator_len - 1
            seperator_len = seperator_len*2 + 2
            seperator = ' '*seperator_len
            padding = ' '*padding_len

            updated_string = ''.join([padding, seperator.join(out_string)])
            string_length = len(updated_string)
            list_of_out_strings[modify_index] = updated_string

        for out_string in list_of_out_strings:
            print out_string


# ------------------------------------------------------------------------------
class binary_search_tree(binary_tree):
    """
    binary_search_tree

    Class to represent a binary search tree. This class is not auto-balanced, so
    it needs to be filled carefully, or it will either be unbalanced.
    """
    def __init__(self, data):
        if isinstance(data,list):
            super(binary_search_tree, self).__init__(data=data[0])
            for this_data in data[1:]:
                self.add_node(this_data)
        else:
            super(binary_search_tree, self).__init__(data=data)

    def add_node(self, new_data):
        if new_data <= self.data:
            if self.left is None:
                self.left = binary_search_tree(new_data)
            else:
                self.left.add_node(new_data)
        else:
            if self.right is None:
                self.right = binary_search_tree(new_data)
            else:
                self.right.add_node(new_data)

# ------------------------------------------------------------------------------
# color enum
# 
# Used to auto-balance a binary search tree using the red/black tree structure
# ------------------------------------------------------------------------------
color = Enum('black', 'red')

# ------------------------------------------------------------------------------
class binary_search_tree_red_black(binary_tree):
    """
    binary_search_tree_red_black

    Class to represent a binary search tree. This class uses the red/black tree
    structure to auto-balance the tree
    """
    def __init__(self, data):
        super(binary_search_tree, self).__init__(data=data)
        self.color = color.red

        print self.data
        print self.color

def construct_tree_pre_order(pre_order_list):

    if pre_order_list is None:
        return None

    if not isinstance(pre_order_list, deque):
        pre_order_list = deque(pre_order_list)

    if len(pre_order_list) == 0:
        return None

    next_value = pre_order_list.popleft()
    if next_value is None:
        return None

    tree = binary_tree(next_value)

    left_branch = construct_tree_pre_order(pre_order_list)
    if not left_branch is None:
        tree.left = left_branch

    right_branch = construct_tree_pre_order(pre_order_list)
    if not right_branch is None:
        tree.right = right_branch

    return tree

if __name__ == '__main__':
    test_tree = binary_tree(1)
    test_tree.left = binary_tree(2)
    test_tree.right = binary_tree(3)
    test_tree.print_tree()
    print

    test_tree = construct_tree_pre_order([0, 1, 3, None, None, 4, None, None,
                                          2, 5, None, None, 6, None, None])
    test_tree.print_tree()
    print

##      0
##     / \
##    1   2 
##   / \ / \
##   3 4 5 6
## 
##   0 1 3 None None 4 None None 2 5 None None 6 None None

    test_tree = construct_tree_pre_order([0, 1, 3, None, None, 4,
                                          7, None, None, 8, None, None,
                                          2, 5, 9, None, None, 10,
                                          None, None, 6, None, None])
    test_tree.print_tree()
    print

##        0
##     /     \
##    1       2 
##   / \     / \
##  3   4   5   6
##     / \ / \
##     7 8 9 10
## 
##   0 1 3 None None 4 7 None None 8 None None 2 5 9 None None 10 None None 6 None None

    test_tree = construct_tree_pre_order([0, 1, 3, None, None, 4,
                                          7, 11, None, None, 12, None, None,
                                          8, None, None,
                                          2, 5, 9, None, None, 10,
                                          None, None, 6, None, None])
    test_tree.print_tree()
    print "Unbalanced trees don't print very well :-("
    print

##         0
##      /     \
##     1       2 
##    / \     / \
##   3   4   5   6
##      / \ / \
##      7 8 9 10
##     / \
##    11 12
##
##   0 1 3 None None 4 7 11 None None 12 None None 8 None None 2 5 9 None None 10 None None 6 None None

    print 'The next trees should match'
    test_tree = binary_search_tree(5)
    test_tree.add_node(3)
    test_tree.add_node(7)
    test_tree.add_node(2)
    test_tree.add_node(1)
    test_tree.add_node(4)
    test_tree.add_node(6)
    test_tree.add_node(8)
    test_tree.add_node(9)
    test_tree.print_tree()
    print

    test_tree = binary_search_tree([5, 3, 7, 2, 1, 4, 6, 8, 9])
    test_tree.print_tree()
    print

    test_tree = binary_search_tree([5, 3, 2, 1, 4, 7, 6, 8, 9])
    test_tree.print_tree()
    print

##     [1, 2, 3, 4, 5, 6, 7, 8, 9]
## 
##         5
##     3       7
##   2   4   6   8
## 1               9
## 
## 
## [5, 3, 7, 2,1, 4, 6, 8, 9]
