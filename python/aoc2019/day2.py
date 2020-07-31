import unittest
import copy

def day(n):
    i = 0
    while i < len(n):
        opcode = n[i]
        if opcode == 99:
            return n
        if i+3 > len(n):
            return n
        if opcode == 1:
            n[n[i+3]] = n[n[i+1]] + n[n[i+2]]
        elif opcode == 2:
            n[n[i+3]] = n[n[i+1]] * n[n[i+2]]
        else:
            return n
        i += 4
    return n



def run():
    ls = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,5,23,2,23,9,27,1,5,27,31,1,9,31,35,1,35,10,39,2,13,39,43,1,43,9,47,1,47,9,51,1,6,51,55,1,13,55,59,1,59,13,63,1,13,63,67,1,6,67,71,1,71,13,75,2,10,75,79,1,13,79,83,1,83,10,87,2,9,87,91,1,6,91,95,1,9,95,99,2,99,10,103,1,103,5,107,2,6,107,111,1,111,6,115,1,9,115,119,1,9,119,123,2,10,123,127,1,127,5,131,2,6,131,135,1,135,5,139,1,9,139,143,2,143,13,147,1,9,147,151,1,151,2,155,1,9,155,0,99,2,0,14,0]
    for i in range(99):
        for j in range(99):
            new_ls = copy.deepcopy(ls)
            new_ls[1] = i
            new_ls[2] = j
            day(new_ls)
            if new_ls[0] == 19690720:
                print(f">>>{i}, {j}")
                return
    print("error")
    return
 

class TestDay(unittest.TestCase):
    def test_day(self):
        tests = (
            {
                "i": [1,0,0,0,99],
                "r": [2,0,0,0,99],
            },
            {
                "i": [2,3,0,3,99],
                "r": [2,3,0,6,99],
            },
            {
                "i": [2,4,4,5,99,0],
                "r": [2,4,4,5,99,9801],
            },
            {
                "i": [1,1,1,4,99,5,6,0,99],
                "r": [30,1,1,4,2,5,6,0,99],
            },
        )
        for t in tests:
            self.assertListEqual(day(t["i"]), t["r"], f'i: {t["i"]} for {t["r"]}')

if __name__ == '__main__':
    run()
    unittest.main()
    