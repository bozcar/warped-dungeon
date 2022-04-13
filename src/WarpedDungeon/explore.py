def init_dungeon():
    from argparse import ArgumentParser
    from pathlib import Path
    from importlib import resources

    from .explorer import rooms

    parser = ArgumentParser(description="Explore the warped dungeon in Senley Forest.")
    parser.add_argument('--room_data', '-rd', default='')
    parser.add_argument('--start', '-s', default='1')
    arguments = parser.parse_args()

    if arguments.room_data == '':
        pkg = resources.files("WarpedDungeon")
        room_data= pkg / "data" / "layout.json"
    else:
        room_data = Path(arguments.room_data)
        if not room_data.is_file():
            raise FileNotFoundError(f"The file {room_data} does not exist.")

    dungeon = rooms.from_json(room_data)
    dungeon.place_explorer(arguments.start)
    return dungeon


def help():
    return


def explore():
    dungeon = init_dungeon()

    run = True
    EXIT_COMMANDS = ['quit', 'q', 'x', 'exit', 'end']
    HELP_COMMANDS = ['help', 'h']
    EXPLORE_COMMANDS = {
        'go north' : dungeon.go_north,
        'go south' : dungeon.go_south,
        'go east' : dungeon.go_east,
        'go west' : dungeon.go_west,
        'go up' : dungeon.go_up,
        'go down' : dungeon.go_down,
        'inspect' : dungeon.inspect_room
    }

    while run:
        line = input("    ").lower()
        print()
        if line in EXIT_COMMANDS:
            run = False
        elif line in HELP_COMMANDS:
            help()
        elif line in EXPLORE_COMMANDS.keys():
            EXPLORE_COMMANDS[line]()
        else:
            print("Command not recognised.")
        print()

if __name__ == '__main__':
    explore()