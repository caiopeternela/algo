# https://leetcode.com/problems/defanging-an-ip-address/


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")


def test_1108():
    solution = Solution()
    assert solution.defangIPaddr("1.1.1.1") == "1[.]1[.]1[.]1"
    assert solution.defangIPaddr("255.100.50.0") == "255[.]100[.]50[.]0"
