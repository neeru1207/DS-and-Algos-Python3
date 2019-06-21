class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
        self.n = n

# Path compression
    def find(self, x):
        # If x is not the representative of it's own set, then recursively find the representative.
        # Then make x the new representative
        if not self.parent[x] == x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

# Union by rank
    def union(self, x, y):
        # Find the set representatives of x and y
        xset = self.find(x)
        yset = self.find(y)
        # If they are already in the same set, no need to do anything
        if xset == yset:
            return
        # Make the set representative with the higher rank the parent of the lower rank one
        if self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        elif self.rank[yset] > self.rank[xset]:
            self.parent[xset] = yset
        # If they have the same ranks, make one of them the new representative and increase it's rank.
        # Move the other under the new representative
        else:
            self.rank[xset] += 1
            self.parent[yset] = xset

