from merge_k_sorted_lists import Solution, Utils

solution = Solution()
utils = Utils()


def test_case_1():
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    linked_lists = [utils.list_to_linked_list(li) for li in lists]
    result_linked_list = solution.mergeKLists(linked_lists)
    result = utils.linked_list_to_list(result_linked_list)
    expected = [1, 1, 2, 3, 4, 4, 5, 6]
    assert result == expected


def test_case_2():
    lists = []
    linked_lists = [utils.list_to_linked_list(li) for li in lists]
    result_linked_list = solution.mergeKLists(linked_lists)
    result = utils.linked_list_to_list(result_linked_list)
    expected = []
    assert result == expected


def test_case_3():
    lists = [[]]
    linked_lists = [utils.list_to_linked_list(li) for li in lists]
    result_linked_list = solution.mergeKLists(linked_lists)
    result = utils.linked_list_to_list(result_linked_list)
    expected = []
    assert result == expected
