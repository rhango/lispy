(
    eval(__import__('lispy').lispy),

    _(set_, {'main': (lambda:
        _(let, {'x': 0},
            (lambda: _(while_, (lambda: _(op.lt, x, 100)),
                (lambda: _(set_, {'x': _(op.add, x, 1)})),
                (lambda: _(print, x))))))}),

    _(if_, _(op.eq, __name__, '__main__'),
        main,
        nil)
)