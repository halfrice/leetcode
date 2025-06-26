from insertion_sort_list import Solution, Utils

solution = Solution()
utils = Utils()


def test_case_1():
    head = [4, 2, 1, 3]
    head_as_linked_list = utils.list_to_linked_list(head)
    result_as_linked_list = solution.insertionSortList(head_as_linked_list)
    result = utils.linked_list_to_list(result_as_linked_list)
    expected = [1, 2, 3, 4]
    assert result == expected


def test_case_2():
    head = [-1, 5, 3, 4, 0]
    head_as_linked_list = utils.list_to_linked_list(head)
    result_as_linked_list = solution.insertionSortList(head_as_linked_list)
    result = utils.linked_list_to_list(result_as_linked_list)
    expected = [-1, 0, 3, 4, 5]
    assert result == expected


def test_case_3():
    head = [1]
    head_as_linked_list = utils.list_to_linked_list(head)
    result_as_linked_list = solution.insertionSortList(head_as_linked_list)
    result = utils.linked_list_to_list(result_as_linked_list)
    expected = [1]
    assert result == expected
