from core.player_io import ask_player_action


def calculate_hand_value(hand: list[dict]) -> int:

    sum_hand = 0

    for item in hand:

        if (item["rank"] == "J") or (item["rank"] == "Q") or (item["rank"] == "K"):

            sum_hand += 10

        elif item["rank"] == "A":

            sum_hand += 1

        else:

            sum_hand += item["rank"]

    return sum_hand


def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:

    player["hand"].append (deck[0])
    deck.pop(0)
    player["hand"].append (deck[0])
    deck.pop(0)
    dealer["hand"].append (deck[0])
    deck.pop(0)
    dealer["hand"].append (deck[0])
    deck.pop(0)

    print ("the player hand:", calculate_hand_value(player["hand"]))
    print ("the dealer hand:", calculate_hand_value(dealer["hand"]))

    return None


def dealer_play(deck: list[dict], dealer: dict) -> bool:

    dealer_value_hand = calculate_hand_value(dealer["hand"])

    while dealer_value_hand < 17:
        dealer["hand"].append(deck[0])
        deck.pop(0)
        dealer_value_hand = calculate_hand_value(dealer["hand"])

    if 21 >= dealer_value_hand >= 17:
        return True

    elif dealer_value_hand > 21:
        print("the computer loss, you win")
        return False

    return True


def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:

    deal_two_each(deck, player, dealer)
    user_choices = ask_player_action()

    while user_choices != "S":
        if user_choices == "H":
            player["hand"].append(deck[0])
            deck.pop(0)
            sum_the_all_hand = calculate_hand_value(player["hand"])
            print("your hand:", sum_the_all_hand)
            if sum_the_all_hand > 21:
                print ("you loss, the dealer win")
                return None
        user_choices = ask_player_action()

    dealer_turn = dealer_play(deck, dealer)
    if not dealer_turn:
        return None
    else:
        pass

    user_score = calculate_hand_value (player["hand"])
    computer_score = calculate_hand_value (dealer["hand"])
    print("your hand:", user_score)
    print("dealer hand:", computer_score)
    if user_score > computer_score:
        print("you win")
    elif computer_score > user_score:
        print("the dealer win")
    else:
        print("tie")

    return None