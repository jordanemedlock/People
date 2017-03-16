
(function ($) {
    $.fn.spiderplot = function(options) {
        var settings = $.extend({
            keys: [],
            values: [],
            changedCallback: function(k,v) {}
        }, $.fn.spiderplot.defaults, options)

        return this.each(function() {
            $(this).css('background-color', settings.backgroundColor)
            $(this).svg({onLoad: mkRenderer(settings)})
        })
    }

    // function which returns the start and end of every radial line
    // in the circle
    function getLines(names, innerRadius, outterRadius){
        // find delta theta
        var dth = Math.PI * 2 / names.length;

        // initialize the list
        var vals = []
        _.each(names, function(name, i) {
            // start point
            var ix = innerRadius * Math.cos(dth * i)
            var iy = innerRadius * Math.sin(dth * i)

            // end point
            var ox = outterRadius * Math.cos(dth * i)
            var oy = outterRadius * Math.sin(dth * i)

            // add it to the list
            vals.push({
                name: name,
                start: {
                    x: ix,
                    y: iy
                },
                end: {
                    x: ox,
                    y: oy
                }
            })
        });
        return vals;
    }

    function drawConcentricCircles(svg, root, n, innerRadius, outterRadius) {
        // draw the radial circles in the middle
        // n-1 because I want the last circle to show up
        var deltaR = (outterRadius-innerRadius) / (n-1);
        _.times(n, function(i) {
            svg.circle(root, 0, 0, innerRadius + deltaR * i, {
                fillOpacity: 0.0,
                stroke: '#3a4045',
                strokeWidth: 1
            })
        })
    }

    function lerp(start, end, scale) {
        let lx = end.x - start.x;
        let ly = end.y - start.y;
        let dx = lx * scale;
        let dy = ly * scale;
        return {
            x: start.x + dx,
            y: start.y + dy
        }
    }

    function getValueLines(lines, values){
        return _.chain(lines)
                .zip(values)
                .map(function(lav) {
                    return {
                        name: lav[0].name,
                        value: lav[1],
                        start: lav[0].start,
                        end: lerp(lav[0].start, lav[0].end, lav[1])
                    };
                })
                .value();
    }

    function setNthPoint(n, point) {
        var d = $('#data-path').attr('d');
        var pointsStrings = d.replace('M','').replace('z','').split('L')

        var start = pointsStrings.slice(0,n)
        var end = pointsStrings.slice(n+1)
        var rep = 'M' + start.join('L') + (start.length ? 'L' : '') + point.x + ',' + point.y + (end.length ? 'L' : '') + end.join('L') + 'z'
        $('#data-path').attr('d', rep);
    }

    function mkRenderer(settings){
        return function(svg) {

            var backdrop = svg.rect(0,0,'100%','100%', {
                fill: settings.backgroundColor
            })

            var pickedup = null;
            $(backdrop).parent().mousedown(function(event) {
            }).mousemove(function(event) {
                if (pickedup) {
                    var offset = $(this).offset();
                    var svgSpace = {
                        x: event.clientX - offset.left,
                        y: event.clientY - offset.top
                    }
                    var rootOffsetStr = $("#root").attr("transform")
                    var xandy = /translate\(([0-9.]+),([0-9.]+)\)/.exec(rootOffsetStr)
                    var rootOffset = {x: xandy[1], y: xandy[2]}
                    var rootSpace = {
                        x: svgSpace.x - rootOffset.x,
                        y: svgSpace.y - rootOffset.y
                    }
                    var dist = Math.sqrt(rootSpace.x * rootSpace.x + rootSpace.y * rootSpace.y)
                    var lx = $('#' + pickedup + '-background-line').attr('x2')
                    var ly = $('#' + pickedup + '-background-line').attr('y2')
                    var len = Math.sqrt(lx*lx+ly*ly)
                    var scale = dist / len
                    scale = scale > 1 ? 1 : scale
                    var point = lerp({x:0,y:0}, {x:lx,y:ly}, scale)
                    $('#' + pickedup + '-group').find(".data-nub").
                            attr('cx', point.x).
                            attr('cy', point.y)
                    $('#' + pickedup + '-group').find('.data-line').
                            attr('x2', point.x).
                            attr('y2', point.y)
                    let n = settings.names.indexOf(pickedup)
                    setNthPoint(n, point)

                    let newValue = (dist - 15) / (len - 15)
                    newValue = newValue > 1 ? 1 : newValue
                    $('#' + pickedup + '-text tspan').text('[' + newValue.toFixed(2) + ']')
                }
                event.preventDefault();
            }).mouseup(function(event) {
                $('#' + pickedup + '-group').removeClass('pickedup')
                pickedup = null;
            })


            var h = svg.height();
            var w = svg.width();
            var px = 300, py = 80;
            var smallest = Math.min(h - py, w - px); // 80 and 200 are the padding needed in w and h
            var cx = w / 2;
            var cy = h / 2;

            var root = svg.group('root', {transform: 'translate('+cx+','+cy+')'})

            var cr = 15; // center circle radius
            var nr = 5; // nub radius
            var br = smallest / 2.0 // big radius

            // draw concentric circles
            drawConcentricCircles(svg, root, 20, cr, br);

            // get the radial lines
            var lines = getLines(settings.names, cr, br);

            // draw background lines
            _.each(lines, function(line) {
                var s = line.start, e = line.end;
                svg.line(root, s.x, s.y, e.x, e.y, {
                    id: line.name + '-background-line',
                    strokeWidth: 2,
                    stroke: '#3a4045'
                })
            })

            // draw background nubs
            _.each(lines, function(line) {
                svg.circle(root, line.end.x, line.end.y, 5, {
                    strokeWidth: 2,
                    stroke: '#4F4F4F',
                    fill: '#33393f'
                })
            })

            // get value points
            var valueLines = getValueLines(lines, settings.values);

            // draw value web
            var path = svg.createPath().move(valueLines[0].end.x, valueLines[0].end.y);
            _.each(valueLines.slice(1), function(line) {
                path = path.line(line.end.x, line.end.y)
            });
            path = path.close();
            svg.path(root, path, {
                id: 'data-path',
                stroke: settings.foregroundColor,
                strokeWidth: 1,
                strokeOpacity: 0.5,
                fill: settings.foregroundColor,
                fillOpacity: 0.25
            });

            // draw value lines
            _.each(valueLines, function(line) {
                var s = line.start, e = line.end;
                var g = svg.group(root, line.name + "-group", {
                    class_: 'nub-parent'
                })
                // draw value nubs
                svg.circle(g, line.end.x, line.end.y, 5, {
                    id: line.name + '-nub',
                    class_: 'data-nub',
                    fill: settings.foregroundColor
                });
                svg.line(g, s.x, s.y, e.x, e.y, {
                    id: line.name + '-line',
                    strokeWidth: settings.foregroundWidth,
                    stroke: settings.foregroundColor,
                    strokeOpacity: 0.5,
                    class_: 'data-line'
                });

                $(g).mousedown(function(event) {
                    pickedup = line.name;
                    $(this).addClass("pickedup")
                })
            });


            // draw text
            _.each(lines, function(line, i) {
                var value = settings.values[i]
                var valueString = '[' + value.toFixed(2) + ']';

                var dx = line.end.x - line.start.x;
                var dy = line.end.y - line.start.y;
                var z = (x) => -0.01 < x && x < 0.01;

                var originPoint = customSwitch([dx, dy],
                [
                    { cond: (dx,dy) =>  z(dx), value: 'middle' }, // top and bottom
                    { cond: (dx,dy) => dx < 0, value: 'end' },    // left
                    { cond: (dx,dy) =>   true, value: 'start' }   // right
                ]);

                var scale = customSwitch([dx, dy],
                [
                    { cond: (dx,dy) => dy > 0, value: 1.10 },// bottom few
                    { cond: (dx,dy) =>   true, value: 1.05 } // rest
                ]);

                var before = dx < 0 // left

                var text = svg.createText();
                if (before) {
                    text = text.span(valueString, {
                        fill: '#7799aa'
                    }).string(' ' + line.name);
                } else {
                    text = text.string(line.name + ' ').span(valueString, {
                        fill: '#7799aa'
                    });
                }

                var pos = lerp(line.start, line.end, scale);
                svg.text(root, pos.x, pos.y, text, {
                    textAnchor: originPoint,
                    id: line.name + '-text',
                    fill: '#557788'
                });
            })

            // draw the center circle
            svg.circle(root, 0, 0, cr, {
                stroke: settings.selectedColor,
                strokeWidth: settings.foregroundWidth,
                fillOpacity: 0.0
            })
        }
    }

    function customSwitch(values, cases) {
        return _.chain(cases)
            .find((obj) => obj.cond.apply(this, values))
            .value().value;
    }

    $.fn.spiderplot.defaults = {
        numberOfCircles: 20,
        selectedColor: '#7799aa',
        foregroundColor: '#557788',
        foregroundWidth: 2,
        backgroundStroke: '#4F4F4F',
        backgroundWidth: 2,
        backgroundColor: '#33393f'

    }
})(jQuery);
