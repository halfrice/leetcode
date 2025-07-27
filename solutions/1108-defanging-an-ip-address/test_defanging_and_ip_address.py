from defanging_and_ip_address import Solution

solution = Solution()


def test_case_1():
    address = '1.1.1.1'
    expected = '1[.]1[.]1[.]1'
    assert solution.defangIPaddr(address) == expected


def test_case_2():
    address = '255.100.50.0'
    expected = '255[.]100[.]50[.]0'
    assert solution.defangIPaddr(address) == expected
