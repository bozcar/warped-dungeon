from dataclasses import dataclass
from typing import List
import json

@dataclass
class room:
    name: str
    north: str
    south: str
    east: str
    west: str
    up: str
    down: str

class rooms:
    def __init__(self, rooms:List[room]):
        self.rooms = {}
        for room in rooms:
            self.rooms[room.name] = room

        self.has_explorer = False

    @classmethod
    def from_json(cls, json_file):
        with open(json_file, mode = 'r') as f:
            data:dict = json.load(f)
        
        rooms = []
        for key, value in data.items():
            rooms.append(room(
                name = key,
                north = value['N'],
                south = value['S'],
                east = value['E'],
                west = value['W'],
                up = value['U'],
                down = value['D']
            ))

        return cls(rooms)

    def place_explorer(self, room_name):
        if room_name in self.rooms.keys():
            self.current_room = room_name
            self.has_explorer = True
            return
        else: 
            raise ValueError(f"There is no room called {room_name}")
    
    def go_north(self):
        if self.has_explorer:
            print(f"Moved north from room {self.current_room} into room {self.rooms[self.current_room].north}")
            self.current_room = self.rooms[self.current_room].north
        else:
            raise RuntimeError("There is not currently an explorer placed in these rooms.")

    def go_south(self):
        if self.has_explorer:
            print(f"Moved south from room {self.current_room} into room {self.rooms[self.current_room].south}")
            self.current_room = self.rooms[self.current_room].south
        else:
            raise RuntimeError("There is not currently an explorer placed in these rooms.")
    
    def go_east(self):
        if self.has_explorer:
            print(f"Moved east from room {self.current_room} into room {self.rooms[self.current_room].east}")
            self.current_room = self.rooms[self.current_room].east
        else:
            raise RuntimeError("There is not currently an explorer placed in these rooms.")

    def go_west(self):
        if self.has_explorer:
            print(f"Moved west from room {self.current_room} into room {self.rooms[self.current_room].west}")
            self.current_room = self.rooms[self.current_room].west
        else:
            raise RuntimeError("There is not currently an explorer placed in these rooms.")

    def go_up(self):
        if self.has_explorer:
            print(f"Moved up from room {self.current_room} into room {self.rooms[self.current_room].up}")
            self.current_room = self.rooms[self.current_room].up
        else:
            raise RuntimeError("There is not currently an explorer placed in these rooms.")

    def go_down(self):
        if self.has_explorer:
            print(f"Moved down from room {self.current_room} into room {self.rooms[self.current_room].down}")
            self.current_room = self.rooms[self.current_room].down
        else:
            raise RuntimeError("There is not currently an explorer placed in these rooms.")

    def inspect_room(self):
        if self.has_explorer:
            print(f"The door to the north leads to room {self.rooms[self.current_room].north}.")
            print(f"The door to the east leads to room {self.rooms[self.current_room].east}.")
            print(f"The door to the south leads to room {self.rooms[self.current_room].south}.")
            print(f"The door to the west leads to room {self.rooms[self.current_room].west}.")
            print(f"The trapdoor in the ceiling leads to room {self.rooms[self.current_room].up}.")
            print(f"The trapdoor in the floor leads to room {self.rooms[self.current_room].down}.")
        else:
            raise RuntimeError("There is not currently an explorer placed in these rooms.")