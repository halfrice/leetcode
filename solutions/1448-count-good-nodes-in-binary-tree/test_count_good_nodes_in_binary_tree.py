from count_good_nodes_in_binary_tree import Solution, Utils

solution = Solution()
utils = Utils()


def test_case_1():
    root = [3, 1, 4, 3, None, 1, 5]
    root_tree = utils.list_to_tree(root)
    expected = 4
    assert solution.goodNodes(root_tree) == expected


def test_case_2():
    root = [3, 3, None, 4, 2]
    root_tree = utils.list_to_tree(root)
    expected = 3
    assert solution.goodNodes(root_tree) == expected


def test_case_3():
    root = [1]
    root_tree = utils.list_to_tree(root)
    expected = 1
    assert solution.goodNodes(root_tree) == expected
