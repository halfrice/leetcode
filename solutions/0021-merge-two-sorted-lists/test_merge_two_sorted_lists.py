from merge_two_sorted_lists import Solution, Utils

solution = Solution()
utils = Utils()


def test_case_1():
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]
    list1 = utils.list_to_linked_list(list1)
    list2 = utils.list_to_linked_list(list2)
    output = solution.mergeTwoLists(list1, list2)
    output = utils.linked_list_to_list(output)
    expected = [1, 1, 2, 3, 4, 4]
    assert output == expected


def test_case_2():
    list1 = []
    list2 = []
    list1 = utils.list_to_linked_list(list1)
    list2 = utils.list_to_linked_list(list2)
    output = solution.mergeTwoLists(list1, list2)
    output = utils.linked_list_to_list(output)
    expected = []
    assert output == expected


def test_case_3():
    list1 = []
    list2 = [0]
    list1 = utils.list_to_linked_list(list1)
    list2 = utils.list_to_linked_list(list2)
    output = solution.mergeTwoLists(list1, list2)
    output = utils.linked_list_to_list(output)
    expected = [0]
    assert output == expected
