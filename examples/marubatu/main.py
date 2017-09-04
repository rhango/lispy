(
    eval(__import__('marubatu').marubatu()),


    _(set_, {'main': (lambda:
        _(let, {
                'is_end': False,
                'end': (lambda: _(set_, {'is_end': True}))
            },
            (lambda: _(while_, (lambda: _(not_, is_end)),
                (lambda: _(print, "In :", end=" ")),
                (lambda: _(print, "Out:", _(eval, _(input)), end="\n\n"))))))}),


    _(main)
)