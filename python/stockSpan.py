import unittest

def stockSpan(input):
    """The stock span problem is a financial problem where we have a series of n daily price quotes for a stock and we need to calculate span of stock’s price for all n days. 
The span Si of the stock’s price on a given day i is defined as the maximum number of consecutive days just before the given day, for which the price of the stock on the current day is less than or equal to its price on the given day.
For example, if an array of 7 days prices is given as {100, 80, 60, 70, 60, 75, 85}, then the span values for corresponding 7 days are {1, 1, 1, 2, 1, 4, 6}
    """
    stack = []
    ret = []
    for i, v in enumerate(input):
        if not stack:
            stack.append((v, i))
            ret.append(1)
            continue
        while stack:
            last_v, last_i = stack[-1]
            if last_v > v:
                stack.append((v, i))
                ret.append(i - last_i)
                break
            else:
                stack.pop()
    return ret



class simpletest(unittest.TestCase):
    def setUp(self):
        pass

    def testisNetblock(self):
        tests = [
            {
                't': [100,80,60,70,60,75,85],
                'r': [1,1,1,2,1,4,6],
            },
            ]
        for t in tests:
            self.assertEqual(stockSpan(t['t']), t['r'])

if __name__ == '__main__':
    unittest.main()
