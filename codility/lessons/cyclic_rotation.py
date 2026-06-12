"""
# CyclicRotation

An array A consisting of N integers is given. Rotation of the array means that
each element is shifted right by one index, and the last element of the array
is moved to the first place.

For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7]
(elements are shifted right by one index and 6 is moved to the first place).

The goal is to rotate array A K times; that is, each element of A will be
shifted to the right K times.

Write a function:

    class Solution { public int[] solution(int[] A, int K); }

that, given an array A consisting of N integers and an integer K,
returns the array A rotated K times.

For example, given
    A = [3, 8, 9, 7, 6]
    K = 3

the function should return [9, 7, 6, 3, 8]. Three rotations were made:
    [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
    [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
    [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]

For another example, given
    A = [0, 0, 0]
    K = 1

the function should return [0, 0, 0]

Given
    A = [1, 2, 3, 4]
    K = 4

the function should return [1, 2, 3, 4]

Assume that:

        N and K are integers within the range [0..100];
        each element of array A is an integer within the range [−1,000..1,000].

In your solution, focus on correctness. The performance of your solution will
not be the focus of the assessment.

Copyright 2009–2022 by Codility Limited. All Rights Reserved.
Unauthorized copying, publication or disclosure prohibited.
"""
import unittest
import random

# For interactive testing
# A = [6, 3, 8, 9, 7]
# K = 3

# length = len(A)
# if not length:
#     print(A)

# mod_k = (length + K) % length

# # No rotations required
# if mod_k == 0:
#     print(A)

# head = A[: mod_k]
# print(f"Head: {head}")
# tail = A[length - mod_k:]
# print(f"Tail: {tail}")
# res = tail + head

# print(f"res: {res}")

def solution(A: list, K: int):
    # return array as is if empty
    length = len(A)
    if not length:
        return A

    mod_k = (length + K) % length

    # No rotations required
    if mod_k == 0:
        return A
    
    head = A[: -mod_k]
    tail = A[length - mod_k:]
    res = tail + head

    return res


ARRAY_RANGE = (-1000, 1000)
INT_RANGE = (0, 100)

class TestCyclicRotation(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(solution([3, 8, 9, 7, 6], 3), [9, 7, 6, 3, 8])
        self.assertEqual(solution([0, 0, 0], 1), [0, 0, 0])
        self.assertEqual(solution([1, 2, 3, 4], 4), [1, 2, 3, 4])

    def test_zero(self):
        self.assertEqual(solution([6, 3, 8, 9, 7], 0), [6, 3, 8, 9, 7])

    def test_one(self):
        self.assertEqual(solution([6, 3, 8, 9, 7], 1), [7, 6, 3, 8, 9])

    def test_full(self):
        self.assertEqual(solution([6, 3, 8, 9, 7], 5), [6, 3, 8, 9, 7])

    def test_empty(self):
        self.assertEqual(solution([], 5), [])

    def test_random(self):
        N = random.randint(*INT_RANGE)
        K = random.randint(*INT_RANGE)
        A = [random.randint(*ARRAY_RANGE) for _ in range(0, N)]
        print(K, A)
        print(solution(A, K))

if __name__ == "__main__":
    unittest.main()