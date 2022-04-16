test = {   'name': 'q2_1_2',
    'points': [1, 2],
    'suites': [   {   'cases': [   {   'code': '>>> correct_dis = 0.001406116\n'
                                               '>>> dis = distance_two_features("clerks.", "the godfather", "water", "feel")\n'
                                               '>>> np.isclose(np.round(dis, 9), correct_dis) # Make sure you can use any two movies\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> correct_dis = 0.005647119\n'
                                               '>>> dis = distance_two_features("clerks.", "the godfather", "your", "that")\n'
                                               '>>> np.isclose(np.round(dis, 9), correct_dis) # Make sure you can use any two features\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
