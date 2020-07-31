import unittest


class BiTree(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if data > self.data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BiTree(data)
        elif data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BiTree(data)
        else:
            raise ValueError('ERROR: duplicated data: %s' % data)

    def bfs(self):
        temp = [self]
        for i in temp:
            if i.left:
                temp.append(i.left)
            if i.right:
                temp.append(i.right)
        ret = []
        for t in temp:
            ret.append(t.data)
        return ret

    def dfs(self):
        ret = []
        if self.left:
            ret += self.left.dfs()
        ret.append(self.data)
        if self.right:
            ret += self.right.dfs()
        return ret

    def dfs_b(self):
        ret = []
        if self.left:
            ret += self.left.dfs()
        if self.right:
            ret += self.right.dfs()
        ret.append(self.data)
        return ret

#     def printTree(self):
#         result = []
#         if self.left:
#             result += self.left.printTree()
#         result += [self.data]
#         if self.right:
#             result += self.right.printTree()
#         return result

#     def printLayer(self):
#         temp = [self]
#         for i in temp:
#             if i.left:
#                 temp.append(i.left)
#             if i.right:
#                 temp.append(i.right)
#         result = []
#         for t in temp:
#             result.append(t.data)
#         return result


# class bitreetest(unittest.TestCase):
#     def testinsert(self):
#         tests = [
#             {
#                 'input': [62, 67, 41, 92, 38, 98, 99, 9, 78],
#                 'r1': [9, 38, 41, 50, 62, 67, 78, 92, 98, 99],
#                 'r2': [50, 41, 62, 38, 67, 9, 92, 78, 98, 99],
#             },
#             ]
#         Bt = BiTree(50)
#         for t in tests:
#             for i in t['input']:
#                 Bt.insert(i)
#             self.assertEqual(t['r1'], Bt.printTree())
#             self.assertEqual(t['r2'], Bt.printLayer())

class test_btree(unittest.TestCase):
    def setUp(self):
        self.tree = BiTree(50)
        for i in [62, 67, 41, 92, 38, 98, 99, 9, 78]:
            self.tree.insert(i)
        return super().setUp()

    def bfs(self):
        self.assertEqual([50, 41, 62, 38, 67, 9, 92,
                          78, 98, 99], self.tree.bfs())

    def dfs(self):
        self.assertEqual([9, 38, 41, 50, 62, 67, 78,
                          92, 98, 99], self.tree.dfs())

    def dfs_b(self):
        self.assertEqual([9, 38, 41, 99, 78, 98, 92,
                          67, 62, 50], self.tree.dfs_b())


if __name__ == '__main__':
    unittest.main()
