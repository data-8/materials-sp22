test = {   'name': 'q2_4',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> \n'
                                               '>>> import hashlib # This imports a hashing library for the autograder.\n'
                                               '>>> def get_hash(num):\n'
                                               '...     """Helper function for assessing correctness."""\n'
                                               '...     return hashlib.md5(str(num).encode()).hexdigest()\n'
                                               '>>> \n'
                                               '>>> get_hash(set(np.array(q2_4).astype(int))) \n'
                                               "'3649655f87d3a44afa82f25eced24944'",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
