import unittest
import sys


def mas(A):
    if not A:
        return 0
    for i in range(len(A)):
        A[i] = abs(A[i])
    M = max(A)
    S = sum(A)
    HS = S//2+1
    count = [0]*(M+1)
    for i in A:
        count[i] += 1
    dp = set([0])
    for i, v in enumerate(count):
        if v > 0:
            for d in list(dp):
                m = min(d+i*v+1, HS)
                ra = range(d+i, m, i)
                if ra:
                    dp = dp.union(list(ra))
    return S - max(dp)*2


class simpletest(unittest.TestCase):
    def testMas(self):
        tests = [
            # {
            #     'i': [1, 2, -2, 5],
            #     'r': 0,
            # },
            # {
            #     'i': [],
            #     'r': 0,
            # },
            {
                'i': [-100, 3, 2, 4],
                'r': 91,
            },
            ]
        for t in tests:
            self.assertEqual(mas(t['i']), t['r'])

if __name__ == '__main__':
    unittest.main()
