import unittest
import sys


def quickSort(array):
    if len(array) <= 1:
        return array
    left = []
    right = []
    for i in range(1, len(array)):
        if array[i] < array[0]:
            left.append(array[i])
        else:
            right.append(array[i])
    return quickSort(left) + [array[0]] + quickSort(right)


class simpletest(unittest.TestCase):
    def setUp(self):
        pass

    def testquickSort(self):
        tests = [
            {
                'i': [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48],
                'r': [2, 3, 4, 5, 15, 19, 26, 27, 36, 38, 44, 46, 47, 48, 50],
            },
            ]
        for t in tests:
            self.assertEqual(quickSort(t['i']), t['r'])

if __name__ == '__main__':
    unittest.main()
