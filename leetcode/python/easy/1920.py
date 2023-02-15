# https://leetcode.com/problems/build-array-from-permutation/submissions/865993186

class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        return [nums[i] for i in nums]


def test_1920():
    solution = Solution()
    assert solution.buildArray([0,2,1,5,3,4]) == [0,1,2,4,5,3]
    assert solution.buildArray([5,0,1,2,3,4]) == [4,5,0,1,2,3]
