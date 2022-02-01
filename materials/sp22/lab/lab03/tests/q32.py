test = {   'name': 'q32',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> type(imdb) == tables.Table\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> imdb.num_rows == 250\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> imdb.select('Votes', 'Rating', 'Title', 'Year', 'Decade').sort(0).take(range(2,5))\n"
                                               'Votes | Rating | Title                       | Year | Decade\n'
                                               '31003 | 8.1    | Le salaire de la peur       | 1953 | 1950\n'
                                               '32385 | 8      | La battaglia di Algeri      | 1966 | 1960\n'
                                               '35983 | 8.1    | The Best Years of Our Lives | 1946 | 1940',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
