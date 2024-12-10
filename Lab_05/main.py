from Lab_05 import DisjointSet

if __name__ == '__main__':
    # Tasks A
    uf = DisjointSet(10)
    # 0 1-2-5-6-7 3-8-9 4
    uf.unionByRank(1, 2)
    uf.unionByRank(2, 5)
    uf.unionByRank(5, 6)
    uf.unionByWeight(6, 7)
    uf.unionByRank(3, 8)
    uf.unionByWeight(8, 9)
    print(uf.isConnected(1, 5))
    print(uf.isConnected(5, 7))
    print(uf.isConnected(4, 9))
    # 0 1-2-5-6-7 3-8-9-4
    uf.unionByWeight(9, 4)
    print(uf.isConnected(4, 9))
    # Tasks B
    connected = [[1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 1]]
    uf = DisjointSet(4)
    uf.joinBlocks(connected)
    uf.findBlockCount(1)
