test = {   'name': 'q1_5',
    'points': [0, 0, 0],
    'suites': [   {   'cases': [   {   'code': ">>> # Check your column labels and spelling\n>>> fertility_over_time('usa', 2010).labels == ('Year', 'Children per woman')\nTrue",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Check that you use the start year to determine the data range.\n'
                                               ">>> all(fertility_over_time('usa', 2010).column('Year') == np.arange(2010, 2021))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Check that you use the start year to determine the data range.\n'
                                               ">>> all(fertility_over_time('usa', 2005).column('Year') == np.arange(2005, 2021))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
