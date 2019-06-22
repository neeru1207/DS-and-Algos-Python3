class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class CircularSingleLinkedList:
    def __init__(self):
        self.head = None

    # Add node function. Returns 0 on success and -1 on failure.
    def addnode(self, data, pos):
        # 1 based position indexing, -1 for inserting at the end.
        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head
        else:
            newnode = Node(data)
            if pos == -1:
                temp = self.head
                while temp.next is not self.head:
                    temp = temp.next
                temp.next = newnode
                newnode.next = self.head
            elif pos == 1:
                temp = self.head
                while temp.next is not self.head:
                    temp = temp.next
                temp.next = newnode
                newnode.next = self.head
                self.head = newnode
            else:
                prev = self.head
                for i in range(1, pos-1):
                    prev = prev.next
                curr = prev.next
                prev.next = newnode
                newnode.next = curr
                if curr is self.head:
                    self.head = newnode
            return 0

    def printlist(self):
        temp = self.head
        while temp.next is not self.head:
            print(temp.data,end=" ")
            temp = temp.next
        print(temp.data)

    # Delete by value function. Returns 0 on success and -1 on error.
    def delete_by_value(self, value):
        prev = self.head
        found = False
        if self.head.data == value:
            self.head = self.head.next
            return 0
        while prev.next is not self.head:
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
            curr = prev.next
            prev.next = curr.next
            if curr is self.head:
                self.head = curr.next
        return 0

    # Returns True if found, else False
    def search(self, data):
        temp = self.head.next
        found = False
        if data == self.head.data:
            return True
        while temp is not self.head:
            if temp.data == data:
                found = True
            temp = temp.next
        return found

    # Reverses the linked list and returns head of the new list
    def reverse(self):
        prev = self.head
        while prev.next is not self.head:
            prev = prev.next
        curr = self.head
        tempx = None
        while tempx is not self.head:
            nextn = curr.next
            curr.next = prev
            prev = curr
            curr = nextn
            tempx = curr
        return prev