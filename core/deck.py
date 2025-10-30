import random



def build_standard_deck() -> list[dict]:

    the_deck = []
    suite = ["H", "C", "D", "S"]

    for i in range (2, 11):
        dict_of_card = {"rank" : i}
        dict_of_card["suite"] = suite[0]
        the_deck.append(dict_of_card)

    for i in range (2, 11):
        dict_of_card = {"rank" : i}
        dict_of_card["suite"] = suite[1]
        the_deck.append(dict_of_card)

    for i in range (2, 11):
        dict_of_card = {"rank" : i}
        dict_of_card["suite"] = suite[2]
        the_deck.append(dict_of_card)

    for i in range (2, 11):
        dict_of_card = {"rank" : i}
        dict_of_card["suite"] = suite[3]
        the_deck.append(dict_of_card)

    the_deck.append ({"rank" : "A", "suite" : "H"})
    the_deck.append({"rank": "A", "suite": "C"})
    the_deck.append({"rank": "A", "suite": "D"})
    the_deck.append({"rank": "A", "suite": "S"})
    the_deck.append({"rank": "J", "suite": "H"})
    the_deck.append({"rank": "J", "suite": "C"})
    the_deck.append({"rank": "J", "suite": "D"})
    the_deck.append({"rank": "J", "suite": "S"})
    the_deck.append({"rank": "Q", "suite": "H"})
    the_deck.append({"rank": "Q", "suite": "C"})
    the_deck.append({"rank": "Q", "suite": "D"})
    the_deck.append({"rank": "Q", "suite": "S"})
    the_deck.append({"rank": "K", "suite": "H"})
    the_deck.append({"rank": "K", "suite": "C"})
    the_deck.append({"rank": "K", "suite": "D"})
    the_deck.append({"rank": "K", "suite": "S"})

    return the_deck


def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:

    for i in range(swaps):

        not_good_index = True

        while not_good_index:

            random_index_1 = random.randint(0, 51)
            card_1 = deck[random_index_1]
            random_index_2 = random.randint(0, 51)
            card_2 = deck[random_index_2]

            if card_1["rank"] != card_2["rank"]:
                if card_1["suite"] == "H":
                    if random_index_2 % 5 != 0:
                        not_good_index = False
                        temp_value = card_1
                        deck[random_index_1] = card_2
                        deck[random_index_2] = temp_value
                elif card_1["suite"] == "C":
                    if random_index_2 % 3 != 0:
                        not_good_index = False
                        temp_value = card_1
                        deck[random_index_1] = card_2
                        deck[random_index_2] = temp_value
                elif card_1["suite"] == "D":
                    if random_index_2 % 2 != 0:
                        not_good_index = False
                        temp_value = card_1
                        deck[random_index_1] = card_2
                        deck[random_index_2] = temp_value
                elif card_1["suite"] == "S":
                    if random_index_2 % 7 != 0:
                        not_good_index = False
                        temp_value = card_1
                        deck[random_index_1] = card_2
                        deck[random_index_2] = temp_value

    return deck