import unittest
from typing import List
Array = List[int]

def minAbsSum_not_best(A:Array) -> int:
  j = 0
  for i in range(len(A)):
    A[i] = abs(A[i])
  dp = set([0])
  S = sum(A)
  HS = S // 2 + 1
  for i in A:
    for l in list(dp):
      l2 = l+i
      if l2 < HS and l2 not in dp:
        dp.add(l2)
      j+=1
  print(">>>", j)
  return S - max(dp)*2

def minAbsSum_trial1(A:Array) -> int:
  if not A:
    return 0
  M = 0
  for i in range(len(A)):
    A[i] = abs(A[i])
    M = max(M, A[i])
  count = [0] * (M+1)
  print(count)
  for i in range(len(A)):
    count[A[i]] +=1
  S = sum(A)
  HS = S//2 + 1
  dp = set([0])
  for i,v in enumerate(count):
    if v > 0:
      for d in list(dp):
        to = d+(i+1)*v
        tt = to if to < HS else HS
        toadd = range(d+i,tt,i)
        print(list(toadd))
        if toadd:
          dp = dp.union(list(toadd))
  return S - max(dp)*2


def minAbsSum(A:Array) -> int:
    N = len(A)
    M = 0
    jjj = 0
    for i in range(N):
        A[i] = abs(A[i])
        M = max(A[i], M)
    S = sum(A)
    count = [0] * (M + 1)
    for i in range(N):
        count[A[i]] += 1
    dp = [-1] * (S + 1)
    dp[0] = 0
    #print("count: ", count)
    #print("dp: ", dp)
    #print("M: %s; S: %s" % (M, S))
    for a in range(1, M + 1):
        if count[a] > 0:
            for j in range(S):
                #print(a,">",j, dp)
                if dp[j] >= 0:
                    dp[j] = count[a]
                elif (j >= a and dp[j - a] > 0):
                    dp[j] = dp[j - a] - 1
                jjj+=1
    result = S
    print(">>>", jjj)
    for i in range(S // 2 + 1):
        if dp[i] >= 0:
            result = min(result, S - 2 * i)
    return result

class simpletest(unittest.TestCase):
    def setUp(self):
        pass

    def testminAbsSum(self):
        tests = [
            #{
            #  'i': list(range(100)),
            #  'r': 0,
            #},
            {
                'i': [1,5,-2,2],
                'r': 0,
            },
            {
                'i': [-100,3,2,4],
                'r': 91,
            },
            {
                'i': [],
                'r': 0,
            },
            {
                'i': [10, 1, 1, 1, 1, 1, 1],
                'r': 4,
            },
            ]
        for t in tests:
          self.assertEqual(minAbsSum_trial1(t['i']), t['r'])

if __name__ == '__main__':
    unittest.main()
