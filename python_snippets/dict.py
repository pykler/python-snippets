def dict_findall(d, k, path=[]):
    ''' Return all key paths that contain key `k`

    >>> list(dict_findall({'a': {'a': {'b': 1}, 'b': 2}, 'b': {'b': 4}}, 'b'))
    [['a', 'a'], ['a'], [], ['b']]
    >>> list(dict_findall({'a': [{'a': {'b': 1}, 'b': 2}]}, 'b'))
    [['a', 0, 'a'], ['a', 0]]
    '''
    if isinstance(d, dict):
        for _k,v in d.iteritems():
            if _k == k:
                yield list(path)
            for p in dict_findall(v, k, path+[_k]):
                yield p
    elif isinstance(d, list):
        for i,v in enumerate(d):
            for p in dict_findall(v, k, path+[i]):
                yield p

def get_key(d, kl):
    '''
    given a list of keys ``kl``, loop through them to return the value
    can be used to grab one of the keys returned by :func:dict_findall

    >>> get_key({'a': [{'a': {'b': 1}, 'b': 2}]}, ['a', 0, 'a'])
    {'b': 1}
    >>> get_key({'a': [{'a': {'b': 1}, 'b': 2}]}, ['a', 1, 'a'])
    Traceback (most recent call last):
    KeyError: ['a', 1]
    '''
    for i,k in enumerate(kl):
        try:
            d = d[k]
        except (KeyError, IndexError):
            raise KeyError(kl[:i+1])
    return d

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
