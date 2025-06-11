from remove_duplicates_from_sorted_list import Solution, Utils

solution = Solution()
utils = Utils()


def test_case_1():
    head = [1, 1, 2]
    head_ll = utils.list_to_linked_list(head)
    res = solution.deleteDuplicates(head_ll)
    res_list = utils.linked_list_to_list(res)
    expected = [1, 2]
    assert res_list == expected


def test_case_2():
    head = [1, 1, 2, 3, 3]
    head_ll = utils.list_to_linked_list(head)
    res = solution.deleteDuplicates(head_ll)
    res_list = utils.linked_list_to_list(res)
    expected = [1, 2, 3]
    assert res_list == expected
