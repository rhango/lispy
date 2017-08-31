exec(__import__('lispy').lispy)
_(set_, {'functools': _(__import__, 'functools')})

_(set_, {'fib': _(_(functools.lru_cache, maxsize=None), (lambda n:
    _(cond,
        (_(op.eq, n, 0), (lambda: 0)),
        (_(op.eq, n, 1), (lambda: 1)),
        (True, (lambda: _(op.add, _(fib, _(op.sub, n, 1)), _(fib, _(op.sub, n, 2))))))))})

_(set_, {'main': (lambda:
    _(print, _(fib, 99)))})

_(if_, _(op.eq, __name__, '__main__'),
    main,
    nil)
