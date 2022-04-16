test = {   'name': 'q3_2_2',
    'points': [3],
    'suites': [   {   'cases': [   {   'code': '>>> from collections import Counter\n'
                                               ">>> g = train_movies.column('Genre')\n"
                                               '>>> r = np.where(test_movies[\'Title\'] == "godzilla")[0][0]\n'
                                               '>>> t = test_my_features.row(r)\n'
                                               '>>> godzilla_expected_genre = Counter(np.take(g, np.argsort(fast_distances(t, train_my_features))[:15])).most_common(1)[0][0]\n'
                                               '>>> godzilla_genre == godzilla_expected_genre\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
