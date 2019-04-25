import json

def process (result):
    return list (map (lambda r: [r[0].isoformat(), r[1]], result))[1:]