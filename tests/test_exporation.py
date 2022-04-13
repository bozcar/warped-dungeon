import pytest

from WarpedDungeon.explore import init_dungeon


class test_args:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


@pytest.mark.parametrize("test_method,expected", [
    ('N', '6'),
    ('S', '4'),
    ('E', '5'),
    ('W', '3'),
    ('U', '2'),
    ('D', '8'),
])
def test_movement(test_method, expected):
    default_args = test_args(room_data='', start='1')
    default_dungeon = init_dungeon(default_args)

    MOVES = {
        'N': default_dungeon.go_north,
        'S': default_dungeon.go_south,
        'E': default_dungeon.go_east,
        'W': default_dungeon.go_west,
        'U': default_dungeon.go_up,
        'D': default_dungeon.go_down,
    }

    MOVES[test_method]()
    assert default_dungeon.current_room == expected
