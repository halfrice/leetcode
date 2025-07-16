from count_complete_tree_nodes import Solution, Utils

solution = Solution()
utils = Utils()


def test_case_1():
    root = [1, 2, 3, 4, 5, 6]
    root_tree = utils.list_to_tree(root)
    result = solution.countNodes(root_tree)
    expected = 6
    assert result == expected


def test_case_2():
    root = []
    root_tree = utils.list_to_tree(root)
    result = solution.countNodes(root_tree)
    expected = 0
    assert result == expected


def test_case_3():
    root = [1]
    root_tree = utils.list_to_tree(root)
    result = solution.countNodes(root_tree)
    expected = 1
    assert result == expected
