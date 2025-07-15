from average_levels_in_binary_tree import Solution, Utils

solution = Solution()
utils = Utils()


def test_case_1():
    root = [3, 9, 20, None, None, 15, 7]
    root_tree = utils.list_to_tree(root)
    result = solution.averageOfLevels(root_tree)
    expected = [3.00000, 14.50000, 11.00000]
    assert result == expected


def test_case_2():
    root = [3, 9, 20, 15, 7]
    root_tree = utils.list_to_tree(root)
    result = solution.averageOfLevels(root_tree)
    expected = [3.00000, 14.50000, 11.00000]
    assert result == expected
