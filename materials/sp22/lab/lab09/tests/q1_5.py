test = {   'name': 'q1_5',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> \n'
                                               '>>> import hashlib # This imports a hashing library for the autograder.\n'
                                               '>>> def get_hash(num):\n'
                                               '...     """Helper function for assessing correctness."""\n'
                                               '...     return hashlib.md5(str(num).encode()).hexdigest()\n'
                                               '>>> \n'
                                               '>>> get_hash(int(correlation)) # Your choice is incorrect.\n'
                                               "'eccbc87e4b5ce2fe28308fd9f2a7baf3'",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
