test = {   'name': 'q1_2',
    'points': [0],
    'suites': [   {   'cases': [   {   'code': '>>> # Ensure your correlation function returns one number between -1 and 1\n'
                                               '>>> abs(correlation(Table().with_columns(\'a\', np.random.normal(0, 1, 10),\'b\', np.random.normal(0, 1, 10)), "a", "b")) <= 1\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
