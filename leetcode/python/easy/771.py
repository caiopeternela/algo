class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return len([stone for stone in list(stones) if stone in jewels])

def test_771():
    solution = Solution()
    assert solution.numJewelsInStones("aA", "aAAbbbb") == 3
    assert solution.numJewelsInStones("z", "ZZ") == 0
