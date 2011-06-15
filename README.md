node.js.py
==========

This module acts as a bridge to node.js and npm.

`Node(dependencies, version, path, npm_version, daemonic)` will start a process (all parameters optional). It will locally install and compile node.js and dependencies using [nodeenv](https://github.com/ekalinin/nodeenv).

The processes communicate over HTTP using [JSON-RPC 1.0](http://json-rpc.org/wiki/specification). A `Node` instance acts as a bridge to the node process's global namespace.

    node = Node(["coffee-script==1.0.1"], "0.4.8")
    
    assert 2 == node.eval("2")

    coffee = node.require("coffee")

    double = coffee.eval("return (x) -> x * 2")

    assert double(2) == 4
    
    print coffee.compile("(x) -> x * 2")
    # prints "(function(x) {\n  return x * 2;\n});"""

The bridge maps `Object`s to `NodeProxyObject`s and Functions to `NodeProxyFunction`s. Booleans and strings map to the corresponding types, numbers map to floats, and `null` and `undefined` map to `None`.

`NodeProxyObject`s implement `__copy__` and `__deepcopy__` to create local copies of the remote objects.

Python callables can be passed to node.js, but they will execute asynchronously and return nothing. Define a parameter with a default value of `nodejs.THIS` to receive JavaScript's `this` value.

In node.js a `python` object will be defined, with the async methods `exec` and `eval`.

Python 2.6+ will be supported, but I won't be testing on Python 3 yet.
