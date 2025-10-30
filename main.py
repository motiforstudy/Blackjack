from core.deck import build_standard_deck, shuffle_by_suit
from core.game_logic import run_full_game



if __name__ == "__main__":

    build_the_deck = build_standard_deck()
    shuffle_the_deck = shuffle_by_suit(build_the_deck)

    player = {"hand" : []}
    dealer = {"hand" : []}

    run_full_game(shuffle_the_deck, player, dealer)