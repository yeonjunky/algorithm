import gc

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

    def __repr__(self) -> str:
        return str(self.value)

class LinkedList:
    def __init__(self, node=None) -> None:
        if node is None:
            self.head = Node(None)
        else:
            self.head = node

        self.len = 1

    def append(self, node, index=None):
        if index is None:
            last_node = self.head

            while last_node.next:
                last_node = last_node.next

            last_node.next = node

        else:
            ith_node = self.head
            for _ in range(index):
                ith_node = node.next
            
            temp = ith_node.next

            ith_node.next = node
            node.next = temp

        self.len += 1

    def delete(self, index):
        node = self.head

        if index == 0:
            self.head = node.next

        else:
            for _ in range(index-1):
                node = node.next

            node.next = node.next.next

        self.len -= 1

    def print(self):
        node = self.head
        for i in range(self.len):
            print('index {}'.format(i), node)
            node = node.next

head = Node(1)
linkedlist = LinkedList(head)

linkedlist.append(Node(123))
linkedlist.append(Node(45))
linkedlist.append(Node(46))
linkedlist.append(Node(47))
linkedlist.append(Node(48))

linkedlist.delete(2)

linkedlist.print()
