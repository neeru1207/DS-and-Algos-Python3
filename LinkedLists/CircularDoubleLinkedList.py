class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


class CircularDoubleLinkedList:
    def __init__(self):
        self.head = None

    # Add node function. Returns 0 on success and -1 on failure.
    def add_node(self, data, pos):
        # 1 based position indexing, -1 for inserting at the end.
        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head
        else:
            newnode = Node(data)
            if pos == -1:
                newnode.prev = self.head.prev
                if self.head.prev is not None:
                    self.head.prev.next = newnode
                    newnode.next = self.head
                    self.head.prev = newnode
                else:
                    self.head.next = newnode
                    newnode.next = self.head
                    newnode.prev = self.head
                    self.head.prev = newnode
            elif pos == 1:
                x = self.head.prev
                x.next = newnode
                newnode.prev = x
                newnode.next = self.head
                self.head.prev = newnode
                self.head = newnode
            else:
                previ = self.head
                for i in range(1,pos-1):
                    previ = previ.next
                curr = previ.next
                if curr is self.head:
                    return -1
                previ.next = newnode
                curr.prev = newnode
                newnode.prev = previ
                newnode.next = curr
            return 0

    def print_list_forward(self):
        temp = self.head
        while temp.next is not self.head:
            print(temp.data, end=" ")
            temp = temp.next
        print(temp.data)

    def print_list_reverse(self):
        temp = self.head.prev
        while temp is not self.head and temp is not None:
            print(temp.data, end=" ")
            temp = temp.prev
        print(self.head.data)

    # Delete by value function. Returns 0 on success and -1 on error.
    def delete_by_value(self, value):
        curr = self.head
        found = False
        if self.head.data == value:
            self.head = self.head.next
            self.head.prev = None
            return 0
        while curr.next is not self.head:
            if curr.data == value:
                found = True
                break
            curr = curr.next
        if self.head.prev.data == value:
            curr = self.head.prev
            found = True
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
            if self.head is not None:
                self.head.prev = None
        elif pos == -1:
            tobedel = self.head.prev
            if tobedel is self.head:
                self.head = None
            else:
                prev = tobedel.prev
                next = tobedel.next
                prev.next = tobedel.next
                next.prev = prev


        else:
            curr = self.head
            for i in range(1, pos):
                curr = curr.next
            prev = curr.prev
            next = curr.next
            prev.next = next
            next.prev = prev
        return 0
