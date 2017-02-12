models = function(patterns, _) {
    /// Inport aliases
    var Class = patterns.Class;
    var defaults = _.defaults;

    /// Input class
    var InputLink = new Class({
        cons: function(name, data, output) {
            this.name = name;
            this.data = data;
            this.output = output || null;
        },
        methods: {
            run: function() {
                return this.output.run();
            },
            join: function(output) {
                this.output = output
                output.input = this
            }
        }
    });

    /// Output class
    var OutputLink = new Class({
        cons: function(name, data, input) {
            this.name = name;
            this.data = data;
            this.input = input || null;
        },
        methods: {
            run: function() {
                return this.data.run()[this.name];
            },
            join: function(input) {
                this.input = input;
                input.output = this;
            }
        }
    })

    /// Node class
    var ComputationNode = new Class({
        cons: function(data) {
            this.data = data;
            this.inputs = {};
            this.outputs = {};
        },
        methods: {
            getInput: function(name) {
                if (!(name in this.inputs)) {
                    this.inputs[name] = new InputLink(name, this, null);
                }
                return this.inputs[name];
            },
            getOutput: function(name) {
                if (name in this.outputs) {
                    this.outputs[name] = new OutputLink(name, this, null);
                }
                return this.outputs[name];
            },
            run: function() {
                return this.data(this.inputs);
            }
        },
        classProperties: ComputationNode => ({
            add: function() {
                return new ComputationNode(function(inputs) {
                    return {
                        output: inputs.a.run() + inputs.b.run()
                    }
                });
            },
            constant: function(x) {
                return new ComputationNode(function(inputs) {
                    return {
                        output: x
                    }
                })
            },
            identity: function() {
                return new ComputationNode(function(inputs) {
                    return _.mapObject(inputs, function(val, key) { return val.run() })
                })
            }
        })
    });

    // Size class
    var Size = new Class({
        cons: function Size(width, height) {
            this.width = width
            this.height = height || width
        },
        methods: {
            add: function(other) {
                var x, y;
                if (_.has(other, 'x')) {
                    x = other.x;
                    y = other.y;
                } else if (_.has(other, 'width')) {
                    x = other.width;
                    y = other.height;
                } else {
                    throw new Error("add cannot be applied to " + this + " and " + other)
                }
                return new Size(this.width + x, this.height + y);
            },
            timesScalar: function(num) {
                return new Size(this.width * num, this.height * num);
            }
        },
        classProperties: Size => ({
            zero: new Size(0,0)
        })
    });

    // Point class
    var Point = new Class({
        cons: function(x,y) {
            this.x = x
            this.y = y
        },
        methods: {
           add: function(other) {
                var x, y;
                if (_.has(other, 'x')) {
                    x = other.x;
                    y = other.y;
                } else if (_.has(other, 'width')) {
                    x = other.width;
                    y = other.height;
                } else {
                    throw new Error("add cannot be applied to " + this + " and " + other)
                }
                return new Point(this.x + x, this.y + y);
            },
            sub: function(other) {
                var x, y;
                if (_.has(other, 'x')) {
                    x = other.x;
                    y = other.y;
                } else if (_.has(other, 'width')) {
                    x = other.width;
                    y = other.height;
                } else {
                    throw new Error("add cannot be applied to " + this + " and " + other)
                }
                return new Point(this.x - x, this.y - y);
            },
            timesScalar: function(num) {
                return new Point(this.x * num, this.y * num);
            }
        },
        classProperties: Point => ({
            zero: new Point(0,0)
        })
    });

    // Color class
    var Color = new Class({
        cons: function(r,g,b) {
            function truncate(x) {
                if (x > 255) {
                    return 255;
                } else if (x < 0) {
                    return 0;
                } else {
                    return x;
                }
            }
            this.r = truncate(r)
            this.g = truncate(g)
            this.b = truncate(b)
        },
        methods: {
            darken: function(percent) {
                percent = percent || 10;
                percent /= 100.0;
                var scale = 1 - percent;
                return new Color(this.r * scale, this.g * scale, this.b * scale);
            },
            lighten: function(percent) {
                percent = percent || 10;
                percent /= 100.0;
                var scale = 1 + percent;
                return new Color(this.r * scale, this.g * scale, this.b * scale);
            },
            hex: function() {
                var r = this.r.toString(16);
                var g = this.g.toString(16);
                var b = this.b.toString(16);
                return "#" + r + g + b;
            },
            fill: function(processing) {
                processing.fill(this.r, this.b, this.g)
            },
            stroke: function(processing) {
                processing.stroke(this.r, this.b, this.g)
            }
        },
        classProperties: Color => ({
            red: new Color(255,  0,  0),
            yellow: new Color(255,255,  0),
            green: new Color(  0,255,  0),
            cyan: new Color(  0,255,255),
            blue: new Color(  0,  0,255),
            magenta: new Color(255,  0,255),
            white: new Color(255,255,255),
            black: new Color(  0,  0,  0),
            lightGray: new Color(170,170,170),
            darkGray: new Color( 85, 85, 85)
        })
    });
    return {
        InputLink: InputLink,
        OutputLink: OutputLink,
        Size: Size,
        Point: Point,
        Color: Color,
        ComputationNode: ComputationNode
    }
}(patterns, _);