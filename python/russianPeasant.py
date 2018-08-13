import unittest


def rp(x, y, result=0):
    if y == 1:
        return result+x
    if y % 2:
        return rp(x*2, y/2, result+x)
    return rp(x*2, y/2, result)


class simpletest(unittest.TestCase):
    def setUp(self):
        pass

    def testisNetblock(self):
        tests = [
            {
                'x': 57,
                'y': 86,
                'r': 4902,
            },
            {
                'x': 1920,
                'y': 8734,
                'r': 1920*8734,
            },
            ]
        for t in tests:
            self.assertEqual(rp(t['x'], t['y']), t['r'])

if __name__ == '__main__':
    unittest.main()
