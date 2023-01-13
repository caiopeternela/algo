class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        out = []
        for index, num in enumerate(nums):
            total = sum(nums[:index])
            out.append(num+total)
        return out


def test_1480():
    solution = Solution()
    assert solution.runningSum([1,2,3,4]) == [1,3,6,10]
    assert solution.runningSum([1,1,1,1,1]) == [1,2,3,4,5]
    assert solution.runningSum([3,1,2,10,1]) == [3,4,6,16,17]
