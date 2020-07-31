import unittest

def day(n):
    return fuel(n)

def day_p2(n):
    ret = 0
    while fuel(n) > 0:
        ret += fuel(n)
        n = fuel(n)
    return ret

def fuel(n):
    return n//3-2

def run():
    ret = 0
    with open("C:\\Users\\l136836\\code\\playground\\day1input", "r") as f:
        for l in f:
            ret += day_p2(int(l.strip()))
    print(f">> {ret}")



class TestDay(unittest.TestCase):
    def test_day(self):
        tests = (
            {
                "i": 12,
                "r": 2,
            },
            {
                "i": 14,
                "r": 2,
            },
            {
                "i": 1969,
                "r": 654,
            },
            {
                "i": 100756,
                "r": 33583,
            },
        )
        for t in tests:
            self.assertEqual(day(t["i"]), t["r"], f'i: {t["i"]} for {t["r"]}')

    def test_day_p2(self):
        tests = (
            {
                "i": 14,
                "r": 2,
            },
            {
                "i": 1969,
                "r": 966,
            },
            {
                "i": 100756,
                "r": 50346,
            },
        )
        for t in tests:
            self.assertEqual(day_p2(t["i"]), t["r"], f'i: {t["i"]} for {t["r"]}')


if __name__ == '__main__':
    run()
    unittest.main()
    