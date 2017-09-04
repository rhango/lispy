(
    __import__('sys').path.append('..'),
    eval(__import__('lispy').lispy()),

    _(set_, {'sys': _(__import__, 'sys')}),
    _(set_, {'re': _(__import__, 're')}),


    _(set_, {'to_oneliner': (lambda target:
        _((lambda file_:
            _(" ".join,
                (_(re.sub, r"^\s+|\s+$", "", line)
                    for line in file_
                        if _(not_, _(re.search, r"^\s*$", line))))
        ), **{
            'file_': _(open, target, 'r')
        }))}),


    _(set_, {'main': (lambda:
        _(print, _(to_oneliner, sys.argv[1])))}),


    _(main)
)