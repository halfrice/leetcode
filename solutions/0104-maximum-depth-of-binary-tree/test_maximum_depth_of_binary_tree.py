from maximum_depth_of_binary_tree import Solution, Utils

solution = Solution()
utils = Utils()


def test_case_1():
    root = [3, 9, 20, None, None, 15, 7]
    tree = utils.list_to_tree(root)
    output = solution.maxDepth(tree)
    expected = 3
    assert output == expected


def test_case_2():
    root = [1, None, 2]
    tree = utils.list_to_tree(root)
    output = solution.maxDepth(tree)
    expected = 2
    assert output == expected
