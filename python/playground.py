import unittest


def optimalUtilization(deviceCapacity, foregroundAppList, backgroundAppList):
    fg = {}
    bg = {}
    
    for i, m in foregroundAppList:
        if not fg.has_key(m):
            fg[m] = [i]
        else:
            fg[m].append(i)
            
    for i, m in backgroundAppList:
        if not bg.has_key(m):
            bg[m] = [i]
        else:
            bg[m].append(i)
    
    candidate = []
    maxi = 0 
    
    for i in fg.keys():
        for j in bg.keys():
            if i+j > deviceCapacity:
                continue
            if i+j < maxi:
                continue
            if i+j > maxi:
                maxi = i+j
                candidate = []
            candidate.append((fg[i], bg[j]))
    
    return candidate


class simpletest(unittest.TestCase):
    def setUp(self):
        pass

    def testisNetblock(self):
        tests = [
            {
                'arr': [
                    'ykc 82 01',
                    'eo first qpx',
                    '09z cat hamster',
                    '06f 12 25 6',
                    'az0 first qpx',
                    '236 cat dog rabbit snake',
                ],
                'exp': 2
            },
            ]
        for t in tests:
            self.assertEqual(
                t['exp'],
                optimalUtilization(20, [[1,8], [2,4]], [[3,7]])
            )


if __name__ == '__main__':
    unittest.main()
