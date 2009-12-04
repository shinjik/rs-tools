import json

def to_j(o):
    s = None
    j = json.JSONEncoder(o)
    try:
        s = j.encode(o)
    except Exception, e:
        raise e
    finally:
        return s

def from_j(s):
    o = None
    j = json.JSONDecoder()
    try:
        o = j.decode(s)
    except Exception, e:
        raise e
    finally:
        return o

