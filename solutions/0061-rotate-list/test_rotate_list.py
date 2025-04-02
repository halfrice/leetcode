from rotate_list import Solution, Utils

solution = Solution()
utils = Utils()


def test_case_1():
    head = [1, 2, 3, 4, 5]
    k = 2
    linked_list = utils.list_to_linked_list(head)
    result_linked_list = solution.rotateRight(linked_list, k)
    result = utils.linked_list_to_list(result_linked_list)
    expected = [4, 5, 1, 2, 3]
    assert result == expected


def test_case_2():
    head = [0, 1, 2]
    k = 4
    linked_list = utils.list_to_linked_list(head)
    result_linked_list = solution.rotateRight(linked_list, k)
    result = utils.linked_list_to_list(result_linked_list)
    expected = [2, 0, 1]
    assert result == expected
