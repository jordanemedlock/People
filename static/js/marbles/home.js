patterns.mixin(window, models);
patterns.mixin(window, views);

log = new StringView({text: "log", pos: new Point(500,500)})



var getNodeProc = function(view) {

    return function(processing) {
        processing.ellipseMode(processing.RADIUS)
        var initialPoint = null;
        var finalPoint = null;
        processing.setup = function() {
            processing.size(view.size.width,view.size.height);
        }
        processing.draw = function() {
            view.drawAll(processing);
            if (processing.__mousePressed && (processing.mouseButton == processing.LEFT)) {
                if (_.isNull(initialPoint)) {
                    initialPoint = new Point(processing.mouseX, processing.mouseY);
                    finalPoint = new Point(processing.mouseX, processing.mouseY);
                    var initView = view.getView(initialPoint);
                    console.log('initView', initView);
                } else {
                    finalPoint = new Point(processing.mouseX, processing.mouseY);
                }
                Color.black.stroke(processing)
                processing.line(initialPoint.x, initialPoint.y, finalPoint.x, finalPoint.y)
                console.log('pressed: ', initialPoint, finalPoint)

            } else {
                initialPoint = null;
                finalPoint = null;
            }
        }
    }
}

$(function() {

    var canvas = document.getElementById("canvas1");

    var a = ComputationNode.constant(10);
    var aView = new NodeView({
        name: "10",
        node: a,
        inputs: [],
        outputs: ["output"],
        pos: new Point(10, 10),
        fillColor: Color.yellow
    });
    var b = ComputationNode.constant(20);
    var bView = new NodeView({
        name: "20",
        node: b,
        inputs: [],
        outputs: ["output"],
        pos: new Point(10, 60),
        fillColor: Color.magenta
    });
    var addf = ComputationNode.add();
    var addView = new NodeView({
        name: "add",
        node: addf,
        inputs: ['a','b'],
        outputs: ["output"],
        pos: new Point(10, 110),
        fillColor: Color.cyan
    });

    var canvas = document.getElementById("canvas1");

    var view = new View({
        pos: Point.zero,
        size: new Size(1800, 800),
        fillColor: Color.lightGray,
        borderColor: Color.lightGray
    })
    view.addSubviews(aView, bView, addView);

    var nodeProc = getNodeProc(view);

    var processingInstance = new Processing(canvas, nodeProc);

})
