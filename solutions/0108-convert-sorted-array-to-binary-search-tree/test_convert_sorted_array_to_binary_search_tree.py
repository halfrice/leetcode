from convert_sorted_array_to_binary_search_tree import Solution, Utils

solution = Solution()
utils = Utils()


def test_case_1():
    nums = [-10, -3, 0, 5, 9]
    expected = [0, -10, 5, None, -3, None, 9]
    result = solution.sortedArrayToBST(nums)
    result_list = utils.tree_to_list(result)
    assert result_list == expected


def test_case_2():
    nums = [1, 3]
    expected = [1, None, 3]
    result = solution.sortedArrayToBST(nums)
    result_list = utils.tree_to_list(result)
    assert result_list == expected
