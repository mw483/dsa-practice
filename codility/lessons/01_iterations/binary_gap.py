"""
--- BINARY GAP ---
A binary gap within a positive integer N is any maximal sequence of consecutive zeros
that is surrounded by ones at both ends in the binary representation of N.
For example, number 9 has binary representation 1001 and contains a binary gap of length 2.
The number 529 has binary representation 1000010001 and contains two binary gaps:
one of length 4 and one of length 3.
The number 20 has binary representation 10100 and contains one binary gap of length 1.
The number 15 has binary representation 1111 and has no binary gaps.
The number 32 has binary representation 100000 and has no binary gaps.

Write a function:
class Solution { public int solution(int N); }

that, given a positive integer N, returns the length of its longest binary gap.
The function should return 0 if N doesn't contain a binary gap.
For example, given N = 1041 the function should return 5, because
N has binary representation 10000010001 and so its longest binary gap is of length 5.
Given N = 32 the function should return 0, because N has binary representation '100000'
and thus no binary gaps.
Write an efficient algorithm for the following assumptions:
N is an integer within the range [1..2,147,483,647].
"""
import unittest

def solution(N):
    if N == 0:
        return 0
    
    # initialize counters
    count = 0
    
    return final_count

class TestBinaryGap(unittest.TestCase):
    MAXINT = 2147483647  # The largest input we need worry about.

    def test_examples(self):
        self.assertEqual(solution(9), 2)
        self.assertEqual(solution(529), 4)
        self.assertEqual(solution(20), 1)
        self.assertEqual(solution(15), 0)
        self.assertEqual(solution(32), 0)

    def test_example1(self):
        self.assertEqual(5, solution(1041))

    def test_example2(self):
        self.assertEqual(0, solution(15))

    def test_extremes(self):
        self.assertEqual(0, solution(1))
        self.assertEqual(1, solution(5))
        self.assertEqual(0, solution(self.MAXINT))

    def test_trailing_zeros(self):
        self.assertEqual(solution(6), 0)
        self.assertEqual(solution(328), 2)

    def test_simple1(self):
        self.assertEqual(solution(9), 2)
        self.assertEqual(solution(11), 1)
        self.assertEqual(solution(32), 0)

    def test_simple2(self):
        self.assertEqual(solution(19), 2)
        self.assertEqual(solution(42), 1)

    def test_simple3(self):
        self.assertEqual(solution(1162), 3)
        self.assertEqual(solution(5), 1)

    def test_medium1(self):
        self.assertEqual(solution(51712), 2)
        self.assertEqual(solution(20), 1)

    def test_medium2(self):
        self.assertEqual(solution(561892), 3)
        self.assertEqual(solution(9), 2)

    def test_medium3(self):
        self.assertEqual(solution(66561), 9)

    def test_large1(self):
        self.assertEqual(solution(6291457), 20)

    def test_large2(self):
        self.assertEqual(solution(74901729), 4)

    def test_large3(self):
        self.assertEqual(solution(805306369), 27)

    def test_large4(self):
        self.assertEqual(solution(1376796946), 5)

    def test_large5(self):
        self.assertEqual(solution(1073741825), 29)

    def test_large6(self):
        self.assertEqual(solution(1610612737), 28)


if __name__ == "__main__":
    unittest.main()