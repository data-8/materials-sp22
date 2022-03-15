test = {   'name': 'q2_8',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> test_stat = round(simulate_and_test_statistic(bakers, "won", "star baker awards"), 3)\n>>> -2 < test_stat < 2\nTrue',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> np.random.seed(1)\n'
                                               '>>> test_stat2 = simulate_and_test_statistic(bakers, "won", "star baker awards")\n'
                                               '>>> np.round(test_stat2, 3) == -0.023 or np.round(test_stat2, 3) == -0.132\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
