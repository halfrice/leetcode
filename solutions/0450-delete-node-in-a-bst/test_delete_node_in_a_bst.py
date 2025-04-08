from delete_node_in_a_bst import Solution, Utils

solution = Solution()
utils = Utils()


def test_case_1():
    root = [5, 3, 6, 2, 4, None, 7]
    key = 3
    root_tree = utils.list_to_tree(root)
    result_tree = solution.deleteNode(root_tree, key)
    result = utils.tree_to_list(result_tree)
    expected = [5, 4, 6, 2, None, None, 7]
    assert result == expected


def test_case_2():
    root = [5, 3, 6, 2, 4, None, 7]
    key = 0
    root_tree = utils.list_to_tree(root)
    result_tree = solution.deleteNode(root_tree, key)
    result = utils.tree_to_list(result_tree)
    expected = [5, 3, 6, 2, 4, None, 7]
    assert result == expected


def test_case_3():
    root = []
    key = 0
    root_tree = utils.list_to_tree(root)
    result_tree = solution.deleteNode(root_tree, key)
    result = utils.tree_to_list(result_tree)
    expected = []
    assert result == expected
