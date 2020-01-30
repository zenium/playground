import unittest
import collections

def day4(n):
    number_str = str(n)
    if len(number_str) != 6:
        return False
    has_double = False
    last = 0
    last_largest = 0
    for s in number_str:
        i = int(s)
        if i < last_largest:
            return False
        if i == last:
            has_double = True
        last = i
        last_largest = max(last_largest, i)
    if not has_double:
        return False
    return True

def day4_p2(n):
    number_str = str(n)
    if len(number_str) != 6:
        return False
    last = 0
    last_largest = 0
    repeat_count = 1

    repeat = collections.defaultdict(list)

    for s in number_str:
        i = int(s)
        if i < last_largest:
            return False
        if i == last:
            repeat_count += 1
        elif repeat_count > 1:
            if repeat_count <2:
                continue
            if repeat_count > 4:
                return False
            repeat[repeat_count].append(last)
            repeat_count = 1

        last = i
        last_largest = max(last_largest, i)

    if repeat_count > 1:
        if repeat_count > 4:
            return False
        repeat[repeat_count].append(last)

    if not len(repeat):
        return False
    if len(repeat)==1 and list(repeat.keys()) != [2]:
        return False
    return True

def run():
    ret = []
    a = []
    for i in range(245318, 765747):
        a.append(i)
        if day4_p2(i):
            ret.append(i)
    print(f">>>{len(ret)}, {len(a)}")
    print(ret)


class TestDay4(unittest.TestCase):
    def test_day4(self):
        tests = (
            {
                "i": 123456,
                "r": False,
            },
            {
                "i": 122345,
                "r": True,
            },
            {
                "i": 111111,
                "r": True,
            },
            {
                "i": 223450,
                "r": False,
            },
            {
                "i": 123789,
                "r": False,
            },
        )
        for t in tests:
            assert day4(t["i"]) is t["r"]

    def test_day4_p2(self):
        tests = (
            {
                "i": 123456,
                "r": False,
            },
            {
                "i": 122345,
                "r": True,
            },
            {
                "i": 111111,
                "r": False,
            },
            {
                "i": 223450,
                "r": False,
            },
            {
                "i": 123789,
                "r": False,
            },
            {
                "i": 112233,
                "r": True,
            },
            {
                "i": 123444,
                "r": False,
            },
            {
                "i": 111122,
                "r": True,
            },
        )
        for t in tests:
            self.assertIs(day4_p2(t["i"]), t["r"], f'i: {t["i"]} for {t["r"]}')


if __name__ == '__main__':
    run()
    unittest.main()
    