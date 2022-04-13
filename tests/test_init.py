import pytest

from WarpedDungeon.explore import init_dungeon


class test_args:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


def test_default_init():
    from dataclasses import asdict

    default_args = test_args(room_data='', start='1')
    default_dungeon = init_dungeon(default_args)

    assert default_dungeon.has_explorer is True
    assert default_dungeon.current_room == '1'
    assert asdict(default_dungeon.rooms['2']) == {
        'name': '2',
        'north': '1',
        'south': '7',
        'east': '5',
        'west': '3',
        'up': '6',
        'down': '4'
    }


def test_failed_init():
    bad_path = test_args(room_data='bad path', start='1')
    bad_start = test_args(room_data='', start='bad start')

    with pytest.raises(FileNotFoundError) as excinfo:
        init_dungeon(bad_path)
    assert "The file bad path does not exist." in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        init_dungeon(bad_start)
    assert "There is no room called bad start." in str(excinfo.value)
