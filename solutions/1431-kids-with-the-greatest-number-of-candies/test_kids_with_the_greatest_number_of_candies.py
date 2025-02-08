from kids_with_the_greatest_number_of_candies import Solution

solution = Solution()


def test_case_1():
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3
    expected = [True, True, True, False, True]
    assert solution.kidsWithCandies(candies, extraCandies) == expected


def test_case_2():
    candies = [4, 2, 1, 1, 2]
    extraCandies = 1
    expected = [True, False, False, False, False]
    assert solution.kidsWithCandies(candies, extraCandies) == expected
