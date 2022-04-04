import json
import json_serialize
from Player import *

player_file = 'elo_player_data.json'


# will return object from read file
def read_file(filename: str):
    with open(filename, 'r') as file:
        data = json_serialize.convert_to_obj(json.load(file))
        file.close()
    return data


# converts whatever data is input into json and writes to file
def write_file(data, filename: str) -> None:
    with open(filename, 'w') as file:
        json.dump(json_serialize.convert_to_data(data), file, indent=4)
        file.close()


def read_players() -> [Player]:
    """return list of players from file"""
    return read_file(player_file)


def write_players(players: [Player]) -> None:
    """writes list of players to file"""
    write_file(players, player_file)
