from same_tree import Solution, Utils

solution = Solution()
utils = Utils()


def test_case_1():
    p = [1, 2, 3]
    q = [1, 2, 3]
    p_tree = utils.list_to_tree(p)
    q_tree = utils.list_to_tree(q)
    expected = True
    assert solution.isSameTree(p_tree, q_tree) == expected


def test_case_2():
    p = [1, 2]
    q = [1, None, 2]
    p_tree = utils.list_to_tree(p)
    q_tree = utils.list_to_tree(q)
    expected = False
    assert solution.isSameTree(p_tree, q_tree) == expected


def test_case_3():
    p = [1, 2, 1]
    q = [1, 1, 2]
    p_tree = utils.list_to_tree(p)
    q_tree = utils.list_to_tree(q)
    expected = False
    assert solution.isSameTree(p_tree, q_tree) == expected
