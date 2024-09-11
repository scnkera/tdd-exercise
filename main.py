VALID_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

def blackjack_score(hand):
    score = 0
    if len(hand) > 5:
        return None
    else: 
        for card in hand:
            if card in VALID_CARDS:
                if isinstance(card, int):
                    score += card
                    # print(score, card)
                elif card.isalpha() and card != 'Ace':
                    card = 10
                    score += card
                    # print(score, card)
                elif card.isalpha() and card == 'Ace': # card is 'Ace'
                    if score > 10:
                        card = 1
                    else:
                        card = 11
                    score += card
            else: 
                return None
    # print(score)
    return score

blackjack_score([1, 6, "Ace"])

