test = {   'name': 'q2_4',
    'points': [0, 0, 2],
    'suites': [   {   'cases': [   {'code': '>>> type(ab_test_stat) == np.ndarray\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> all([1 <= option <= 6 for option in ab_test_stat])\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> all([type(option) in set([np.int64, np.int32, int]) for option in list(ab_test_stat)])\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
