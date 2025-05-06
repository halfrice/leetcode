from path_sum_iii import Solution, Utils

solution = Solution()
utils = Utils()


def test_case_1():
    root = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
    root_tree = utils.list_to_tree(root)
    targetSum = 8
    expected = 3
    assert solution.pathSum(root_tree, targetSum) == expected


def test_case_2():
    root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
    root_tree = utils.list_to_tree(root)
    targetSum = 22
    expected = 3
    assert solution.pathSum(root_tree, targetSum) == expected
