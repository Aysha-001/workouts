def flatten_dict( a, result=None, parent=""):
    """.

        flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
{'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}
    """
    if result is None:
        result = {}
    

    for key, value in a.items():
        if isinstance(value, dict):
            flatten_dict(value, result, parent + key + ".")
        else:
            new_key = f"{parent}{key}"
            result[new_key] = value

    return result
print(flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}))
print(flatten_dict( {'a':{'b':{'c':{'d':5}}}}  ))