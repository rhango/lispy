(
    __import__('sys').path.append('../'),
    eval(__import__('lispy').lispy()),

    _(set_, {'lru_cache': _(__import__, 'functools').lru_cache}),


    _(set_, {'fib': _(_(lru_cache, maxsize=None), (lambda n:
        _(cond,
            (_(eq, n, 0), (lambda: 0)),
            (_(eq, n, 1), (lambda: 1)),
            (True, (lambda: _(add, _(fib, _(sub, n, 1)), _(fib, _(sub, n, 2)))))
        )[-1]
    ))}),


    _(set_, {'main': (lambda:
        _(print, _(fib, 60)))}),


    _(if_, _(eq, __name__, '__main__'),
        main, nil)
)