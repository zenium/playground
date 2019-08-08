import unittest

def stringCompression(s):
  last = ''
  result = ''
  count = 0
  for v in s:
    if v != last:
      if count:
        result += (last+str(count))
      last = v
      count = 1
    else:
      count += 1
  if count:
    result += (last+str(count))
  if len(result)>len(s):
    return s
  return result

def isSubstring(a,b):
  a = sorted(a)
  b = sorted(b)
  if len(a) < len(b):
    b,a = a,b
  for i, _ in enumerate(a):
    print(a[i:i+len(b)], b)
    if i > len(a)-len(b):
      return False
    if a[i:(i+len(b))]==b:
      return True
  return False


def PyTri(arr):
  """
  Pythagorean Triplet in an array
  Given an array of integers, write a function that returns true if there is a triplet (a, b, c) that satisfies a2 + b2 = c2
  """
  sqSet = set()
  sqArr = []
  for i in arr:
    sqSet.add(i*i)
    sqArr.append(i*i)
  sqArr = sorted(sqArr)
  for i in sqArr[:(len(sqArr)-1)]:
    for j in sqArr[1:(len(sqArr)-1)]:
      if (i+j) in sqSet:
        return True
  return False
  


class simpletest(unittest.TestCase):
    def setUp(self):
        pass
    
    def testkLargest(self):
        tests = [
            {
                'arr': [1,2,3,4,5,6,7,8,9,10,11],
                'r': [9,10,11],
            },
            {
                'arr': [1,2,3,4,5,6,7,8,9,10,11],
                'r': [8,9,10,11],
            },
            ]
        for t in tests:
          self.assertEqual(Pytri(t['arr']), t['r'])
    
if __name__ == '__main__':
    unittest.main()
