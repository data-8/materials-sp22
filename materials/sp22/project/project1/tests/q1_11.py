test = {   'name': 'q1_11',
    'points': [0, 0, 0, 4],
    'suites': [   {   'cases': [   {   'code': '>>> # Incorrect labels for columns\n'
                                               '>>> t = stats_for_year(1990)\n'
                                               ">>> t.labels == ('geo', 'population_total', 'children_per_woman_total_fertility', 'child_mortality_under_5_per_1000_born')\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> # Incorrect number of rows\n>>> t = stats_for_year(1990)\n>>> t.num_rows\n50', 'hidden': False, 'locked': False},
                                   {   'code': ">>> print(stats_for_year(1960).sort('geo').take(np.arange(5, 50, 5)))\n"
                                               'geo  | population_total | children_per_woman_total_fertility | child_mortality_under_5_per_1000_born\n'
                                               'can  | 17847404         | 3.88                               | 32.6\n'
                                               'dza  | 11057864         | 7.52                               | 242.54\n'
                                               'gbr  | 52370595         | 2.69                               | 26.56\n'
                                               'irq  | 7289753          | 6.25                               | 191.93\n'
                                               'mar  | 12328532         | 7.04                               | 237.06\n'
                                               'nga  | 45138460         | 6.35                               | 339.85\n'
                                               'pol  | 29614201         | 3.11                               | 65.03\n'
                                               'tur  | 27472339         | 6.37                               | 258.29\n'
                                               'uzb  | 8526299          | 6.26                               | 169.4\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> print(stats_for_year(2010).sort('geo').take(np.arange(3, 50, 5)))\n"
                                               'geo  | population_total | children_per_woman_total_fertility | child_mortality_under_5_per_1000_born\n'
                                               'bgd  | 147575433        | 2.28                               | 49.1\n'
                                               'col  | 45222699         | 2.01                               | 18.47\n'
                                               'eth  | 87639962         | 4.92                               | 82.94\n'
                                               'ind  | 1234281163       | 2.6                                | 58.23\n'
                                               'ken  | 42030684         | 4.37                               | 56.54\n'
                                               'moz  | 23531567         | 5.56                               | 104.53\n'
                                               'per  | 29027680         | 2.55                               | 20.13\n'
                                               'sdn  | 34545014         | 4.88                               | 75.92\n'
                                               'ukr  | 45792086         | 1.45                               | 11.72\n'
                                               'yem  | 23154854         | 4.67                               | 55.96\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
