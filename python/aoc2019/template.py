import unittest

def day(n):
    pass

def run():
    ret = []
    # a = []
    # for i in range(245318, 765747):
    #     a.append(i)
    #     if day4_p2(i):
    #         ret.append(i)
    # print(f">>>{len(ret)}, {len(a)}")
    print(ret)


class TestDay(unittest.TestCase):
    def test_day(self):
        tests = (
            {
                "i": 111122,
                "r": True,
            },
        )
        for t in tests:
            self.assertIs(day(t["i"]), t["r"], f'i: {t["i"]} for {t["r"]}')


if __name__ == '__main__':
    # run()
    unittest.main()
    