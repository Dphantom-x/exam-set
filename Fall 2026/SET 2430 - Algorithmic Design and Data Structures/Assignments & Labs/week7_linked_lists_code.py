# SET 2430 - Week 7 In-Class Code (Circular & Doubly Linked Lists)
# Prof. Haiying Xiao

class Node:
    def __init__(self, val):
        self.value = val
        self.right = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def addAtHead(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            new_node.right = new_node
            return
        current = self.head
        while current.right != self.head:
            current = current.right
        new_node.right = self.head
        current.right = new_node
        self.head = new_node

    def print_list(self):
        if not self.head:
            print("Empty")
            return
        curr = self.head
        res = []
        while True:
            res.append(str(curr.value))
            curr = curr.right
            if curr == self.head:
                break
        print(" -> ".join(res) + " -> (head)")


# Node for Doubly Linked List
class DoublyNode:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value):
        new_node = DoublyNode(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.right = new_node
            new_node.left = self.tail
            self.tail = new_node
        self.size += 1

    def addAtHead(self, val):
        new_node = DoublyNode(val)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.right = self.head
            self.head.left = new_node
            self.head = new_node
        self.size += 1

    def get(self, index):
        if index < 0 or index >= self.size:
            return None
        curr = self.head
        for _ in range(index):
            curr = curr.right
        return curr.value

    def countNodes(self):
        return self.size

    def print_forward(self):
        current = self.head
        vals = []
        while current:
            vals.append(str(current.value))
            current = current.right
        print("<->".join(vals))


if __name__ == '__main__':
    print("--- Circular Linked List Test ---")
    clist = CircularLinkedList()
    clist.addAtHead(100)
    clist.addAtHead(200)
    clist.addAtHead(300)
    clist.print_list()

    print("\n--- Doubly Linked List Test ---")
    dlist = DoublyLinkedList()
    dlist.append(10)
    dlist.append(20)
    dlist.append(30)
    dlist.addAtHead(5)
    dlist.print_forward()
    print("Node count:", dlist.countNodes())
    print("Item at index 2:", dlist.get(2))
