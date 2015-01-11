def dict_findall(d, k, path=[]):
    ''' Return all key paths that contain key `k`

    >>> list(dict_findall({'a': {'a': {'b': 1}, 'b': 2}, 'b': {'b': 4}}, 'b'))
    [['a', 'a'], ['a'], [], ['b']]
    '''
    for _k,v in d.iteritems():
        if _k == k:
            yield list(path)
        if isinstance(v, dict):
            for p in dict_findall(v, k, path+[_k]):
                yield p
