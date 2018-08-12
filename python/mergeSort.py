import unittest
import sys


def mergeSort(array):
    if len(array) == 1:
        return array
    # if len(array) == 2:
    #     if array[0] < array[1]:
    #         return array
    #     return array[::-1]
    left = mergeSort(array[:len(array)/2])
    right = mergeSort(array[len(array)/2:])
    left.append(sys.maxint)
    right.append(sys.maxint)
    result = []
    l, r = 0, 0
    for _ in xrange(len(array)):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    print(result)
    return result


class simpletest(unittest.TestCase):
    def setUp(self):
        pass

    def testmergeSort(self):
        tests = [
            {
                'i': [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48],
                'r': [2, 3, 4, 5, 15, 19, 26, 27, 36, 38, 44, 46, 47, 48, 50],
            },
            ]
        for t in tests:
            self.assertEqual(mergeSort(t['i']), t['r'])

if __name__ == '__main__':
    unittest.main()
