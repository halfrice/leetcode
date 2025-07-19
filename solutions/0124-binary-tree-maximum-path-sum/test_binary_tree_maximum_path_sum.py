from binary_tree_maximum_path_sum import Solution, Utils

solution = Solution()
utils = Utils()


def test_case_1():
    root = [1, 2, 3]
    root_tree = utils.list_to_tree(root)
    result = solution.maxPathSum(root_tree)
    expected = 6
    assert result == expected


def test_case_2():
    root = [-10, 9, 20, None, None, 15, 7]
    root_tree = utils.list_to_tree(root)
    result = solution.maxPathSum(root_tree)
    expected = 42
    assert result == expected
