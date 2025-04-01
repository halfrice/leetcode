from remove_duplicates_from_sorted_list_ii import Solution, Utils

solution = Solution()
utils = Utils()


def test_case_1():
    head = [1, 2, 3, 3, 4, 4, 5]
    linked_list = utils.list_to_linked_list(head)
    result_linked_list = solution.deleteDuplicates(linked_list)
    result = utils.linked_list_to_list(result_linked_list)
    expected = [1, 2, 5]
    assert result == expected


def test_case_2():
    head = [1, 1, 1, 2, 3]
    linked_list = utils.list_to_linked_list(head)
    result_linked_list = solution.deleteDuplicates(linked_list)
    result = utils.linked_list_to_list(result_linked_list)
    expected = [2, 3]
    assert result == expected
