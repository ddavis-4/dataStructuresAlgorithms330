"""
Dylan Davis
EECS 330
Lab 05
October 2 2023
Content: Disjoint Set
"""


class DisjointSet:
    def __init__(self, size):
        self.vertex = [i for i in range(size)]
        self.weight = [1] * size

    # This is the validate function, and it checks whether index v1 is a valid
    # The index must be greater than or equal to 0 but less than the length of the vertex
    def validate(self, v1):
        return 0 <= v1 < len(self.vertex)

    # Size function that will return the size of the set v1 belongs to
    def size(self, v1):
        if not self.validate(v1):
            return 0
        r = self.find(v1)
        return self.weight[r]

    # parent function will return the parent of vertex v1
    def parent(self,v1):
        if not self.validate(v1):
            return None
        r = self.find(v1)
        if self.vertex[v1] == r:
            return -self.weight[r]
        else:
            return r

    # isConnected function, it checks to see if v1 and v2 are connected
    def isConnected(self, v1, v2):
        r1 = self.find(v1)
        r2 = self.find(v2)
        return r1 == r2

    # Created Find function will return the root of the set v1
    def find(self, v1):
        if not self.validate(v1):
            return None
        if self.vertex[v1] == v1:
            return v1
        self.vertex[v1] = self.find(self.vertex[v1])
        return self.vertex[v1]

    # Union by weight function, first gets the root of v1 and v2 and if r1 is not r2.
    def unionByWeight(self,v1, v2):
        r1 = self.find(v1)
        r2 = self.find(v2)
        if r1 != r2:
            if self.weight[r1] < self.weight[r2]: # check to see if r1 and r2 have different roots
                self.vertex[r1] = r2 # makes r2 the parent of r1
                self.weight[r2] += self.weight[r1] # change weight of r2
            elif self.weight[r1] > self.weight[r2]:
                self.vertex[r2] = r1 # r1 becomes the parent of r2
                self.weight[r1] += self.weight[r2]
            else: # equal ranks meaning the order doesn't matter.
                self.vertex[r1] = r2 # r2 becomes the parent of r1
                self.weight[r2] += 1 # we increment the weight of r2

    # Function union by Rank
    def unionByRank(self, v1, v2):
        r1 = self.find(v1) # find the root pf v1
        r2 = self.find(v2) # find the root of v2

        if r1 != r2: # make sure r1 and r2 have different roots
            if self.weight[r1] < self.weight[r2]: # If rank r1 is less than r2
                self.vertex[r1] = r2 # make r2 the parent of r1
            elif self.weight[r1] > self.weight[r2]: # If r1 is greater than r3
                self.vertex[r2] = r1 # make r1 parent of r2
            else:
                self.vertex[r1] = r2 # else make r2 parent of r1
                self.weight[r2] += 1 # and increment the rank of r2

    # joinBlocks function to make disjoint sets with a given matrix
    def joinBlocks(self, connected):
        msize = len(connected) # gets the length of the matrix
        for i in range(msize): # iterates though the rows
            for j in range(msize): # iterates thought the columns
                if connected[i][j] == 1: # if i and j are connected
                    self.unionByRank(i, j)
        return self.vertex # returns disjoint-set

    # Function to return the quantity of connected block sets
    def findBlockSets(self):
        blkst = 0 # keeps track of the number of block sets
        for i in range(len(self.vertex)):
            if self.vertex[i] == i:
                blkst += 1
        return blkst # return number of block set

    # Function created to return number of blocks where block id is identified
    def findBlockCount(self, blockid):
        r = self.find(blockid) # finds the root element of the block containing the blockid
        x = 0 # keeps track of how many times the loop runs
        for i in range(len(self.vertex)): # iterates through elements in disjoint-set
            if self.vertex[i] == r: # If the root is == to the block id root
                x += 1 # increment up one
        return x # return the count