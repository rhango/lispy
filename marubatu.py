(
    eval(__import__('lispy').lispy),

    _(set_, {'enum': _(__import__, 'enum')}),
    _(set_, {'abc': _(__import__, 'abc')}),
    _(set_, {'np': _(__import__, 'numpy')}),


    _(set_, {'MaruBatu': _(enum.IntEnum, 'MaruBatu', {
        'NULL': 0,
        'MARU': 1,
        'BATU': -1,
    })}),

    _(setattr, MaruBatu, '__str__', (lambda self:
        _(cond,
            (_(op.is_, self, MaruBatu.MARU), (lambda: 'o')),
            (_(op.is_, self, MaruBatu.BATU), (lambda: 'x')),
            (True, (lambda: ' '))
        )[-1])),

    _(setattr, MaruBatu, 'get_opponent', (lambda self:
        _(MaruBatu, _(op.neg, self)))),


    _(set_, {'State': _(enum.Enum, 'State', {
        'DRAW': 0,
        'MARU_WIN': 1,
        'BATU_WIN': -1,
        'PLAYING': 2
    })}),


    _(set_, {'Game': _(type, 'Game', (object,), {
        '__init__': (lambda self, maru_player, batu_player:
            _(prog,
                (lambda: _(setattr, self, 'player', {
                    MaruBatu.MARU: _(maru_player.setup, self, MaruBatu.MARU),
                    MaruBatu.BATU: _(batu_player.setup, self, MaruBatu.BATU)
                })),
                (lambda: _(setattr, self, 'board', _(np.zeros, (3,3), dtype=np.int8))),
                (lambda: _(setattr, self, 'turn', MaruBatu.MARU))
            )[0]),

        'can_put': (lambda self, place:
            _(op.eq, self.board[place], MaruBatu.NULL)),

        'put': (lambda self, place:
            _(if_, _(self.can_put, place),
                (lambda: _(prog,
                    (lambda: _(self.board.__setitem__, place, self.turn)),
                    (lambda: True)
                )[-1]),
                (lambda: False))),

        'exist_null_place': (lambda self:
            _(op.not_, _(self.board.all))),

        'check_win': (lambda self, marubatu:
            _((lambda board:
                _(any, (
                    _(_(board.all, axis=0).any),
                    _(_(board.all, axis=1).any),
                    _(_(board.diagonal).all),
                    _(_(board[::-1,:].diagonal).all)))
            ), **{
                'board': _(op.eq, self.board, marubatu)
            })),

        'get_state': (lambda self:
            _(cond,
                (_(self.check_win, MaruBatu.MARU), (lambda: State.MARU_WIN)),
                (_(self.check_win, MaruBatu.BATU), (lambda: State.BATU_WIN)),
                (_(self.exist_null_place), (lambda: State.PLAYING)),
                (True, (lambda: State.DRAW))
            )[-1]),

        'render': (lambda self:
            _(print,
                _("\n---+---+---\n".join,
                    _(map, (lambda board_row:
                        _("|".join,
                            _(map, (lambda marubatu:
                                _(" {} ".format, _(str, _(MaruBatu, marubatu)))),
                                board_row))),
                        self.board)),
                end="\n\n")),

        'start': (lambda self:
            _(self.process_turn)),

        'process_turn': (lambda self:
            _((lambda game_state:
                _(prog,
                    (lambda: _(self.render)),
                    (lambda: _(cond,
                        (_(op.is_, game_state, State.PLAYING), 
                            (lambda: _(self.player[self.turn].tell_your_turn))),
                        (_(op.is_, game_state, State.MARU_WIN),
                            (lambda: _(print, "Maru win!!\n"))),
                        (_(op.is_, game_state, State.BATU_WIN),
                            (lambda: _(print, "Batu win!!\n"))),
                        (True, (lambda: _(print, "Draw!!\n")))
                    )[-1])
                )[-1]
            ), **{
                'game_state': _(self.get_state)
            })),

        'tell_where_put': (lambda self, place:
            _(prog,
                (lambda: _(self.put, place)),
                (lambda: _(setattr, self, 'turn', _(self.turn.get_opponent))),
                (lambda: _(self.process_turn))
            )[-1])
    })}),


    _(set_, {'Player': _(type, 'Player', (object,), {
        '__metaclass__': abc.ABCMeta,

        'setup': (lambda self, game, marubatu:
            _(prog,
                (lambda: _(setattr, self, 'game', game)),
                (lambda: _(setattr, self, 'marubatu', marubatu)),
                (lambda: self)
            )[-1]),

        'tell_your_turn': _(abc.abstractmethod, (lambda self: None))
    })}),


    _(set_, {'Human': _(type, 'Human', (Player,), {
        '__init__': (lambda self: None),

        'tell_your_turn': (lambda self:
            _(print, "Your turn!\n"))
    })}),


    _(set_, {'Random': _(type, 'Random', (Player,), {
        '__init__': (lambda self: None),

        'tell_your_turn': (lambda self:
            _(self.game.tell_where_put,
                _((lambda null_place:
                    _((lambda idx:
                        (null_place[0][idx], null_place[1][idx])
                    ), **{
                        'idx': _(np.random.randint, null_place[0].size)
                    })
                ), **{
                    'null_place': _(np.where, _(op.eq, self.game.board, MaruBatu.NULL))
                })))
    })}),


    _(set_, {'main': (lambda:
        _(let, {
                'is_end': False,
                'end': (lambda: _(set_, {'is_end': True}))
            },
            (lambda: _(while_, (lambda: _(op.not_, is_end)),
                (lambda: _(print, "in :", end="")),
                (lambda: _(print, "out:", _(eval, _(input)), end="\n\n"))))))}),


    _(if_, _(op.eq, __name__, '__main__'),
        main, nil)
)