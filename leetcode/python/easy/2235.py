# https://leetcode.com/problems/add-two-integers/


class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2


def test_2235():
    solution = Solution()
    assert solution.sum(12, 5) == 17
    assert solution.sum(-10, 4) == -6
