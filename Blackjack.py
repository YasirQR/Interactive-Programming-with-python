# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
    def cover(self, canvas, pos):
        card_loc = (CARD_BACK_CENTER[0], CARD_BACK_CENTER[1])
        canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [pos[0] + CARD_BACK_CENTER[0] + 1, pos[1] + CARD_BACK_CENTER[1] + 1], CARD_BACK_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand_field = []

    def __str__(self):
        self.hand_string = ""
        for i in range(len(self.hand_field)):
            self.hand_string += str(self.hand_field[i])
            self.hand_string += " "
      
        return "Hand contains " + self.hand_string
        
    def add_card(self, card):
        self.hand_field.append(card)

    def get_value(self):
        self.value = 0
        for i in range(len(self.hand_field)):
            for k, v in VALUES.items():
                if k in self.hand_field[i].get_rank():
                    self.value += v
        for card in self.hand_field:
            if card.get_rank() == "A" and (self.value + 10) <= 21:
                self.value += 10
            
        return self.value

   
    def draw(self, canvas, pos):
        for c in self.hand_field:
            c.draw(canvas, pos)
            pos[0] += 90
        
        
# define deck class 
class Deck:
    def __init__(self):
        self.decklist = []
        for i in range(len(SUITS)):
            for j in range(len(RANKS)):
                self.decklist.append(Card(SUITS[i],RANKS[j]))

    def shuffle(self):
        random.shuffle(self.decklist)

    def deal_card(self):
        return self.decklist.pop()
    
    def __str__(self):
        self.deck_string = ""
        for i in range(len(self.decklist)):
            self.deck_string += str(self.decklist[i])
            self.deck_string += " "
      
        return "Deck contains " + self.deck_string
    

#define event handlers for buttons
def deal():
    global outcome, in_play, game_deck, player_hand, dealer_hand, score
    
    if in_play:
        score -= 1

    game_deck = Deck()
    game_deck.shuffle()
    
    outcome = ""
    
    player_hand = Hand()
    dealer_hand = Hand()
    
    dealer_hand.add_card(game_deck.deal_card())
    dealer_hand.add_card(game_deck.deal_card())
    player_hand.add_card(game_deck.deal_card())
    player_hand.add_card(game_deck.deal_card())
    
    in_play = True

def hit():
    global in_play, score, outcome
    
    if in_play:
        player_hand.add_card(game_deck.deal_card())
    
    if player_hand.get_value() > 21 and in_play:
        outcome = "BUSTED! You lose"
        in_play = False
        score -= 1
    elif player_hand.get_value() == 21 and in_play:
        outcome = "BACKJACK!"
        in_play = False
        score += 1     

       
def stand():
    
    global score, outcome, in_play
    
    if player_hand.get_value() > 21 and in_play:
        outcome = "BUSTED! You lose"
    else:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(game_deck.deal_card())
            
        if dealer_hand.get_value() > 21 and in_play:
            outcome = "Dealer BUSTED! You win"
            score += 1
            in_play = False
        
        elif dealer_hand.get_value() >= player_hand.get_value() and in_play:
            outcome = "Dealer wins!"
            in_play = False
            score -= 1
        else:
            if in_play:  
                outcome = "You win!"
                in_play = False
                score += 1

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    canvas.draw_text('BlackJack', (80, 80), 64, 'Blue', 'serif')
    
    canvas.draw_text('Dealer', (50, 170), 30, "black")
    dealer_hand.draw(canvas, [50,200])
    
    canvas.draw_text('Player', (50, 370), 30, "black")
    player_hand.draw(canvas, [50,400])
    
    canvas.draw_text(outcome, (250, 370), 24, "black")
    canvas.draw_text("Score " + str(score), (450, 80), 30, "Black")
    
    if in_play:
        dealer_hand.hand_field[0].cover(canvas, [50,200])
    
    if in_play:
        canvas.draw_text("Hit or Stand?", (250, 170), 24, "black")
    else:
        canvas.draw_text('New Deal?', (250, 170), 30, "black")
    

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()