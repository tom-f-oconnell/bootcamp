

def concat_strings(a, b, **kwargs):
    """ Concatenate strings """
    seq = a + b
    for key in kwargs:
        seq += kwargs[key]
    return seq
