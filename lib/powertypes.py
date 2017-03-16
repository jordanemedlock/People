
"""
Symbol class which should replicate/encapsulation the string type

So at the moment this only contains a string and checks equality
normally, so theres nothing added by this class, but I would like to 
have this represent a "fuzzy" string, where you can have many representations
and it can encorporate typos and yada yada yada. I want to make it fancy.
"""
def Symbol(str):
    """
    Initializes a Symbol with the string that it represents
    """
    def __init__(self, *args, **kwargs):
        str.__init__(self, *args, **kwargs)

    def __repr__(self):
        return 'Symbol('+repr(self.value)+')'

"""
PowerDict class which gives the class the same attributes as its keys

it also will get or set the items of any contained values
it basically flattens itself
"""
class PowerDict(dict):
    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)

    def __getitem__(self, key):
        if dict.__contains__(self, key):
            return dict.__getitem__(self, key)
        else:
            for k, v in self.items():
                if isinstance(v, dict) and key in v:
                    return v[key]
            return None

    def __setitem__(self, key, value):
        set_value = False
        if dict.__contains__(self, key):
            dict.__setitem__(self, key, value)
            set_value = True
        else:
            for k, v in self.items():
                if isinstance(v, dict) and key in v:
                    v[key] = value
                    set_value = True
        if not set_value:
            dict.__setitem__(self, key, value)

