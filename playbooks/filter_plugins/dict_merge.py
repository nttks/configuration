from copy import deepcopy


def dict_merge(a, b):
    if not isinstance(b, dict):
        return b if b != 'None' else None
    result = deepcopy(a)
    for k, v in b.iteritems():
        if k in result and isinstance(result[k], dict):
            data = dict_merge(result[k], v)
            if data is None:
                del result[k]
            else:
                 result[k] = data
        else:
            result[k] = deepcopy(v)
    return result


class FilterModule( object ):
    def filters( self ):
        return { 'dict_merge' : dict_merge }
