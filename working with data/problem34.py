def read_words(filename):
    return open(filename).read().split()

def word_frequency(words):
    """Returns frequency of each word given a list of words.

        >>> word_frequency(['a', 'b', 'a'])
        {'a': 2, 'b': 1}
    """
    frequency = {}
    for w in words:
        frequency[w] = frequency.get(w, 0) + 1
    return frequency

def decendin_order(frequency):
    sorted_items = sorted(frequency.items(), key=lambda item:min(item[1]))
    return sorted_items


def main(filename):
    frequency = word_frequency(read_words(filename))
    result = decendin_order(frequency)

    for key , value in result.items():
        print(key, value)

if __name__ == "__main__":
    import sys
    main(sys.argv[2])