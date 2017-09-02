(
    eval(__import__('lispy').lispy),

    _(set_, {'lru_cache': _(__import__, 'functools').lru_cache}),


    _(set_, {'fib': _(_(lru_cache, maxsize=None), (lambda n:
        _(cond,
            (_(op.eq, n, 0), (lambda: 0)),
            (_(op.eq, n, 1), (lambda: 1)),
            (True, (lambda: _(op.add, _(fib, _(op.sub, n, 1)), _(fib, _(op.sub, n, 2)))))
        )[-1]
    ))}),


    _(set_, {'main': (lambda:
        _(print, _(fib, 66)))}),


    _(if_, _(op.eq, __name__, '__main__'),
        main, nil)
)