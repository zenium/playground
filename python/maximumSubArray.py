import unittest


def maximumSubArray(array):
    left = None
    right = None
    current_sum = 0
    max_left = None
    max_right = None
    max_sum = 0
    for i, v in enumerate(array):
        if v > 0:
            if not current_sum:
                left = i
            right = i
            current_sum += v
            if current_sum > max_sum:
                max_left = left
                max_right = right
                max_sum = current_sum
        if v <= 0:
            if current_sum+v > 0:
                right = i
                current_sum += v
            else:
                left = None
                right = None
                current_sum = 0
    return (max_left, max_right, max_sum)


def maximumSubArrayII(array):
    pass


class MyTest(unittest.TestCase):

    def test_maximumSubArray(self):
        tests = [
            {'args': [
                13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4,
                7], 'exp': (7, 10, 43)},
            {'args': [-22, -15, -4, -7], 'exp': (None, None, 0)},
            {'args': [-22, -15, 4, -7], 'exp': (2, 2, 4)},
            {'args': [22, 15, 4, -7], 'exp': (0, 2, 41)},
            {'args': [1, -2, 3, 10, -4, 7, 2, -5], 'exp': (2, 6, 18)},
            ]
        for t in tests:
            self.assertEqual(t['exp'], maximumSubArray(t['args']))

if __name__ == '__main__':
    unittest.main()
