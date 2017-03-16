


class CustomValue(object):
    @property
    def value(self):
        pass

    @value.setter
    def value(self, value):
        pass

class SingleValue(CustomValue):
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class FunctionValue(CustomValue):
    def __init__(self, fget, fset=None, obj=None):
        def default_set(a=None, b=None):
            raise Exception('property cannot be set')
        self.fget = fget
        self.fset = fset or default_set
        self.obj = obj


    @property
    def value(self):
        if self.obj is None:
            return self.fget()
        else:
            return self.fget(self.obj)

    @value.setter
    def value(self, value):
        if self.obj is None:
            self.fset(value)
        else:
            self.fset(self.obj, value)



