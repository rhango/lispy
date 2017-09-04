(
    __import__('sys').path.append('../..'),
    eval(__import__('lispy').lispy()),

    _(set_, {'enum': _(__import__, 'enum')}),
    _(set_, {'abc': _(__import__, 'abc')}),
    _(set_, {'np': _(__import__, 'numpy')}),


    (
        _(set_, {'MaruBatu': _(enum.IntEnum, 'MaruBatu', {
            'NULL': 0,
            'MARU': 1,
            'BATU': -1,
        })}),

        _(setattr, MaruBatu, '__str__', (lambda self:
            _(cond,
                (_(is_, self, MaruBatu.MARU), (lambda: 'o')),
                (_(is_, self, MaruBatu.BATU), (lambda: 'x')),
                (True, (lambda: ' '))
            )[-1])),

        _(setattr, MaruBatu, 'get_opponent', (lambda self:
            _(MaruBatu, _(neg, self)))),
    ),


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
            _(eq, self.board[place], MaruBatu.NULL)),

        'put': (lambda self, place:
            _(if_, _(self.can_put, place),
                (lambda: _(prog,
                    (lambda: _(self.board.__setitem__, place, self.turn)),
                    (lambda: True)
                )[-1]),
                (lambda: False))),

        'exist_null_place': (lambda self:
            _(not_, _(self.board.all))),

        'check_win': (lambda self, marubatu:
            _((lambda board:
                _(any, (
                    _(_(board.all, axis=0).any),
                    _(_(board.all, axis=1).any),
                    _(_(board.diagonal).all),
                    _(_(board[::-1,:].diagonal).all)))
            ), **{
                'board': _(eq, self.board, marubatu)
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
            _(self.shift_to_check_state_process)),

        'shift_to_check_state_process': (lambda self:
            _((lambda game_state:
                _(prog,
                    (lambda: _(self.render)),
                    (lambda: _(cond,
                        (_(is_, game_state, State.PLAYING),
                            (lambda: _(self.player[self.turn].shift_to_think_process))),
                        (_(is_, game_state, State.MARU_WIN),
                            (lambda: _(print, "Info: Maru win"))),
                        (_(is_, game_state, State.BATU_WIN),
                            (lambda: _(print, "Info: Batu win"))),
                        (True, (lambda: _(print, "Info: Draw")))
                    )[-1])
                )[-1]
            ), **{
                'game_state': _(self.get_state)
            })),

        'shift_to_put_process': (lambda self, place:
            _(if_, _(self.put, place),
                (lambda: _(prog,
                    (lambda: _(setattr, self, 'turn', _(self.turn.get_opponent))),
                    (lambda: _(self.shift_to_check_state_process))
                )[-1]),
                (lambda: _(prog,
                    (lambda: _(print, "Error: There is already put")),
                    (lambda: _(self.player[self.turn].shift_to_think_process))
                )[-1])))
    })}),


    _(set_, {'Player': _(type, 'Player', (object,), {
        '__metaclass__': abc.ABCMeta,

        'setup': (lambda self, game, marubatu:
            _(prog,
                (lambda: _(setattr, self, 'game', game)),
                (lambda: _(setattr, self, 'marubatu', marubatu)),
                (lambda: self)
            )[-1]),

        'shift_to_think_process': _(abc.abstractmethod, (lambda self: None))
    })}),


    _(set_, {'Human': _(type, 'Human', (Player,), {
        '__init__': (lambda self:
            _(setattr, self, 'is_my_turn', False)),

        'shift_to_think_process': (lambda self:
            _(prog,
                (lambda: _(print, "Info: Your turn")),
                (lambda: _(setattr, self, 'is_my_turn', True))
            )[-1]),

        'put': (lambda self, place:
            _(cond,
                (_(or_,
                    _(gt, _(abs, _(sub, place[0], 1)), 1),
                    _(gt, _(abs, _(sub, place[1], 1)), 1)),
                        (lambda: _(print, "Error: Argment points outside the board"))),
                (self.is_my_turn,
                    (lambda: _(setattr, self, 'is_my_turn', False)),
                    (lambda: _(self.game.shift_to_put_process, place))),
                (True, (lambda: _(print, "Error: It is not your turn")))
            )[-1])
    })}),


    _(set_, {'Random': _(type, 'Random', (Player,), {
        '__init__': (lambda self: None),

        'shift_to_think_process': (lambda self:
            _(self.game.shift_to_put_process,
                _((lambda null_place:
                    _((lambda idx:
                        (null_place[0][idx], null_place[1][idx])
                    ), **{
                        'idx': _(np.random.randint, null_place[0].size)
                    })
                ), **{
                    'null_place': _(np.where, _(eq, self.game.board, MaruBatu.NULL))
                })))
    })}),


    _(set_, {'marubatu': (lambda: _(code, __name__))})
)