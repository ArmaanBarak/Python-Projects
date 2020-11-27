# Black Jack Game
# This code only represents some part of the original game and single player
# This is made using classes. I hope you like it.
# Made by: Armaan Barak

# Imports
from random import shuffle

# local game variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {
    'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
game_on = True

# Card Class
class Card:
    
    # Initializing a card with its suit and rank
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[self.rank]
    
    # String representation of a card
    def __repr__(self):
        return self.rank + ' of ' + self.suit

# Deck class
class Deck:
    
    # Initializing a deck with a list of cards which are object of card class
    def __init__(self):
        
        # cards lists
        self.all_cards = []
        
        # For every suit in suits tuple and every rank in rank tuple, creating cards for respective suits and ranks
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))
    
    # String representation of Deck
    def __repr__(self):
        text_to_print = 'CARDS IN DECK:'
        for card in self.all_cards:
            text_to_print += '\n' + card.__repr__()
        return text_to_print
    
    # Method to deal one card and removing it from deck
    def deal_one(self):
        return self.all_cards.pop()
    
    # Method to shuffle cards
    def shuffle_cards(self):
        shuffle(self.all_cards)
    
    # Method to reset the whole deck
    def reset(self):
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                
                self.all_cards.append(Card(suit, rank))
        
        # shuffling cards
        self.shuffle_cards()

# Chips class for player
class Chips:
    
    # Intializing chips class with total to default 100
    def __init__(self):
        self.total = 100
        self.bet = 0

    # Method to update total chips if win
    def win(self):
        self.total += self.bet
    
    # Method to update total chips if lose
    def lose(self):
        self.total -= self.bet

# Hand class to depict player and dealer
class Hand:
    
    # Initializing players card value and aces
    def __init__(self):
        self.all_cards = []
        self.value = 0
        self.aces = 0
    
    # Dealing cards to player
    def add_card(self, card):
        self.all_cards.append(card)
        self.value += card.value

        # Updating num of aces
        if card.rank == 'Ace':
            self.aces += 1
    
    # Adjusting ace value as per rule
    def adjust_ace_val(self):
        while self.aces and self.value > 21:
            self.value -= 10
            self.aces -= 1
    
    # Reseting player's and dealer's card
    def reset(self):
        self.all_cards = []
        self.value = 0
        self.aces = 0

# Gameplay Class to play game
class GamePlay:
    
    # Nothing to initialize with gameplay object
    def __init__(self):
        pass
    
    # Taking bet from player
    def take_bet(self, chips):
        
        while True:

            # Handling errors for wrong input
            try:
                chips.bet = int(input('Make a bet: '))

            except ValueError:
                print('Please enter integer value only.\n')
            else:
                if chips.bet > chips.total:
                    print('You do not have that many chips.\nRetry:\n')
                else:
                    break
    
    # dealing 2 cards
    def deal_cards(self, player, dealer, deck):

        # dealing cards to player and dealer
        for x in range(2):
            player.add_card(deck.deal_one())
            dealer.add_card(deck.deal_one())
            del x
    
    # Displaying player's and dealer's card and hiding one of dealer's card
    def display_some(self, player, dealer):
        print('\nPlayer\'s cards: ', *player.all_cards, sep='\n')
        print('\nDealer\'s cards: ', '<card hidden>', dealer.all_cards[1], sep='\n')
    
    # Displaying all the cards of both player and dealer
    def display_full(self, player, dealer):
        print("\nDealer's Hand:", *dealer.all_cards, sep='\n ')
        print("Dealer's Hand =",dealer.value)
        print("\nPlayer's Hand:", *player.all_cards, sep='\n ')
        print("Player's Hand =",player.value)
    
    # If player or dealer hits then deal one card
    def hit(self, deck, hand):
        
        hand.add_card(deck.deal_one())
        hand.adjust_ace_val()
    
    # Getting input to check if player wants to hit or stand
    def hit_or_stand(self, deck, player):
        global playing
        
        # working with only valid inputs
        while True:
            
            res = input('Do you want to Hit or Stand? h or s: ')
            
            if res[0].lower() == 'h':
                self.hit(deck, player)
            elif res[0].lower() == 's':
                print('Player chooses to Stand.\nDealer\'s turn: \n')
                playing = False
            else:
                print('Invalid Input!\nRetry:')
                continue
            break
    
    # If player busted
    def player_bust(self, chips):
        print('PLAYER BUSTED!!')
        chips.lose()
    
    # If player won
    def player_win(self, chips):
        print('Player Won!')
        chips.win()
    
    # If dealer busted
    def dealer_bust(self, chips):
        print('DEALER BUSTED!!')
        chips.win()
    
    # If dealer won
    def dealer_win(self, chips):
        print('Dealer Won!')
        chips.lose()
    
    # If game tied and its push
    def push(self):
        print('Dealer and Player tie! It\'s a push.')
    
    # If player wants to replay
    def replay(self):
        
        while True:
            
            res = input('Do you want to play again? Y or N: ')
            
            if res[0].lower() == 'y':
                return True
            elif res[0].lower() == 'n':
                return False
            else:
                print('Invalid Input!\nRetry: ')
                continue
            break    


# If its main file
if __name__ == "__main__":

    # Creating required game Objects
    deck_of_cards = Deck()
    deck_of_cards.shuffle_cards()
    player_hand = Hand()
    dealer_hand = Hand()
    player_chips = Chips()
    game_functions = GamePlay()


    # Playing Game
    while game_on:
        
        playing = True

        # Welcome message
        print('WELCOME TO BLACKJACK!')
        
        # taking bet
        game_functions.take_bet(player_chips)
        
        # dealing cards
        game_functions.deal_cards(player_hand, dealer_hand, deck_of_cards)
        
        # displaying some cards
        game_functions.display_some(player_hand, dealer_hand)
        
        # while player is playing
        while playing:
            
            # input if player wants to hit or stand
            game_functions.hit_or_stand(deck_of_cards, player_hand)
            
            # displaying some cards
            game_functions.display_some(player_hand, dealer_hand)
            
            # If player is busted
            if player_hand.value > 21:
                
                game_functions.player_bust(player_chips)
                break
        
        # If player is not busted and choose to stand
        if player_hand.value <= 21:
            
            # while dealer's cards value are less than 18 (18 choosen to be lowest value, can be changed, game works fine still)
            while dealer_hand.value < 18:
                
                # hitting dealer's deck
                game_functions.hit(deck_of_cards, dealer_hand)
            
            # displating full cards
            game_functions.display_full(player_hand, dealer_hand)
            
            # If dealer got busted
            if dealer_hand.value > 21:
                
                game_functions.dealer_bust(player_chips)
            
            elif dealer_hand.value < player_hand.value: # If Player won having value nearer to 21
                
                game_functions.player_win(player_chips)
                
            elif dealer_hand.value > player_hand.value: # If Dealer won having value nearer to 21
                
                    game_functions.dealer_win(player_chips)
                    
            else: # If it's a tie and game is pushed
                
                game_functions.push()
                
        # Displaying players chips after playing game
        print('Player now has total of {}'.format(player_chips.total))
        
        # If player doesn't wants to replay
        if not game_functions.replay():
            print('Thanks for playing!')
            break
        
        # Else reseting the deck, player's card, dealer's card
        else:
            deck_of_cards.reset()
            player_hand.reset()
            dealer_hand.reset()
            continue

