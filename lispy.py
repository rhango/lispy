(
    globals().update({'set_': (lambda vars_:
        globals().update(vars_))}),


    set_({'_': (lambda func, *args, **kwargs:
        func(*args, **kwargs))}),


    _(set_, {'del_': (lambda *keys:
        _((lambda g_vars:
            [_(g_vars.pop, key) for key in keys]
        ), **{
            'g_vars': _(globals)
        }))}),


    _(set_, {'import_all': (lambda mod_name:
        _((lambda mod:
            _((lambda vals:
                {key: vals[key] for key in mod.__all__}
            ), **{
                'vals': _(vars, mod)
            })
        ), **{
            'mod': _(__import__, mod_name)
        }))}),


    _(set_, _(import_all, 'operator')),


    _(set_, {'nil': (lambda: None)}),


    _(set_, {'prog': (lambda *procs:
        [_(proc) for proc in procs])}),


    _(set_, {'let': (lambda vars_, *procs:
        _((lambda held_vars:
            _(prog,
                (lambda: _(set_, vars_)),
                *procs,
                (lambda: _(del_, *_(vars_.keys))),
                (lambda: _(set_, held_vars))
            )[1:-2]
        ), **{
            'held_vars':
                _((lambda g_vars:
                    {key: g_vars[key]
                        for key in vars_ if _(contains, g_vars, key)}
                ), **{
                    'g_vars': _(globals)
                })
        }))}),


    _(set_, {'if_': (lambda p, then, else_:
        _(then) if p else _(else_))}),


    _(set_, {'cond': (lambda *cases:
        _(prog,
            *_(next, (case[1:] for case in cases if case[0]))))}),


    _(set_, {'dolist': (lambda var, list_, *procs:
        _(let, {var: None},
            (lambda: [
                _(prog,
                    (lambda: _(set_, {var: elm})),
                    *procs
                )[1:]
            for elm in list_])
        )[0])}),


    _(set_, {'stop_iter': (lambda:
        _(next, _(iter, ())))}),


    _(set_, {'WhileIter': _(type, 'WhileIter', (object,), {
        '__init__': (lambda self, p:
            _(prog,
                (lambda: _(setattr, self, 'p', p)),
                nil
            )[1]),

        '__iter__': (lambda self: self),

        '__next__': (lambda self:
            _(if_, _(self.p),
                nil,
                stop_iter))
    })}),


    _(set_, {'while_': (lambda p, *procs:
        [_(prog, *procs) for dummy in _(WhileIter, p)])}),


    _(set_, {'wraps': _(__import__, 'functools').wraps}),


    _(set_, {'TailCall': _(type, 'TailCall', (object,), {
        'CONTINUE': _(object),
        'is_first_call': True,
        'func': None,

        '__init__': (lambda self: None),

        '__call__': (lambda self, func:
            _(_(wraps, func), (lambda *args, **kwargs:
                _(prog,
                    (lambda: _(setattr, TailCall, 'func', (lambda: _(func, *args, **kwargs)))),

                    (lambda: _(if_, TailCall.is_first_call,
                        (lambda: _(let, {'result': TailCall.CONTINUE},
                            (lambda: _(setattr, TailCall, 'is_first_call', False)),

                            (lambda: _(while_, (lambda: _(is_, result, TailCall.CONTINUE)),
                                (lambda: _(set_, {'result': _(TailCall.func)})))),

                            (lambda: _(setattr, TailCall, 'is_first_call', True)),
                            (lambda: _(setattr, TailCall, 'func', None)),
                            (lambda: result)
                        )[-1]),

                        (lambda: self.CONTINUE)))
                )[-1])))
    })}),


    _(set_, {'code': (lambda name:
        _(compile,
            _(_(open, _(__import__, name).__file__, 'r').read),
            name, 'eval'))}),


    _(set_, {'lispy': (lambda: _(code, __name__))})
)