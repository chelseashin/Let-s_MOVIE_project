__all__ = ['example']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['javascriptCode'])
@Js
def PyJsHoisted_javascriptCode_(data, user, this, arguments, var=var):
    var = Scope({'data':data, 'user':user, 'this':this, 'arguments':arguments}, var)
    var.registers(['data', 'user', 'train', 'test', 'cf', 'movie', 'i', 'gt'])
    var.put('movie', var.get('data'))
    var.get('console').callprop('log', var.get('data'))
    var.put('train', Js([]))
    var.put('test', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('movie').get('length')):
        try:
            if (var.get('Math').callprop('random')>Js(0.8)):
                var.get('test').callprop('push', var.get('movie').get(var.get('i')))
            else:
                var.get('train').callprop('push', var.get('movie').get(var.get('i')))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    var.put('cf', var.get('CF').create())
    var.get('cf').put('maxRelatedItem', Js(10.0))
    var.get('cf').put('maxRelatedUser', Js(10.0))
    var.get('cf').callprop('train', var.get('train'), Js('user_id'), Js('movie_id'), Js('rating'))
    var.put('gt', var.get('cf').callprop('gt', var.get('test'), Js('user_id'), Js('movie_id'), Js('rating')))
    return var.get('cf').callprop('recommendToUser', var.get('user'), Js(10.0))
PyJsHoisted_javascriptCode_.func_name = 'javascriptCode'
var.put('javascriptCode', PyJsHoisted_javascriptCode_)
pass
pass


# Add lib to the module scope
example = var.to_python()