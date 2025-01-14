from remove_element import Solution

solution = Solution()


def test_case_1():
    nums = [3, 2, 2, 3]
    val = 3
    expected = 2
    output = solution.removeElement(nums, val)
    assert output == expected
    assert val not in nums[:output]


def test_case_2():
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    expected = 5
    output = solution.removeElement(nums, val)
    assert output == expected
    assert val not in nums[:output]


def test_case_3():
    nums = [3, 3]
    val = 5
    expected = 2
    output = solution.removeElement(nums, val)
    assert output == expected
    assert val not in nums[:output]


def test_case_4():
    nums = [3, 3, 2, 2, 3, 2, 1]
    val = 3
    expected = 4
    output = solution.removeElement(nums, val)
    assert output == expected
    assert val not in nums[:output]


def test_case_5():
    nums = [1]
    val = 1
    expected = 0
    output = solution.removeElement(nums, val)
    assert output == expected
    assert val not in nums[:output]
