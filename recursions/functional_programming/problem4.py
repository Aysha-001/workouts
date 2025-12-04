def treemap(map_f, arr ):
    
    result = []

    for item in arr:
        if isinstance(item, list):
            result.append(treemap(map_f, item))
        else:
            result.append(map_f(item))


    return result
print(treemap(lambda x: x*x, [1, 2, [3, 4, [5]]]))