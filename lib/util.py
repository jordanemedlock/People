from json import JSONEncoder, dump, dumps, load, loads

class CustomEncoder(JSONEncoder):
    def default(self, obj):
        if hasattr(obj, '__json__'):
            return obj.__json__()
        else:
            return JSONEncoder.default(self, obj)


def json_dump(obj, filepath):
    return dump(obj, open(filepath, 'w'), cls=CustomEncoder)

def json_dumps(obj):
    return dumps(obj, cls=CustomEncoder)

def json_load(filepath, cls=None):
    print(filepath)
    if hasattr(cls, 'from_json'):
        return cls.from_json(load(open(filepath, 'r')))
    else:
        return load(open(filepath, 'r'))

def json_loads(string, cls=None):
    if hasattr(cls, 'from_json'):
        return cls.from_json(loads(string))
    else:
        return loads(string)




