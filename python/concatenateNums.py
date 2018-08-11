import unittest

def conc(array):
    digi={}
    for i in array:
        if i//1000>0:
            j = 3
        elif i//100>0:
            j = 2
        elif i//10>0:
            j = 1
        else:
            j = 0
        if j>0:
            quo = i//(10**j)
        else:
            quo = i
        key = '%s-%s' % (j, quo)
        if not digi.has_key(key):
            digi[key] = [i]
        else:
            digi[key] += [i]
    print(digi)
    result = ''
    for i in range(9, 0, -1):
        for j in range(0, 4):
            key = '%s-%s' % (j, i)
            if digi.has_key(key):
                for num in sorted(digi[key], reverse=True):
                    result += str(num)
                
    return result

class simpletest(unittest.TestCase):
    def testconc(self):
        tests = [
            {
                'arg': [3,34,32,5],
                'r': 534332,
            },
            ]
        for t in tests:
            self.assertEqual(conc(t['arg']), t['r'])
    
if __name__ == '__main__':
    unittest.main()