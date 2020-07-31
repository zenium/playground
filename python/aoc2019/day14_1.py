import unittest
import copy

test_res = {
    'FUEL': {
        'quantity': 1,
        'lvl': 0,
        'res': {
            'A': 7,
            'E': 1,
        }
    },
    'A': {
        'quantity': 10,
        'lvl': 1,
        'res': {
            'ORE': 10,
        }
    },
    'E': {
        'quantity': 1,
        'lvl': 1,
        'res': {
            'A': 7,
            'D': 1,
        }
    },
    'D': {
        'quantity': 1,
        'lvl': 2,
        'res': {
            'A': 7,
            'C': 1,
        }
    },
    'C': {
        'quantity': 1,
        'lvl': 3,
        'res': {
            'A': 7,
            'B': 1,
        }
    },
    'B': {
        'quantity': 1,
        'lvl': 4,
        'res': {
            'ORE': 1,
        }
    },
}

{
    'A': 7,
    'E': 1,
}
{
    'A': 14,
    'D': 1,
}


all_res = {}


def day(ls):
    global all_res
    for l in ls.split('\n'):
        all_res.update(react(l))

    total_ore = 0
    fuel = all_res['FUEL']['res']
    while not all(list(all_res[r]['res']) == ['ORE'] for r in fuel):
        fold_res(fuel)
        if not all(is_left_or_ore(f, fuel[f]) for f in fuel):
            continue
        print([(i, fuel[i]) for i in sorted(list(fuel))])
        print('___')
        for f in list(fuel):
            if list(all_res[f]['res']) == ['ORE']:
                continue
            else:
                if fuel[f] % all_res[f]['quantity']:
                    times = int(fuel[f]//all_res[f]['quantity'])
                    fuel[f] = fuel[f] % all_res[f]['quantity']
                else:
                    times = int(fuel[f]/all_res[f]['quantity'])
                    fuel.pop(f)
                for r in all_res[f]['res']:
                    if r not in fuel:
                        fuel[r] = times * all_res[f]['res'][r]
                    else:
                        fuel[r] += times * all_res[f]['res'][r]
    for f in fuel:
        if fuel[f] % all_res[f]['quantity']:
            times = int(fuel[f]//all_res[f]['quantity'] + 1)
        else:
            times = int(fuel[f]/all_res[f]['quantity'])
        total_ore += times * all_res[f]['res']['ORE']
    return total_ore


def is_left_or_ore(name, req):
    if req % all_res[name]['quantity']:
        return True
    if list(all_res[name]['res']) == ['ORE']:
        return True
    return False


def fold_res(res):
    global all_res
    for r in list(res):
        if list(all_res[r]['res']) == ['ORE']:
            continue
        if res[r] % all_res[r]['quantity'] > 0:
            continue
        times = int(res[r] / all_res[r]['quantity'])
        res.pop(r)
        temp_r = fold_res(all_res[r]['res'])
        for t in temp_r:
            if t not in res:
                res[t] = temp_r[t] * times
            else:
                res[t] += temp_r[t] * times
    return res


def react(s):
    ret = {}
    (l, r) = s.lstrip().rstrip().split(' => ')
    (qua_r, res) = r.split(' ')
    l_list = l.split(', ')
    ret[res] = {'quantity': int(qua_r), 'res': {}, 'lvl': 0}
    for ll in l_list:
        (q, r) = ll.split(' ')
        ret[res]['res'][r] = int(q)

    return ret

def addlvl(ret):
    if ret[]


def run():
    ipt = '''2 JNLZG => 7 SJTKF
1 BDCJZ, 3 NWCRL => 5 PMQS
1 TNRBS => 2 LHNGR
7 TWHBV => 6 FLQSP
4 DNLQF, 3 DRFL, 4 RSHRF => 6 HXJFS
5 VHSLS => 7 DZDQN
11 STPXT, 16 XRTW => 1 CTZFK
5 BXWD => 2 RVNR
1 XRTW, 2 SJTKF => 2 FPKWZ
1 JMGDP, 3 TJLKW => 7 FNLF
26 DTQTB, 16 TWHBV => 3 JMGDP
1 DFRNL, 1 LHNGR => 9 NWCRL
2 NWPC, 2 LHNGR, 3 QCHC => 8 HPBP
10 CSKJQ => 4 QRSD
8 FVLQ => 6 WMBVF
11 NPVB, 12 QRFV => 6 STPXT
3 SJTKF, 1 NPVB => 7 GWHG
4 DKPKX, 1 SJPWK => 5 DTQTB
1 RVNR => 8 XRTW
67 KGVR, 1 ZLJR, 4 TBPB, 19 KPJZM, 8 QSWQ, 12 DTQTB, 15 QRSD, 4 FPKWZ => 1 FUEL
20 LHNGR, 6 DNLQF, 9 TWHBV => 8 SJPWK
1 QRSD, 11 HZWS => 5 KGVR
2 CTZFK, 1 DRFL, 1 TNRBS => 5 DKPKX
14 FVFTN, 2 VLKQ, 12 STPXT => 4 TWHBV
1 FXWRB, 1 BXWD => 8 FVFTN
12 NPVB, 2 KJWC, 1 JNLZG => 3 NDNZP
13 NPVB, 7 HZLKM => 3 ZRMQC
2 HXJFS, 14 PDGB, 2 FNLF => 1 FVLQ
7 QRFV, 10 QRSD, 6 FVFTN => 5 DNLQF
4 XQDC, 2 VHSLS => 1 BDCJZ
9 HZLKM, 1 NDNZP => 6 DRFL
147 ORE => 4 BXWD
6 DNLQF => 5 VCBFZ
1 FVFTN => 8 TNRBS
1 RSHRF, 2 PDGB, 1 MKWH, 4 QRSD, 11 DNLQF, 7 WMBVF, 1 HJHM => 8 QSWQ
6 PMQS, 2 HNTS => 1 WNVGC
4 RVNR, 6 GWHG => 2 VLKQ
11 DRFL, 1 PDGB => 6 DFRNL
3 WNVGC, 28 PFZN, 14 HNTS, 2 WMBVF, 18 VCBFZ, 2 HPBP, 2 PDGB => 6 TBPB
2 XQDC => 6 HZWS
7 JNLZG, 1 BXWD, 7 FXWRB => 5 KJWC
9 KJWC, 7 NDNZP => 4 CSKJQ
194 ORE => 9 FXWRB
2 VHSLS, 12 MKWH, 2 FWBL, 6 TJLKW, 9 HZWS, 11 ZQGXM => 5 ZLJR
139 ORE => 2 JNLZG
2 TNRBS => 2 QCHC
7 DRFL, 10 STPXT, 1 QRSD => 6 MKWH
9 JNLZG => 8 NPVB
3 RSHRF => 6 FWBL
7 NDNZP => 5 PDGB
2 FVFTN => 6 QRFV
1 QRSD, 22 XQDC => 3 VHSLS
2 FVFTN => 3 HZLKM
6 ZRMQC => 2 PFZN
12 QRFV, 6 HZLKM => 6 XQDC
12 JMGDP, 1 KPJZM, 10 ZPKP => 5 HJHM
23 JNLZG => 2 ZQGXM
1 TJLKW => 9 HNTS
1 HZLKM, 12 PMQS => 5 KPJZM
7 DNLQF => 9 NWPC
1 FLQSP => 6 ZPKP
5 VLKQ => 7 RSHRF
6 TNRBS, 4 DZDQN, 6 TWHBV => 6 TJLKW'''
    print(day(ipt))


class TestDay(unittest.TestCase):
    def test_react(self):
        tests = (
            {
                "i": "7 A, 1 E => 1 FUEL",
                "r": {
                    'FUEL': {
                        'quantity': 1,
                        'lvl': 0,
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

    @unittest.skip('')
    def test_fold_res(self):
        tests = (
            {
                'res': {'A': 7, 'E': 1},
                'all_res': test_res,
                'exp': {'A': 28, 'B': 1},
            },
        )
        for t in tests:
            global all_res
            all_res = t['all_res']
            res = fold_res(t['res'])
            self.assertDictEqual(res, t['exp'])

    @unittest.skip('')
    def test_day(self):
        tests = (
            # {
            #     "i": '''10 ORE => 10 A
            #             1 ORE => 1 B
            #             7 A, 1 B => 1 C
            #             7 A, 1 C => 1 D
            #             7 A, 1 D => 1 E
            #             7 A, 1 E => 1 FUEL''',
            #     "r": 31,
            # },
            # {
            #     "i": '''9 ORE => 2 A
            #             8 ORE => 3 B
            #             7 ORE => 5 C
            #             3 A, 4 B => 1 AB
            #             5 B, 7 C => 1 BC
            #             4 C, 1 A => 1 CA
            #             2 AB, 3 BC, 4 CA => 1 FUEL''',
            #     "r": 165,
            # },
            # {
            #     "i": '''157 ORE => 5 NZVS
            #             165 ORE => 6 DCFZ
            #             44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
            #             12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
            #             179 ORE => 7 PSHF
            #             177 ORE => 5 HKGWZ
            #             7 DCFZ, 7 PSHF => 2 XJWVT
            #             165 ORE => 2 GPVTF
            #             3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT''',
            #     "r": 13312,
            # },
            # {
            #     "i": '''2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG
            #             17 NVRVD, 3 JNWZP => 8 VPVL
            #             53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL
            #             22 VJHF, 37 MNCFX => 5 FWMGM
            #             139 ORE => 4 NVRVD
            #             144 ORE => 7 JNWZP
            #             5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC
            #             5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV
            #             145 ORE => 6 MNCFX
            #             1 NVRVD => 8 CXFTF
            #             1 VJHF, 6 MNCFX => 4 RFSQX
            #             176 ORE => 6 VJHF''',
            #     "r": 180697,
            # },
            {
                "i": '''171 ORE => 8 CNZTR
                        7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL
                        114 ORE => 4 BHXH
                        14 VRPVC => 6 BMBT
                        6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL
                        6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT
                        15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW
                        13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW
                        5 BMBT => 4 WPTQ
                        189 ORE => 9 KTJDG
                        1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP
                        12 VRPVC, 27 CNZTR => 2 XDBXC
                        15 KTJDG, 12 BHXH => 5 XCVML
                        3 BHXH, 2 VRPVC => 7 MZWV
                        121 ORE => 7 VRPVC
                        7 XCVML => 6 RJRHP
                        5 BHXH, 4 VRPVC => 5 LTCX''',
                "r": 2210736,
            },
        )

        for t in tests:
            self.assertEqual(
                day(t["i"]),
                t["r"],
                'i: %s for %s' % (t["i"], t["r"]))


if __name__ == '__main__':
    unittest.main()
    # run()
