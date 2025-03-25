from maximum_twin_sum_of_a_linked_list import Solution, Utils

solution = Solution()
utils = Utils()


def test_case_1():
    head = [5, 4, 2, 1]
    linked_list = utils.list_to_linked_list(head)
    expected = 6
    assert solution.pairSum(linked_list) == expected


def test_case_2():
    head = [4, 2, 2, 3]
    linked_list = utils.list_to_linked_list(head)
    expected = 7
    assert solution.pairSum(linked_list) == expected


def test_case_3():
    head = [1, 100000]
    linked_list = utils.list_to_linked_list(head)
    expected = 100001
    assert solution.pairSum(linked_list) == expected
