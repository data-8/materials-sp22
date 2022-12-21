test = {   'name': 'q35',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> type(farmers_markets_locations_by_latitude) == tables.Table\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> # HINT: Check the order of your table. \n'
                                               ">>> list(np.round(list(farmers_markets_locations_by_latitude.column('y').take(range(3))),6)) == [64.86275, 64.8459, 64.844414]\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
