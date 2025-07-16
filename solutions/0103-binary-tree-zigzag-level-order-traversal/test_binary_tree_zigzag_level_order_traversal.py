from binary_tree_zigzag_level_order_traversal import Solution, Utils

solution = Solution()
utils = Utils()


def test_case_1():
    root = [3, 9, 20, None, None, 15, 7]
    root_tree = utils.list_to_tree(root)
    result = solution.zigzagLevelOrder(root_tree)
    expected = [[3], [20, 9], [15, 7]]
    assert result == expected


def test_case_2():
    root = [1]
    root_tree = utils.list_to_tree(root)
    result = solution.zigzagLevelOrder(root_tree)
    expected = [[1]]
    assert result == expected


def test_case_3():
    root = []
    root_tree = utils.list_to_tree(root)
    result = solution.zigzagLevelOrder(root_tree)
    expected = []
    assert result == expected


def test_case_4():
    root = [1, 2, 3, 4, None, None, 5]
    root_tree = utils.list_to_tree(root)
    result = solution.zigzagLevelOrder(root_tree)
    expected = [[1], [3, 2], [4, 5]]
    assert result == expected
