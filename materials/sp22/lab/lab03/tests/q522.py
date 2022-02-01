test = {   'name': 'q522',
    'points': None,
    'suites': [   {   'cases': [   {   'code': ">>> # It looks like you're not making an array.  You shouldn't need to\n"
                                               '>>> # use .item anywhere in your solution.\n'
                                               '>>> import numpy as np\n'
                                               '>>> type(more_total_charges) == np.ndarray\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> # You made an array, but it doesn't have the right numbers in it.\n"
                                               '>>> import numpy as np\n'
                                               '>>> sum(abs(more_total_charges - 1.2 * more_restaurant_bills)) < 1e-6\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
