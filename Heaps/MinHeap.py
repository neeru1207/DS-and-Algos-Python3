class MinHeap:
    def __init__(self):
        self.heap = []
        self.root = None

    def insertion_heapify(self, idx):
        while idx>0:
            parentidx = (idx - 1) // 2
            if self.heap[parentidx] > self.heap[idx]:
                self.heap[parentidx], self.heap[idx] = self.heap[idx], self.heap[parentidx]
                idx = parentidx
            else:
                break

    def print(self):
        print(*self.heap)

    def get_min(self):
        try:
            return self.heap[0]
        except:
            print("Error! Heap empty.")

    def deletion_heapify(self, idx):
        curr = idx
        while True:
            left = 2*curr + 1
            right = 2*curr + 2
            if left > len(self.heap)-1:
                break
            if right > len(self.heap)-1:
                if self.heap[left] < self.heap[curr]:
                    self.heap[left], self.heap[curr] = self.heap[curr], self.heap[left]
                    curr = left
                break
            if self.heap[left] < self.heap[curr] and self.heap[left] <= self.heap[right]:
                self.heap[left], self.heap[curr] = self.heap[curr], self.heap[left]
                curr = left
            elif self.heap[right] < self.heap[curr] and self.heap[right] <= self.heap[left]:
                self.heap[right], self.heap[curr] = self.heap[curr], self.heap[right]
                curr = right
            elif self.heap[curr] <= self.heap[left] and self.heap[curr] <= self.heap[right]:
                break

    # Returns 0 on successful deletion, -1 otherwise
    def delete_node(self,index):
        if index >= len(self.heap) or index < 0:
            print("ERROR! Invalid index")
            return -1
        self.heap[-1], self.heap[index] = self.heap[index], self.heap[-1]
        del self.heap[-1]
        self.deletion_heapify(index)

    def extract_min(self):
        x = self.heap[0]
        self.delete_node(0)

    def insert_node(self,value):
        if self.root is None:
            self.root = value
            self.heap.append(value)
        else:
            self.heap.append(value)
            self.insertion_heapify(len(self.heap) - 1)
