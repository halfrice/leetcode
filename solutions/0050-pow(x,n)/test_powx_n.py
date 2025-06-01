from powx_n import Solution
import pytest

solution = Solution()


def test_case_1():
    x = 2.00000
    n = 10
    expected = 1024.00000
    assert pytest.approx(solution.myPow(x, n)) == expected


def test_case_2():
    x = 2.10000
    n = 3
    expected = 9.26100
    assert pytest.approx(solution.myPow(x, n)) == expected


def test_case_3():
    x = 2.00000
    n = -2
    expected = 0.25000
    assert pytest.approx(solution.myPow(x, n)) == expected
