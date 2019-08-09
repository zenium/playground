import unittest

def nge(input):
  """
  Given an array, print the Next Greater Element (NGE) for every element. The Next greater Element for an element x is the first greater element on the right side of x in array. Elements for which no greater element exist, consider next greater element as -1.
  """
  ret = [-1]*len(input)
  stack = []
  for i, v in enumerate(input):
    while stack:
      sv, si = stack[-1]
      if sv>=v:
        break
      ret[si] = v
      stack.pop()
    stack.append((v, i))
  return ret



class simpletest(unittest.TestCase):
    def setUp(self):
        pass

    def testisNetblock(self):
        tests = [
            {
                't': [4,5,2,25],
                'r': [5,25,25,-1],
            },
            {
                't': [13,7,6,12],
                'r': [-1,12,12,-1],
            },
            {
                't': [4,8,6,7,8,9,10],
                'r': [8,9,7,8,9,10,-1],
            },
            ]
        for t in tests:
            self.assertEqual(nge(t['t']), t['r'])

if __name__ == '__main__':
    unittest.main()
