(
    __import__('sys').path.append('../'),
    eval(__import__('lispy').lispy()),


    _(set_, {'main': (lambda:
        _(let, {'x': 0},
            (lambda: _(while_, (lambda: _(lt, x, 100)),
                (lambda: _(set_, {'x': _(add, x, 1)})),
                (lambda: _(print, x))))))}),


    _(if_, _(eq, __name__, '__main__'),
        main, nil)
)