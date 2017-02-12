testing = true;

var defaults = _.defaults


function assertEqual(x, y) {
    var val = _.isEqual(x, y)
    if (val) {
        return true;
    } else {
        console.log(JSON.stringify(x) + " should be equal to " + JSON.stringify(y))
        return false;
    }
}

function TestDefaults(){
    this.testFunctionality = function() {
        var input = {
            a: null,
            b: 10,
            c: "string"
        }

        var defs = {
            a: 10,
            b: 20,
            d: "new",
            e: null
        }

        var expectedOutput = {
            a: null,
            b: 10,
            c: "string",
            d: "new",
            e: null
        }

        var output = defaults(input, defs);
        return assertEqual(output, expectedOutput)
    }

    this.testCopy = function() {
        var input = {
            a: 10
        }

        var defs = {
            b: 20
        }

        var output = defaults(input, defs)
        output.a = 20
        output.b = 10
        return input.a == 10 && defs.b == 20
    }
}

mixin = patterns.mixin
function TestMixin() {
    this.testFunctionality = function() {
        var child = {
            a: 10,
            b: 20
        }
        var parent = {
            b: 30,
            c: 40
        }
        var expectedOutput = {
            a: 10,
            b: 20,
            c: 40
        }
        mixin(child, parent)
        return assertEqual(expectedOutput, child)
    }
}

Class = patterns.Class
function TestClass() {
    this.testAll = function() {
        var A = new Class({
            cons: function() {
                this.a = "a"
            },
            methods: {
                b: function() {
                    return 'b';
                }
            }
        })

        var B = new Class({
            parentClass: A,
            cons: function() {
                A.call(this)
                this.c = 'c'
            },
            methods: {
                d: function() {
                    return this.b();
                }
            }
        })

        var C = new Class({
            parentClass: B,
            cons: function() {
                B.call(this)
                this.e = 'e'
            },
            methods: {
                b: function() {
                    return 'b2';
                },
                d: function() {
                    return 'd';
                },
                f: function() {
                    return this._super.b();
                }
            }
        })

        var a = new A();
        var b = new B();
        var c = new C();

        console.log(a.a == 'a' && a.b() == 'b')
        console.log(b.a == 'a' && b.b() == 'b')
        console.log(b.c == 'c' && b.d() == 'b')
        console.log(c.a == 'a' && c.b() == 'b2')
        console.log(c.c == 'c' && c.d() == 'd')
        console.log(c.e == 'e' && c.f() == 'b')

        return a.a == 'a' && a.b() == 'b' &&
               b.a == 'a' && b.b() == 'b' &&
               b.c == 'c' && b.d() == 'b' &&
               c.a == 'a' && c.b() == 'b2' &&
               c.c == 'c' && c.d() == 'd' &&
               c.e == 'e' && c.d() == 'b';
    }
}

var test = function() {
    _.each(arguments, function(arg) {
        console.log("Testing: " + arg.name);
        var x = new arg();
        _.each(x, function(func, name) {
            var passed = func.call(x)
            console.log("*** " + name + (passed ? " passed" : " failed"))
        }, x)
    })
}

test(TestDefaults, TestMixin, TestClass);