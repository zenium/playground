from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import unittest

def find_pair(array, n):
  if len(array) < 2:
    return []
  if n < array[0] + array[1] or n > array[-1] + array[-2]:
    return []
  i = 0
  j = len(array) - 1
  while i < j:
    s = array[i] + array[j]
    if s == n:
      return [array[i], array[j]]
    elif s > n:
      j = j-1
    else:
      i = i+1
  return []

class MyTest(unittest.TestCase):
  tests = [
      {
          'args': [1,2,4,4],
          'n': 8,
          'exp': [4,4],
      },
      {
          'args': [-1,-2,1,3,4,5,7],
          'n': 4,
          'exp': [-1, 5],
      },
      {
          'args': [1],
          'n': 3,
          'exp': [],
      },
      {
          'args': [1,2,3,4],
          'n': 8,
          'exp': [],
      }
  ]

  def test_find_pair(self):
    for t in self.tests:
      re = find_pair(t['args'], t['n'])
      self.assertEqual(t['exp'], re)

if __name__ == '__main__':
  unittest.main()