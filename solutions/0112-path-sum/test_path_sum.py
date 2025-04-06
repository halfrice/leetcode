from path_sum import Solution, Utils

solution = Solution()
utils = Utils()


def test_case_1():
    root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    targetSum = 22
    root_tree = utils.list_to_tree(root)
    expected = True
    assert solution.hasPathSum(root_tree, targetSum) == expected


def test_case_2():
    root = [1, 2, 3]
    targetSum = 5
    root_tree = utils.list_to_tree(root)
    expected = False
    assert solution.hasPathSum(root_tree, targetSum) == expected
