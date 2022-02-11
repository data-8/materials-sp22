test = {   'name': 'q2_4',
    'points': [0, 0],
    'suites': [   {   'cases': [   {   'code': ">>> # Check your column labels and spelling\n>>> poverty_map.labels == ('latitude', 'longitude', 'name', 'region', 'poverty_total')\nTrue",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Something is wrong with your region column.\n'
                                               ">>> list(np.sort(np.unique(poverty_map.column('region'))))\n"
                                               "['africa', 'americas', 'asia', 'europe']",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
