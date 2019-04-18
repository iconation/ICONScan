import json

def txcount (result):
    return list (map (lambda r: [r[0].isoformat(), r[1]], result))[1:]