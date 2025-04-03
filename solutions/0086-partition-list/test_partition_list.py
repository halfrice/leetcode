from partition_list import Solution, Utils

solution = Solution()
utils = Utils()


def test_case_1():
    head = [1, 4, 3, 2, 5, 2]
    x = 3
    linked_list = utils.list_to_linked_list(head)
    result_linked_list = solution.partition(linked_list, x)
    result = utils.linked_list_to_list(result_linked_list)
    expected = [1, 2, 2, 4, 3, 5]
    assert result == expected


def test_case_2():
    head = [2, 1]
    x = 2
    linked_list = utils.list_to_linked_list(head)
    result_linked_list = solution.partition(linked_list, x)
    result = utils.linked_list_to_list(result_linked_list)
    expected = [1, 2]
    assert result == expected
