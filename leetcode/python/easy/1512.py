# https://leetcode.com/problems/number-of-good-pairs/


from itertools import combinations

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        num_good_pairs = 0
        for x, y in combinations(range(len(nums)), 2):
            if nums[x] == nums[y] and x < y:
                num_good_pairs+=1
        return num_good_pairs


def test_1512():
    solution = Solution()
    assert solution.numIdenticalPairs([1,2,3,1,1,3]) == 4
    assert solution.numIdenticalPairs([1,1,1,1]) == 6
    assert solution.numIdenticalPairs([1,2,3]) == 0
