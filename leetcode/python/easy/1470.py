# https://leetcode.com/problems/shuffle-the-array/submissions/868734738

class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        shuffled_list = []
        for x, y in zip(nums[:n], nums[n:]):
            shuffled_list.extend([x, y])
        return shuffled_list


def test_1470():
    solution = Solution()
    assert solution.shuffle([2,5,1,3,4,7], 3) == [2,3,5,4,1,7]
    assert solution.shuffle([1,2,3,4,4,3,2,1], 4) == [1,4,2,3,3,2,4,1]
    assert solution.shuffle([1,1,2,2], 2) == [1,2,1,2]