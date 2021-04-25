'''
there's a ticket system. 1 day cost $2, 7 days cost $7, 30 days cost $22
given a number of days in a month, find the lowest ticket fee.
[4,5,6] -> $6
[4,5,7,9] -> $7
[4,5,7,20] -> $9
[2,10,20] -> $6
'''
import unittest


def ticket(dates):
    # a dict of options. Date the option can support: cost
    # during the DP, if two options can support till the same date, keep the lowest cost.
    dp = {0: 0}
    for d in dates:
        new_dp = {}
        for date, cost in dp.items():
            if d <= date:
                new_dp[date] = cost
            else:
                single_cost = cost + 2
                if any([d not in new_dp,
                        d in new_dp and single_cost < new_dp[d]]):
                    new_dp[d] = single_cost
                week_cost = cost + 7
                weekend = d + 7
                if any([weekend not in new_dp,
                        weekend in new_dp and week_cost < new_dp[weekend]]):
                    new_dp[weekend] = week_cost
        dp = new_dp
        print(dp)
    return min(list(dp.values()) + [22])


class simpletest(unittest.TestCase):
    def setUp(self):
        pass

    def testmergeSort(self):
        tests = [
            ([4, 5, 6], 6),
            ([4, 5, 7, 9], 7),
            ([4, 5, 7, 20], 8),
            ([2, 10, 20], 6),
            ([1, 6, 7, 9, 10], 9)
        ]
        for l, v in tests:
            self.assertEqual(ticket(l), v)


if __name__ == '__main__':
    unittest.main()
