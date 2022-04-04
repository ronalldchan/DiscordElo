import elo

default_rating = 400


class Player:
    def __init__(self, user_id: int, rating: int = default_rating, wins: int = 0, losses: int = 0):
        self.user_id = user_id
        self.rating = rating
        self.wins = wins
        self.losses = losses

    def __lt__(self, other):
        return self.rating < other.rating

    def __repr__(self):
        return f'({self.user_id}, {self.rating}, {self.wins}, {self.losses})'


def get_player_from_list(player_list: [Player], player_id: int):
    """return player object given player id else add default player to list and return player"""
    for p in player_list:
        if p.user_id == player_id:
            return p
    new_player = Player(player_id)
    player_list.append(new_player)
    return new_player


def player_match(player1: Player, player2: Player, draw: bool = False) -> (Player, Player):
    """modifies player ratings based on elo match result assuming player1 is winner"""
    (player1_result, player2_result) = elo.match_result(player1.rating, player2.rating, draw)
    player1.rating = player1_result
    player2.rating = player2_result
    if not draw:
        player1.wins += 1
        player2.losses += 1
    return player1, player2


def player_match_difference(player1: Player, player2: Player, draw: bool = False) -> (int, int):
    """return potential resulting difference of a match assuming player 1 is winner"""
    player1_og_rating = player1.rating
    player2_og_rating = player2.rating
    (player1_new_rating, player2_new_rating) = elo.match_result(player1_og_rating, player2_og_rating, draw)
    player1_diff = player1_new_rating - player1_og_rating
    player2_diff = player2_new_rating - player2_og_rating
    return player1_diff, player2_diff
