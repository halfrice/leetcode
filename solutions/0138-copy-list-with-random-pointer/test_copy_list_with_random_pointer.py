from copy_list_with_random_pointer import Solution, Utils

solution = Solution()
utils = Utils()


def test_case_1():
    head = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    linked_list = utils.list_to_linked_list(head)
    result_linked_list = solution.copyRandomList(linked_list)
    result = utils.linked_list_to_list(result_linked_list)
    expected = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    assert result == expected


def test_case_2():
    head = [[1, 1], [2, 1]]
    linked_list = utils.list_to_linked_list(head)
    result_linked_list = solution.copyRandomList(linked_list)
    result = utils.linked_list_to_list(result_linked_list)
    expected = [[1, 1], [2, 1]]
    assert result == expected


def test_case_3():
    head = [[3, None], [3, 0], [3, None]]
    linked_list = utils.list_to_linked_list(head)
    result_linked_list = solution.copyRandomList(linked_list)
    result = utils.linked_list_to_list(result_linked_list)
    expected = [[3, None], [3, 0], [3, None]]
    assert result == expected
