class Node:
    """
    value: any
    next: Node
    """
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

    def __repr__(self) -> str:
        return str(self.value)

class LinkedList:
    """
    if node param is none -> linked list created with dummy head
    else -> linked list created without dummy head
    """
    def __init__(self, node=None) -> None:
        if node is None:
            self.head = Node(None)
        else:
        self.head = node

        self.len = 1

    def append(self, new_data):
        """
        add node to end of the list
        """
        new_node = Node(new_data)

        temp = self.head
        self.head = new_node
        self.head.next = temp

        self.len += 1

    def insert(self, value, index=None):
        """
        if index is none add new node to end of the list
        else add node to specific index
        """

        new_node = Node(value)

        if self.head.value is None:
            self.head = new_node

        elif index is None:
            last_node = self.head

            while last_node.next:
                last_node = last_node.next

            last_node.next = new_node
            self.len += 1

        else:
            ith_node = self.head

            for _ in range(index):
                ith_node = ith_node.next
            
            temp = ith_node.next

            
            ith_node.next = new_node
            new_node.next = temp

            self.len += 1

    def delete(self, index):
        """
        delete a node of a specific index
        """
        node = self.head

        if index == 0:
            self.head = node.next

        else:
            for _ in range(index-1):
                node = node.next

            node.next = node.next.next

        self.len -= 1

    def print(self):
        """
        print nodes of list
        """
        node = self.head
        for i in range(self.len):
            print('index {}'.format(i), node)
            node = node.next

    def __len__(self):
        return self.len

head = Node(None)
linkedlist = LinkedList(head)

linkedlist.append(123)
linkedlist.append(45)
linkedlist.append(46)
linkedlist.append(47)
linkedlist.append(48)

linkedlist.push(100)
linkedlist.push(23)

linkedlist.delete(2)

linkedlist.print()
