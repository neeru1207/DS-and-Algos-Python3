class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Add node function. Returns 0 on success and -1 on failure.
    def add_node(self, data, pos):
        # 1 based position indexing, -1 for inserting at the end.
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            newnode = Node(data)
            if pos == -1:
                newnode.prev = self.tail
                self.tail.next = newnode
                self.tail = newnode
            elif pos == 1:
                self.head.prev = newnode
                newnode.next = self.head
                self.head = newnode
            else:
                previ = self.head
                for i in range(1,pos-1):
                    previ = previ.next
                if previ is None:
                    return -1
                curr = previ.next
                previ.next = newnode
                curr.prev = newnode
                newnode.prev = previ
                newnode.next = curr
            return 0

    def print_list_forward(self):
        temp = self.head
        while temp is not None:
            print(temp.data,end=" ")
            temp = temp.next
        print("")

    def print_list_reverse(self):
        temp = self.tail
        while temp is not None:
            print(temp.data,end=" ")
            temp = temp.prev
        print(" ")

    # Delete by value function. Returns 0 on success and -1 on error.
    def delete_by_value(self, value):
        curr = self.head
        found = False
        if self.head.data == value:
            self.head = self.head.next
            self.head.prev = None
            return 0
        while curr is not None:
            if curr.data == value:
                found = True
                break
            curr = curr.next
        if not found:
            return -1
        prev = curr.prev
        next = curr.next
        prev.next = next
        next.prev = prev

    # Delete by position function. Returns 0 on success and -1 on error.
    def delete_by_pos(self, pos):
        # 1 based position indexing is expected
        if pos == 1:
            self.head = self.head.next
            self.head.prev = None
        else:
            curr = self.head
            for i in range(1, pos):
                curr = curr.next
            if curr is None:
                return -1
            prev = curr.prev
            next = curr.next
            prev.next = next
            next.prev = prev
        return 0

    # Returns True if found, else False
    def search(self, data):
        temp = self.head
        found = False
        while temp is not None:
            if temp.data == data:
                found = True
            temp = temp.next
        return found

    # Reverses the linked list and returns the head of the new list
    def reverse(self):
        temp = self.head
        while temp.next is not None:
            temp.next, temp.prev = temp.prev, temp.next
            temp = temp.prev
        temp.next, temp.prev = temp.prev, temp.next
        return temp

x = DoubleLinkedList()
x.add_node(1,-1)
x.add_node(2,-1)
x.add_node(3,-1)
x.add_node(4,-1)
x.add_node(5,-1)
x.print_list_forward()
x.head = x.reverse()
x.print_list_forward()
