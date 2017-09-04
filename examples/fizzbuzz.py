(
    __import__('sys').path.append('..'),
    eval(__import__('lispy').lispy()),


    _(set_, {'fizzbuzz': (lambda n:
        _(dolist, 'i', _(range, 1, _(add, n, 1)),
            (lambda: _(cond,
                (_(eq, _(mod, i, 15), 0), (lambda: _(print, "FizzBuzz"))),
                (_(eq, _(mod, i,  3), 0), (lambda: _(print, "Fizz"))),
                (_(eq, _(mod, i,  5), 0), (lambda: _(print, "Buzz"))),
                (True, (lambda: _(print, i)))))))}),


    _(set_, {'main': (lambda:
        _(fizzbuzz, 100))}),


    _(main)
)