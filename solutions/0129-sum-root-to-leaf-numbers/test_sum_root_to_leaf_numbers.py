from sum_root_to_leaf_numbers import Solution, Utils

solution = Solution()
utils = Utils()


def test_case_1():
    root = [1, 2, 3]
    root_tree = utils.list_to_tree(root)
    result = solution.sumNumbers(root_tree)
    expected = 25
    assert result == expected


def test_case_2():
    root = [4, 9, 0, 5, 1]
    root_tree = utils.list_to_tree(root)
    result = solution.sumNumbers(root_tree)
    expected = 1026
    assert result == expected
