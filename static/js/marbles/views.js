views = function(models, patterns, _) {
    var Point = models.Point
    var Size = models.Size
    var Color = models.Color
    var required = patterns.required
    var Class = patterns.Class
    var defaults = _.defaults


    /// View class
    /// Superclass of all Views that can be displayed
    var View = new Class({
        cons: function (options) {
            var opt = defaults(options, {
                size: Size.zero,
                pos: Point.zero,
                fillColor: Color.lightGray,
                borderColor: Color.lightGray,
                borderWidth: 1
            })
            this.size = opt.size;
            this.pos = opt.pos;
            this.fillColor = opt.fillColor;
            this.borderColor = opt.borderColor;
            this.borderWidth = opt.borderWidth;

            this.subviews = [];
            this.parentView = null;
        },
        methods: {
            drawAll: function(processing) {
                if (this.draw) {
                    this.draw(processing);
                }
                this.drawSubviews(processing);
            },
            setupColors: function(processing) {
                this.fillColor.fill(processing);
                this.borderColor.stroke(processing);
                processing.strokeWeight(this.borderWidth);
            },
            draw: function(processing) {
                this.setupColors(processing);
                drawRectangle(this.globalPos(), this.size, processing);
            },
            pointIsIn: function(point) {
                var pos = this.globalPos();
                return point.x >= pos.x &&
                       point.x <= pos.x + this.size.width &&
                       point.y >= pos.y &&
                       point.y <= pos.y + this.size.height;
            },
            addSubviews: function() {
                _.each(arguments, function(view) {
                    view.parentView = this;
                    this.subviews.push(view)
                }, this)
            },
            drawSubviews: function(processing) {
                _.each(this.subviews, function(view) {
                    view.drawAll(processing);
                }, this);
            },
            globalPos: function() {
                if (this.parentView) {
                    var parentPos = this.parentView.globalPos();
                    return parentPos.add(this.pos);
                } else {
                    return this.pos
                }
            },
            getView: function(point) {
                if (this.pointIsIn(point)) {
                    var view = _.find(this.subviews, function(view) {
                        return view.getView(point)
                    }, this);
                    return view || this;
                } else {
                    return null;
                }
            }
        },
    });

    var drawEllipse = function(pos, size, processing) {
        processing.ellipse(pos.x, pos.y, size.width, size.height)
    }

    var drawRectangle = function(pos, size, processing) {
        processing.rect(pos.x, pos.y, size.width, size.height)
    }

    var drawText = function(text, pos, processing) {
        processing.text(text, pos.x, pos.y)
    }

    var EllipseView = new Class({
        parentClass: View,
        cons: function(options) {
            View.call(this, options)
        },
        methods: {
            draw: function(processing) {
                this.setupColors(processing);
                drawEllipse(this.globalPos(), this.size, processing);
            },
            // we assume point is in global space
            pointIsIn: function(point) {
                var d = point.sub(this.globalPos());
                var w = this.size.width;
                var h = this.size.height;
                return (d.x*d.x)/(w*w) + (d.y*d.y)/(h*h) <= 1
            }
        }
    })

    var OutputView = new Class({
        parentClass: EllipseView,
        cons: function(options) {
            var opt = defaults(options, {
                fillColor: Color.lightGray,
                borderColor: Color.black,
                size: new Size(5,5)
            })
            EllipseView.call(this, opt)

            this.link = null
        }
    })

    var InputView = new Class({
        parentClass: EllipseView,
        cons: function(options) {
            var opt = defaults(options, {
                fillColor: Color.darkGray,
                borderColor: Color.black,
                size: new Size(5,5)
            })
            EllipseView.call(this, opt)

            this.link = null;
        }
    })

    var NodeView = new Class({
        parentClass: View,
        cons: function(options) {
            var opt = defaults(options, {
                size: new Size(110,30),
                borderColor: Color.black,
                shape: drawRectangle
            })
            View.call(this, opt);

            this.name = required(opt, 'name');
            this.node = required(opt, 'node');
            this.inputs = required(opt, 'inputs');
            this.outputs = required(opt, 'outputs');
            this.shape = opt.shape;
            this.inputViews = {};
            this.outputViews = {};
            this.setup();
        },
        methods: {
            draw: function(processing) {
                node = this;
                this.setupColors(processing);
                this.shape(this.globalPos(), this.size, processing);

                Color.black.fill(processing);
                drawText(this.name, this.globalPos().add(new Point(10,20)), processing);
            },
            setup: function() {
                var x = this.size.width - 20;
                var y = this.size.height / 2;

                _.each(this.outputs, function(output) {
                    var outputView = new OutputView({
                        pos: new Point(x, y)
                    });
                    outputView.link = this.node.getOutput(output);
                    this.outputViews[output] = outputView;
                    this.addSubviews(outputView);
                    x -= 20;
                }, this);

                _.each(this.inputs, function(input) {
                    var inputView = new InputView({
                        pos: new Point(x, y)
                    });
                    inputView.link = this.node.getInput(input);
                    this.inputViews[input] = inputView;
                    this.addSubviews(inputView);
                    x -= 20;
                }, this);
            }
        }
    })

    var StringView = new Class({
        parentClass: View,
        cons: function(options) {
            var opt = defaults(options, {
                fillColor: Color.black
            })
            View.call(this, opt);
            this.text = required(options, 'text')
        },
        methods: {
            draw: function(processing) {
                this.setupColors(processing)
                drawText(this.text, this.globalPos(), processing)
            }
        }
    })

    return {
        View: View,
        drawEllipse: drawEllipse,
        drawRectangle: drawRectangle,
        drawText: drawText,
        InputView: InputView,
        OutputView: OutputView,
        NodeView: NodeView,
        StringView: StringView
    }
}(models, patterns, _);