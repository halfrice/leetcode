from binary_tree_level_order_traversal import Solution, Utils

solution = Solution()
utils = Utils()


def test_case_1():
    root = [3, 9, 20, None, None, 15, 7]
    root_tree = utils.list_to_tree(root)
    result = solution.levelOrder(root_tree)
    expected = [[3], [9, 20], [15, 7]]
    assert result == expected


def test_case_2():
    root = [1]
    root_tree = utils.list_to_tree(root)
    result = solution.levelOrder(root_tree)
    expected = [[1]]
    assert result == expected


def test_case_3():
    root = []
    root_tree = utils.list_to_tree(root)
    result = solution.levelOrder(root_tree)
    expected = []
    assert result == expected
