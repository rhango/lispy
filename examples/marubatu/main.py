(
    eval(__import__('marubatu').marubatu()),


    _(set_, {'main': (lambda:
        _(let, {
                'is_continue': True,
                'end': (lambda: _(set_, {'is_continue': False}))
            },
            (lambda: _(while_, (lambda: is_continue),
                (lambda: _(print, "In :", end=" ")),
                (lambda: _(print, "Out:", _(eval, _(input)), end="\n\n"))))))}),


    _(main)
)