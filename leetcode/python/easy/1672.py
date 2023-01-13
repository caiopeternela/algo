class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        return max(list(map(sum, accounts)))


def test_1672():
    solution = Solution()
    assert solution.maximumWealth([[1,2,3],[3,2,1]]) == 6
    assert solution.maximumWealth([[1,5],[7,3],[3,5]]) == 10
    assert solution.maximumWealth([[2,8,7],[7,1,3],[1,9,5]]) == 17
