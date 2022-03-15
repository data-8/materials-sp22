test = {   'name': 'q2_9',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> len(differences)\n5000', 'hidden': False, 'locked': False},
                                   {'code': '>>> abs(np.average(differences)) < 0.05 # On average, your test statistic should be close to 0\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> all(differences == differences.item(0)) == False # Make sure all of the test statistics are different\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
