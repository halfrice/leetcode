from flipping_an_image import Solution

solution = Solution()


def test_case_1():
    image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    expected = [[1, 0, 0], [0, 1, 0], [1, 1, 1]]
    assert solution.flipAndInvertImage(image) == expected
