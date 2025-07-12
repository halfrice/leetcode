from populating_next_right_pointers_in_each_node_ii import Solution, Utils

solution = Solution()
utils = Utils()


def test_case_1():
    root = [1, 2, 3, 4, 5, None, 7]
    root_tree = utils.list_to_tree(root)
    result = solution.connect(root_tree)
    result = utils.levels_list(result)
    expected = [1, '#', 2, 3, '#', 4, 5, 7, '#']
    assert result == expected


def test_case_2():
    root = []
    root_tree = utils.list_to_tree(root)
    result = solution.connect(root_tree)
    result = utils.levels_list(result)
    expected = []
    assert result == expected
