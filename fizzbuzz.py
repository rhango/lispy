(
    eval(__import__('lispy').lispy),

    _(set_, {'fizzbuzz': (lambda n:
        _(dolist, 'i', _(range, 1, _(op.add, n, 1)),
            (lambda: _(cond,
                (_(op.eq, _(op.mod, i, 15), 0), (lambda: _(print, "FizzBuzz"))),
                (_(op.eq, _(op.mod, i,  3), 0), (lambda: _(print, "Fizz"))),
                (_(op.eq, _(op.mod, i,  5), 0), (lambda: _(print, "Buzz"))),
                (True, (lambda: _(print, i)))))))}),

    _(set_, {'main': (lambda:
        _(fizzbuzz, 100))}),

    _(if_, _(op.eq, __name__, '__main__'),
        main, nil)
)