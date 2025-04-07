from minimum_absolute_difference_in_bst import Solution, Utils

solution = Solution()
utils = Utils()


def test_case_1():
    root = [4, 2, 6, 1, 3]
    root_tree = utils.list_to_tree(root)
    expected = 1
    assert solution.getMinimumDifference(root_tree) == expected


def test_case_2():
    root = [1, 0, 48, None, None, 12, 49]
    root_tree = utils.list_to_tree(root)
    expected = 1
    assert solution.getMinimumDifference(root_tree) == expected
