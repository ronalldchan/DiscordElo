import json
from Player import *


# with open('elo_player_data.json') as file:
#     data = json.load(file)
#
# test = {'a': 'something',
#         'b': 'something else'}
#
# testwrite = json.dumps(test)
# with open('elo_player_data.json', 'w') as f:
#     f.write(testwrite)
#     f.close()
# class Player:
#     def __init__(self, user_id, rating, wins, losses):
#         self.user_id = user_id
#         self.rating = rating
#         self.wins = wins
#         self.losses = losses


def encode_class(obj):
    if isinstance(obj, Player):
        return {'user_id': obj.user_id,
                'rating': obj.rating,
                'wins': obj.wins,
                'losses': obj.losses,
                obj.__class__.__name__: True}
    else:



# def write_json(data, filename):
#     with open(filename, 'w') as json_file:
#         json.dump(data, json_file, indent=4)
#
#
# def read_json(filename='elo_player_data.json'):
#     json_file = open(filename)
#     data = json.load(json_file)
#     json_file.close()
#     return data
#
# def write_player_json(player1_id, player2_id):
#     data = read_json('elo_player_data.json')
#     data['players']
#
# player_data = {
#     'players': [
#         {
#             'player_id': 'reggie',
#             'rating': 3561,
#             'wins': 15,
#             'loses': 3
#         },
#         {
#             'player_id': 'bobbie',
#             'rating': 5262,
#             'wins': 20,
#             'loses': 13
#         }
#     ]
# }
#
# match_data = {
#     'match': [
#         {
#             'match_id': 1,
#             'players': [
#                 {
#                     'user_id': 'bobbie',
#                     'deck': 'deck name'
#                 },
#                 {
#                     'user_id': 'reggie',
#                     'deck': 'deck name 2'
#                 }
#             ],
#             'winner': 'reggie'
#         }
#     ]
# }
# write_json(player_data, 'elo_player_data.json')
# write_json(match_data, 'elo_match_data.json')
#
#
# print(read_json('elo_player_data.json')['players'].filter())
# print(read_json('elo_match_data.json'))