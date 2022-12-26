class LinkedList:
    head = None

    class Node:
        def __init__(self, value=0, next_node=None):
            self.value = value
            self.next_node = next_node

        def __str__(self):  # debugging help
            return 'Node [' + str(self.value) + ']'

    def append(self, value):
        if not self.head:  # first call will return True because head = None
            self.head = self.Node(value)
            return value
        cur_node = self.head
        while cur_node.next_node:
            cur_node = cur_node.next_node
        cur_node.next_node = self.Node(value)

    def length(self):
        if not self.head:
            return 0
        cur_node = self.head
        counter = 1
        while cur_node.next_node:
            counter += 1
            cur_node = cur_node.next_node
        print(counter)
        return counter

    def insert_into_beginning(self, value):
        new_node = self.Node(value)
        cur_node = self.head
        new_node.next_node = cur_node
        self.head = new_node

    def out(self):
        cur_node = self.head
        output = ''
        while cur_node.next_node:
            output += str(cur_node.value) + '-->'
            cur_node = cur_node.next_node
        print(output, str(cur_node.value))

    def insert_into_ending(self, value):
        new_last_node = self.head
        while new_last_node.next_node:
            new_last_node = new_last_node.next_node
        new_last_node.next_node = self.Node(value, None)

    def remove_by_index(self, index):
        if index < 0 or index >= self.length():
            raise Exception('Invalid index')
        if index == 0:
            self.head = self.head.next_node
            return
        cur_node = self.head
        counter = 0
        while cur_node:
            if counter == index:
                cur_node.next_node = cur_node.next_node.next_node
                break
            counter += 1
            cur_node = cur_node.next_node



list1 = LinkedList()
list1.append(1)
list1.append(3)
list1.append(2)
list1.append(1)
list1.append(3)
list1.append(2)
list1.out()
