test = {   'name': 'q32',
    'points': None,
    'suites': [   {   'cases': [   {   'code': ">>> # You either didn't add the 'Total Pay ($)' column, \n>>> # or you mislabeled it\n>>> 'Total Pay ($)' in compensation.column_labels\nTrue",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # You have the column in your table, but the values may be wrong\n'
                                               ">>> t = compensation.sort('Total Pay ($)', descending = True)\n"
                                               ">>> np.isclose(t.column('Total Pay ($)').item(0), 53250000.0)\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
