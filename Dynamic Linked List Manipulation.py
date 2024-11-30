# Starter Code from https://www.geeksforgeeks.org/python-linked-list/
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtIndex(self, data, index):
        if index == 0:
            self.insertAtBegin(data)
            return
        
        position = 0
        current_node = self.head
        while current_node and position + 1 != index:
            position += 1
            current_node = current_node.next

        if current_node:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index not present")

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while current_node and position != index:
                position += 1
                current_node = current_node.next

            if current_node:
                current_node.data = val
            else:
                print("Index not present")

    def sizeOfLL(self):
        size = 0
        if self.head:
            current_node = self.head
            while current_node:
                size += 1
                current_node = current_node.next
            return size
        else:
            return 0

    def printLL(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

    def remove_duplicates(self):
        current = self.head
        seen_values = set()
        prev = None
        while current:
            if current.data in seen_values:
                prev.next = current.next
            else:
                seen_values.add(current.data)
                prev = current
            current = current.next

    def merge(self, llist2):
        fake_node = Node(0)
        tail = fake_node
        l1 = self.head
        l2 = llist2.head
        while l1 and l2:
            if l1.data <= l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        self.head = fake_node.next

def main():
    llist_nodes = input().split()
    if llist_nodes[0] == 'duplicate':
        llist = LinkedList()
        for i in range(1, len(llist_nodes)):
            llist.insertAtEnd(int(llist_nodes[i]))
        llist.remove_duplicates()
        llist.printLL()  
    elif llist_nodes[0] == 'merge':
        llist1 = LinkedList()
        llist2 = LinkedList()
        llist2_index = llist_nodes.index("llist2")
        for i in range(1, llist2_index):
            llist1.insertAtEnd(int(llist_nodes[i]))
        for i in range(llist2_index + 1, len(llist_nodes)):
            llist2.insertAtEnd(int(llist_nodes[i]))
        llist1.merge(llist2)
        llist1.printLL()

if __name__ == "__main__":
    main()
