from n_th_tribonacci_number import Solution


solution = Solution()


def test_case_1():
    n = 4
    expected = 4
    assert solution.tribonacci(n) == expected
