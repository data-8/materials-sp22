test = {   'name': 'q2_9',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> len(differences)\n0', 'hidden': False, 'locked': False},
                                   {   'code': '>>> abs(np.average(differences)) < 0.05 # On average, your test statistic should be close to 0\n'
                                               '/opt/conda/lib/python3.9/site-packages/numpy/lib/function_base.py:495: RuntimeWarning: Mean of empty slice.\n'
                                               '  avg = a.mean(axis)\n'
                                               '/opt/conda/lib/python3.9/site-packages/numpy/core/_methods.py:189: RuntimeWarning: invalid value encountered in double_scalars\n'
                                               '  ret = ret.dtype.type(ret / rcount)\n'
                                               'False',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> all(differences == differences.item(0)) == False # Make sure all of the test statistics are different\n', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
