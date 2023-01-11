class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return nums*2


def test_1929():
    solution = Solution()
    assert solution.getConcatenation([1,2,1]) == [1,2,1,1,2,1]
    assert solution.getConcatenation([1,3,2,1]) == [1,3,2,1,1,3,2,1]
