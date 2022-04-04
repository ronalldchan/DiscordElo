k_factor = 32
f_factor = 400


def only_positive(num: int) -> int:
    if num < 0:
        return 0
    else:
        return num


def match_result(player1_rating: int, player2_rating: int, draw: bool = False) -> (int, int):
    """return new elo values of match assuming player1 is the winner"""
    rating_difference = player2_rating - player1_rating
    rating_ratio = float(rating_difference / f_factor)

    player1_expected = 1 / (1 + pow(10, rating_ratio))
    player2_expected = 1 / (1 + pow(10, rating_ratio * -1))

    if not draw:
        player1_new_rating = int(player1_rating + k_factor * (1 - player1_expected))
        player2_new_rating = int(player2_rating + k_factor * (0 - player2_expected))
    else:
        player1_new_rating = int(player1_rating + k_factor * (0.5 - player1_expected))
        player2_new_rating = int(player2_rating + k_factor * (0.5 - player2_expected))
    return player1_new_rating, player2_new_rating
