test = {   'name': 'q2_0_1',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> 0 < probability_large_shiny < 1 \nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> \n'
                                               '>>> import hashlib \n'
                                               '>>> def get_hash(num):\n'
                                               '...     """Helper function for assessing correctness."""\n'
                                               '...     return hashlib.md5(str(num).encode()).hexdigest()\n'
                                               '>>> \n'
                                               '>>> get_hash(np.round(probability_large_shiny, 3))\n'
                                               "'8404599d79837400f000c64a4fa1cc0e'",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
