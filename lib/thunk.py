

class Thunk():
    def __init__(self, runnable):
        self.runnable = runnable
        self.inputs = {}

    def run(self, callback):
        values = {}
        num_values = len(self.inputs)
        if num_values == 0:
            callback(self.runnable(values))
            return
        def get_callback(key):
            def add_to_values(output_value):
                values[key] = output_value
                if len(values) == num_values:
                    o = self.runnable(values)
                    if callback is not None:
                        callback(o)
            return add_to_values

        for k,v in self.inputs.iteritems():
            v.run(callback=get_callback(k))

    def addInput(self, key, value):
        self.inputs[key] = value


id = lambda: Thunk(lambda x: x)
const = lambda x: Thunk(lambda y: x)
add = lambda: Thunk(lambda d: sum(d.values()))


