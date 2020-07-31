import unittest
from typing import List


def dynaList(l1: List[int], l2: List[int]) -> List[int]:
    i = j = 0
    while i < len(l1):
        if i % 2 and j < len(l2):
            l1.insert(i, l2[j])
            j += 1
        i += 1
    if j < len(l2):
        l1 += l2[j:]
    return l1


class simpletest(unittest.TestCase):
    def setUp(self):
        pass

    def testDynaList(self):
        tests = [
            {
                'l1': [1, 2, 3, 4],
                'l2': [11, 12, 13, 14, 15],
                'r': [1, 11, 2, 12, 3, 13, 4, 14, 15],
            },
            {
                'l1': [1, 2, 3, 4, 5, 6],
                'l2': [11, 12],
                'r': [1, 11, 2, 12, 3, 4, 5, 6],
            },
            {
                'l1': [],
                'l2': [11, 12],
                'r': [11, 12],
            },
            {
                'l1': [1, 2],
                'l2': [],
                'r': [1, 2],
            },
        ]
        for t in tests:
            self.assertEqual(dynaList(t['l1'], t['l2']), t['r'])


if __name__ == '__main__':
    unittest.main()
