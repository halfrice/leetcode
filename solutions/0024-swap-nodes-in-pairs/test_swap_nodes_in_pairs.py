from swap_nodes_in_pairs import Solution, Utils

solution = Solution()
utils = Utils()


def test_case_1():
    head = [1, 2, 3, 4]
    head = utils.list_to_linked_list(head)
    result = solution.swapPairs(head)
    result = utils.linked_list_to_list(result)
    expected = [2, 1, 4, 3]
    assert result == expected


def test_case_2():
    head = []
    head = utils.list_to_linked_list(head)
    result = solution.swapPairs(head)
    result = utils.linked_list_to_list(result)
    expected = []
    assert result == expected


def test_case_3():
    head = [1]
    head = utils.list_to_linked_list(head)
    result = solution.swapPairs(head)
    result = utils.linked_list_to_list(result)
    expected = [1]
    assert result == expected


def test_case_4():
    head = [1, 2, 3]
    head = utils.list_to_linked_list(head)
    result = solution.swapPairs(head)
    result = utils.linked_list_to_list(result)
    expected = [2, 1, 3]
    assert result == expected
