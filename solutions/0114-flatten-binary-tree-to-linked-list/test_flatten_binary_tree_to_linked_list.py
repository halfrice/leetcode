from flatten_binary_tree_to_linked_list import Solution, Utils

solution = Solution()
utils = Utils()


def test_case_1():
    root = [1, 2, 5, 3, 4, None, 6]
    tree_root = utils.list_to_tree(root)
    solution.flatten(tree_root)
    result = utils.tree_to_list(tree_root)
    expected = [1, None, 2, None, 3, None, 4, None, 5, None, 6]
    assert result == expected


def test_case_2():
    root = []
    tree_root = utils.list_to_tree(root)
    solution.flatten(tree_root)
    result = utils.tree_to_list(tree_root)
    expected = []
    assert result == expected


def test_case_3():
    root = [0]
    tree_root = utils.list_to_tree(root)
    solution.flatten(tree_root)
    result = utils.tree_to_list(tree_root)
    expected = [0]
    assert result == expected
