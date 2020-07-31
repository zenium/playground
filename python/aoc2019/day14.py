import unittest

{
    'fuel': {
        'quantity': 10,
        'res': {
            'A': 7,
            'E': 1,
        }
    }
}
{
    'A': {
        'quantity': 10,
        'res': {
            'ORE': 10,
        }
    }
}

all_res = {}

def day(ls):
    global all_res
    for l in ls.split('\n'):
        all_res.update(react(l))
    return find_ore(all_res['FUEL'])

def find_ore(res):
    global all_res
    ore = 0
    if len(res['res']) == 1 and list(res['res'])==['ORE']:
        return res['res']['ORE']
    for r in res['res']:
        x = -(- res['res'][r]// all_res[r]['quantity'])
        v = x * find_ore(all_res[r])
        ore += v
    return ore


def react(s):
    ret = {}
    (l,r) = s.split(' => ')
    (qua_r, res) = r.split(' ')
    l_list = l.split(', ')
    ret[res] = {'quantity': int(qua_r), 'res': {}}
    for ll in l_list:
        (q, r) = ll.split(' ')
        ret[res]['res'][r] = int(q)
    return ret


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
    def test_react(self):
        tests = (
            {
                "i": "7 A, 1 E => 1 FUEL",
                "r": {
                    'FUEL': {
                        'quantity': 1,
                        'res': {
                            'A': 7,
                            'E': 1,
                        },
                    },
                },
            },
        )
        for t in tests:
            self.assertDictEqual(react(t["i"]), t["r"], f'i: {t["i"]} for {t["r"]}')

    def test_day(self):
        tests = (
            {
                "i": '''10 ORE => 10 A
1 ORE => 1 B
7 A, 1 B => 1 C
7 A, 1 C => 1 D
7 A, 1 D => 1 E
7 A, 1 E => 1 FUEL''',
                "r": 31,
            },
        )
        for t in tests:
            self.assertEqual(day(t["i"]), t["r"], f'i: {t["i"]} for {t["r"]}')


if __name__ == '__main__':
    # run()
    unittest.main()
    