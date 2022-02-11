test = {   'name': 'q2_3',
    'points': [0, 0, 2],
    'suites': [   {   'cases': [   {   'code': '>>> # Double check that your salary_range function is correct\n>>> compensation_range(make_array(5, 1, 20, 1000)) == 999\nTrue',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Make sure that the table has departments as the rows and organization groups as the columns.\n'
                                               '>>> set(["Department", "Community Health", "Culture & Recreation", "General Administration & Finance", "Human Welfare & Neighborhood Development", '
                                               '"Public Protection", "Public Works, Transportation & Commerce"]) == set(department_ranges.labels)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> sum(department_ranges.column(1))\n554179.0', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
