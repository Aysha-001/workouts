def unflatten_dict(a):
    result = {}
    for key, value in a.items():
        splits = key.split('.')
        if len(splits) > 1:
            parent, child = splits[-2], splits[-1]
            if parent not in result:
                result[parent] = {}
            result[parent][child] = value
        else:
            result[key] = value
    return result
print(unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}))

