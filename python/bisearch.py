import unittest

def biSearch(target, want):
    if want < target[0] or want > target[-1]:
        return False
    i = len(target)
    p = 0
    while i>0:
        print target[p:(p+i)],i/2,p
        j=i
        i=i/2
        j=j-i
        if target[i+p]==want:
            return i+p
        if target[i+p]<want:
            p+=j
    return False

class simpletest(unittest.TestCase):
    def setUp(self):
        pass
    
    def testisNetblock(self):
        tests = [
            {
                't': [1,2,3,4,5,6,7,8,9,10,11],
                'w': 3,
                'r': 2,
            },
            {
                't': [1,2,3,4,5,6,7,8,9,10,11],
                'w': 7,
                'r': 6,
            },
            ]
        for t in tests:
            self.assertEqual(biSearch(t['t'], t['w']), t['r'])
    
if __name__ == '__main__':
    unittest.main()