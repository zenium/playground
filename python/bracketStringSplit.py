import unittest


def bracketStringSplit(string):
    stack = []
    left = {
        '[': 1,
        '(': 2,
        '{': 3,
    }
    right = {
        ']': 1,
        ')': 2,
        '}': 3,
    }
    for i in range(len(string)):
        if string[i] in left.keys():
            stack += string[i]
        if string[i] in right.keys():
            try:
                last = stack.pop()
            except Exception:
                return False
            if left[last] != right[string[i]]:
                return False
    if len(stack) > 0:
        return False
    return True


class simpletest(unittest.TestCase):
    def setUp(self):
        pass

    def testisNetblock(self):
        tests = [
            {
                'i': '{[()()]}',
                'r': True,
            },
            {
                'i': '([)()]',
                'r': False,
            },
            {
                'i': ')[)()]',
                'r': False,
            },
            {
                'i': '()()(',
                'r': False,
            },
        ]
        for t in tests:
            self.assertEqual(bracketStringSplit(t['i']), t['r'])


if __name__ == '__main__':
    unittest.main()
