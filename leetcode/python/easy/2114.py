# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/


class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        return max(len(sentence.split()) for sentence in sentences)


def test_2114():
    solution = Solution()
    assert solution.mostWordsFound(["alice and bob love leetcode","i think so too","this is great thanks very much"]) == 6
    assert solution.mostWordsFound(["please wait","continue to fight","continue to win"]) == 3
