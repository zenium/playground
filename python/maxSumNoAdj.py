import unittest

def msa(input):
  """
  Given an array of positive numbers, find the maximum sum of a subsequence with the constraint that no 2 numbers in the sequence should be adjacent in the array. So 3 2 7 10 should return 13 (sum of 3 and 10) or 3 2 5 10 7 should return 15 (sum of 3, 5 and 7).Answer the question in most efficient way.
  """
  inc = 0
  exc = 0
  for i in input:
    exc += i
    inc, exc = exc, inc
  return max(exc, inc)



class simpletest(unittest.TestCase):
    def setUp(self):
        pass

    def testA(self):
        tests = [
            {
                't': [5,5,10,100,10,5],
                'r': 110,
            },
            {
                't': [1,2,3],
                'r': 4,
            },
            {
                't': [1,20,3],
                'r': 20,
            },
            ]
        for t in tests:
            self.assertEqual(msa(t['t']), t['r'])

if __name__ == '__main__':
    unittest.main()
