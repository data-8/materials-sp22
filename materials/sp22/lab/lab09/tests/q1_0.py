test = {   'name': 'q1_0',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> len(least_squares_order) == 4\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> \n'
                                               '>>> import hashlib # This imports a hashing library for the autograder.\n'
                                               '>>> def get_hash(num):\n'
                                               '...     """Helper function for assessing correctness."""\n'
                                               '...     return hashlib.md5(str(num).encode()).hexdigest()\n'
                                               '>>> \n'
                                               '>>> get_hash(np.array(least_squares_order).astype(int)) # Your ordering is incorrect.\n'
                                               "'cd29f2d730e11535cef30ecc78640daa'",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
