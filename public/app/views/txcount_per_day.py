import json

def txcount (result):
    # return {
        # "dates" : list (map (lambda r: r[0].isoformat(), result))[1:],
        # "counts" : list (map (lambda r: r[1], result))[1:]
    # }
    return list (map (lambda r: [r[0].isoformat(), r[1]], result))[1:]