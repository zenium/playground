'''
We want to optimally compress a sequence of numbers uniformly drawn from the [0, a) range.

Why? Well, for instance to transmit the subsequent draws from a 12-dice (in this case, a = 12).
If we use four plain bits for each result, we'll lose some compression efficiency, since some values are unreachable.

To optimally compress this sequence, we need to find the probability for the four bits to be set to 1.
Then, using an arithmetic coder, we can transmit each values optimally.

Let's work out the example, and write all the numbers in [0,12) as binary:

#n   | binary representation
 0   | 0 0 0 0
 1   | 0 0 0 1
 2   | 0 0 1 0
 3   | 0 0 1 1
 4   | 0 1 0 0
 5   | 0 1 0 1
 6   | 0 1 1 0
 7   | 0 1 1 1
 8   | 1 0 0 0
 9   | 1 0 0 1
10   | 1 0 1 0
11   | 1 0 1 1
-----+---------
count| 4 4 6 6   <- number of bits set to '1' in each column

Hence, probability of bit #0 set to 1 for any number uniformly drawn in [0,12) is 6/12
And similarly: 
  bit #1: p = 6/12,
  bit #2: p = 4/12,
  bit #3: p = 4/12,
  bit #4 and seq.: p = 0/12

Now, in order to transmit a value 'n' using an arithmetic coder function AC(bit, probability), we'd call:

AC((n >> 0) & 1, 6/12)
AC((n >> 1) & 1, 6/12)
AC((n >> 2) & 1, 4/12)
AC((n >> 4) & 1, 4/12)

But! We of course want to generalize (who wouldn't?) to N-dice case, with N arbitrary.

So, let's write a function g(a, b) that counts the number of times the b-th bit will be set to '1' when considering all the integers in the [0, a) range.
'''

# def answer(a, b):
#     # p=2**b;r=a/p/2*p
#     # return r+a%p if a/p%2 else r

#     # p=2**b;r=a/p/2*p;return(r,r+a%p)[a/p%2]

#     # return sum([i/2**b%2 for i in range(a)])
#     return sum([(i>>b)%2 for i in range(a)])

def answer(a, b, i=0):
    x=i+a/2**b%2
    y=a>0 and answer(a-1,b,x) or i
    return y


def main():
    print(answer(12,1))
    print(answer(4120,12))
    print(answer(8204,6))
    print(answer(141152,2))


if __name__ == '__main__':
    main()