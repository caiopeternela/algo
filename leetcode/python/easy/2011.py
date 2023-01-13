class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        x = 0
        for operation in operations:
            if operation == "--X" or operation == "X--":
                x-=1
            else:
                x+=1
        return x


def test_2011():
    solution = Solution()
    assert solution.finalValueAfterOperations(["--X","X++","X++"]) == 1
    assert solution.finalValueAfterOperations(["++X","++X","X++"]) == 3
    assert solution.finalValueAfterOperations(["X++","++X","--X","X--"]) == 0
