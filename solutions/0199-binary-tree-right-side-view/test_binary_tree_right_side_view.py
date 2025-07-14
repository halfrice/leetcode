from binary_tree_right_side_view import Solution, Utils

solution = Solution()
utils = Utils()


def test_case_1():
    root = [1, 2, 3, None, 5, None, 4]
    root_tree = utils.list_to_tree(root)
    result = solution.rightSideView(root_tree)
    expected = [1, 3, 4]
    assert result == expected


def test_case_2():
    root = [1, 2, 3, 4, None, None, None, 5]
    root_tree = utils.list_to_tree(root)
    result = solution.rightSideView(root_tree)
    expected = [1, 3, 4, 5]
    assert result == expected


def test_case_3():
    root = [1, None, 3]
    root_tree = utils.list_to_tree(root)
    result = solution.rightSideView(root_tree)
    expected = [1, 3]
    assert result == expected


def test_case_4():
    root = []
    root_tree = utils.list_to_tree(root)
    result = solution.rightSideView(root_tree)
    expected = []
    assert result == expected
