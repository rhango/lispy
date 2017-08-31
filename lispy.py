(
    globals().update({'set_': (lambda vars_:
        globals().update(vars_))}),

    set_({'_': (lambda func, *args, **kwargs:
        func(*args, **kwargs))}),

    _(set_, {'del_': (lambda *keys:
        [_(_(globals).pop, key) for key in keys])}),

    _(set_, {'nil': (lambda: None)}),

    _(set_, {'if_': (lambda p, then, else_:
        _(then) if p else _(else_))}),

    _(set_, {'cond': (lambda *cases:
        _(_(next, (case[1] for case in cases if case[0]))))}),

    _(set_, {'prog': (lambda *procs:
        [_(proc) for proc in procs])}),

    _(set_, {'let': (lambda vars_, *procs:
        _(prog,
            (lambda: _(set_, vars_)),
            *procs,
            (lambda: _(del_, *_(vars_.keys)))
        )[1:-1])}),

    _(set_, {'dolist': (lambda var, list_, *procs:
        _(prog,
            (lambda: [
                _(prog,
                    (lambda: _(set_, {var: elm})),
                    *procs
                )[1:]
            for elm in list_]),
            (lambda: _(del_, var))
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

    _(set_, {'op': _(__import__, 'operator')}),

    _(set_, {'code': (lambda file:
        _(compile, _(_(open, file, 'r').read), file, 'eval'))}),

    _(set_, {'lispy': _(code, "lispy.py")})
)