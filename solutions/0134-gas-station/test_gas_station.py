from gas_station import Solution

solution = Solution()


def test_case_1():
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    expected = 3
    assert solution.canCompleteCircuit(gas, cost) == expected


def test_case_2():
    gas = [2, 3, 4]
    cost = [3, 4, 3]
    expected = -1
    assert solution.canCompleteCircuit(gas, cost) == expected
