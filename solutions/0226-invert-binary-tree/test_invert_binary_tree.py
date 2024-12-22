from invert_binary_tree import Solution, Utils

solution = Solution()
utils = Utils()


def test_case_1():
    head = [4, 2, 7, 1, 3, 6, 9]
    tree = utils.list_to_tree(head)
    output_tree = solution.invertTree(tree)
    utils.tree_to_list(output_tree)
    output = utils.nums
    expected = [4, 7, 2, 9, 6, 3, 1]
    assert output == expected


def test_case_2():
    head = [2, 1, 3]
    tree = utils.list_to_tree(head)
    output_tree = solution.invertTree(tree)
    utils.tree_to_list(output_tree)
    output = utils.nums
    expected = [2, 3, 1]
    assert output == expected


def test_case_3():
    head = []
    tree = utils.list_to_tree(head)
    output_tree = solution.invertTree(tree)
    utils.tree_to_list(output_tree)
    output = utils.nums
    expected = []
    assert output == expected
