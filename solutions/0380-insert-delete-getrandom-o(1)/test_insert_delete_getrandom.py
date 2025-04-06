from insert_delete_getrandom import Utils

utils = Utils()


def test_case_1():
    calls = [
        'RandomizedSet',
        'insert',
        'remove',
        'insert',
        'getRandom',
        'remove',
        'insert',
        'getRandom',
    ]
    vals = [[], [1], [2], [2], [], [1], [2], []]
    expected = [None, True, False, True, 2, True, False, 2]
    result = utils.command(list(zip(calls, vals)))

    # Omit testing 'getRandom'
    new_result = []
    new_expected = []

    if len(result) == len(expected):
        for i in range(len(calls)):
            c = calls[i]

            if c != 'getRandom':
                new_result.append(result[i])
                new_expected.append(expected[i])

    assert new_result == new_expected
