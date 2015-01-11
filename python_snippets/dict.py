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

def fark(d, key, search, replace):
    '''
    look for keys in ``d`` that match ``key`` recursively
    replace ``search`` with ``replace`` for that value

    NOTE: mutates original dict `d`, returns None

    >>> d = {'a': {'file': '/usr/local/module/a.txt', 'b': {'file': '/usr/local/module/b.txt'}}}
    >>> fark(d, 'file', '/usr', '/home/hatem')
    >>> d == {'a': {'file': '/home/hatem/local/module/a.txt', 'b': {'file': '/home/hatem/local/module/b.txt'}}}
    True
    '''
    for k,v in d.items():
        if isinstance(v, dict):
            fark(v, key, search, replace)
        else:
            if k == key:
                d[k] = v.replace(search, replace)
