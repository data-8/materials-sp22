test = {   'name': 'q2_5',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> \n'
                                               '>>> import hashlib # This imports a hashing library for the autograder.\n'
                                               '>>> def get_hash(num):\n'
                                               '...     """Helper function for assessing correctness."""\n'
                                               '...     return hashlib.md5(str(num).encode()).hexdigest()\n'
                                               '>>> \n'
                                               '>>> get_hash(set(np.array(q2_5).astype(int)))\n'
                                               "'b793dd27381f7b63cada88b749c0e023'",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
