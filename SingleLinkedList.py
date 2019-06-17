class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    # Add node function. Returns 0 on success and -1 on failure.
    def addnode(self, data, pos):
        # 1 based position indexing, -1 for inserting at the end.
        if self.head is None:
            self.head = Node(data)
            self.head.next = None
        else:
            newnode = Node(data)
            if pos == -1:
                temp = self.head
                while temp.next is not None:
                    temp = temp.next
                temp.next = newnode
                newnode.next = None
            elif pos == 1:
                newnode.next = self.head
                self.head = newnode
            else:
                prev = self.head
                for i in range(1,pos-1):
                    prev = prev.next
                if prev is None:
                    return -1
                curr = prev.next
                prev.next = newnode
                newnode.next = curr
            return 0

    def printlist(self):
        temp = self.head
        while temp is not None:
            print(temp.data,end=" ")
            temp = temp.next
        print("")

    # Delete by value function. Returns 0 on success and -1 on error.
    def delete_by_value(self, value):
        prev = self.head
        found = False
        if self.head.data == value:
            self.head = self.head.next
            return 0
        while prev.next is not None:
            if prev.next.data == value:
                found = True
                break
            prev = prev.next
        if not found:
            return -1
        prev.next = prev.next.next
    # Delete by position function. Returns 0 on success and -1 on error.

    def delete_by_position(self,pos):
        # 1 based position indexing is expected
        if pos == 1:
            self.head = self.head.next
        else:
            prev = self.head
            for i in range(1,pos-1):
                prev = prev.next
            if prev is None:
                return -1
            prev.next = prev.next.next
        return 0
