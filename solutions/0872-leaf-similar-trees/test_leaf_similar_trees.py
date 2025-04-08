from leaf_similar_trees import Solution, Utils

solution = Solution()
utils = Utils()


def test_case_1():
    root1 = [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]
    root2 = [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]
    root1_tree = utils.list_to_tree(root1)
    root2_tree = utils.list_to_tree(root2)
    expected = True
    assert solution.leafSimilar(root1_tree, root2_tree) == expected


def test_case_2():
    root1 = [1, 2, 3]
    root2 = [1, 3, 2]
    root1_tree = utils.list_to_tree(root1)
    root2_tree = utils.list_to_tree(root2)
    expected = False
    assert solution.leafSimilar(root1_tree, root2_tree) == expected
