class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        to_kelvin = celsius + 273.15
        to_fahrenheit = (celsius * 1.8) + 32
        return [to_kelvin, to_fahrenheit]


def test_2469():
    solution = Solution()
    assert solution.convertTemperature(36.50) == [309.65000,97.70000]
    assert solution.convertTemperature(122.11) == [395.26000,251.79800]
