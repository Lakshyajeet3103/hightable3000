import tkinter as tk
import random

# Class to handle Blackjack Game
class BlackjackGame:
    def __init__(self, num_decks=1, starting_balance=100000):
        self.num_decks = num_decks
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []
        self.running_count = 0
        self.balance = starting_balance
        self.bet_amount = 0

    def create_deck(self):
        """Create and shuffle a deck using the specified number of decks."""
        deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4 * self.num_decks
        random.shuffle(deck)
        return deck

    def card_value(self, card):
        """Get the numeric value of a card for Blackjack."""
        if card in ['J', 'Q', 'K']:  # Face cards are worth 10
            return 10
        elif card == 'A':  # Ace can be 11 or 1
            return 11
        else:  # Number cards are worth their face value
            return int(card)

    def deal_card(self):
        """Deal a card, and if the deck is low on cards, reshuffle it."""
        if len(self.deck) < 10:  # Reshuffle if fewer than 10 cards left
            self.deck = self.create_deck()
        card = self.deck.pop()
        self.update_card_count(card)
        return card

    def update_card_count(self, card):
        """Update the running count for card counting (Hi-Lo system)."""
        if card in ['2', '3', '4', '5', '6']:
            self.running_count += 1
        elif card in ['10', 'J', 'Q', 'K', 'A']:
            self.running_count -= 1

    def start_game(self, bet):
        """Start a new game by dealing two cards to both the player and dealer."""
        self.bet_amount = bet
        self.player_hand = [self.deal_card(), self.deal_card()]
        self.dealer_hand = [self.deal_card(), self.deal_card()]

    def calculate_hand_value(self, hand):
        """Calculate the total value of a hand, adjusting for Aces if needed."""
        total = sum(self.card_value(card) for card in hand)
        aces = hand.count('A')
        while total > 21 and aces:
            total -= 10  # Adjust Ace from 11 to 1
            aces -= 1
        return total

    def player_has_blackjack(self):
        """Check if the player has a Blackjack (21 with two cards)."""
        return self.calculate_hand_value(self.player_hand) == 21 and len(self.player_hand) == 2

    def player_hit(self):
        """Player takes an additional card."""
        self.player_hand.append(self.deal_card())

    def dealer_play(self):
        """Dealer hits until their hand value is 17 or higher."""
        while self.calculate_hand_value(self.dealer_hand) < 17:
            self.dealer_hand.append(self.deal_card())

    def check_winner(self):
        """Determine the winner based on the player's and dealer's hand values."""
        player_total = self.calculate_hand_value(self.player_hand)
        dealer_total = self.calculate_hand_value(self.dealer_hand)

        if player_total > 21:
            return "Player busts! Dealer wins!"
        elif dealer_total > 21:
            return "Dealer busts! Player wins!"
        elif player_total > dealer_total:
            return "Player wins!"
        elif dealer_total > player_total:
            return "Dealer wins!"
        else:
            return "It's a tie!"

    def update_balance(self, result):
        """Update the balance based on the result of the round."""
        if "Player wins" in result:
            self.balance += self.bet_amount
        elif "Dealer wins" in result:
            self.balance -= self.bet_amount

# Class to handle the GUI for the Blackjack game
class BlackjackGUI:
    def __init__(self, root, num_decks=1):
        self.game = BlackjackGame(num_decks)
        self.root = root
        self.root.title("Blackjack Game")

        # Labels for player and dealer hands
        self.dealer_label = tk.Label(self.root, text="Dealer's Hand:", font=('Arial', 14))
        self.dealer_label.grid(row=0, column=0, padx=10, pady=10)

        self.player_label = tk.Label(self.root, text="Player's Hand:", font=('Arial', 14))
        self.player_label.grid(row=2, column=0, padx=10, pady=10)

        # Display for cards
        self.dealer_hand_display = tk.Label(self.root, font=('Arial', 14))
        self.dealer_hand_display.grid(row=1, column=0, padx=10, pady=10)

        self.player_hand_display = tk.Label(self.root, font=('Arial', 14))
        self.player_hand_display.grid(row=3, column=0, padx=10, pady=10)

        # Bet and balance display
        self.balance_label = tk.Label(self.root, text=f"Balance: ${self.game.balance}", font=('Arial', 14))
        self.balance_label.grid(row=4, column=0, padx=10, pady=10)

        self.bet_label = tk.Label(self.root, text="Bet Amount:", font=('Arial', 12))
        self.bet_label.grid(row=5, column=0, padx=10, pady=10)

        self.bet_entry = tk.Entry(self.root, font=('Arial', 12))
        self.bet_entry.grid(row=5, column=1, padx=10, pady=10)

        # Action buttons
        self.hit_button = tk.Button(self.root, text="Hit", command=self.player_hit, font=('Arial', 12))
        self.hit_button.grid(row=6, column=0, padx=10, pady=10)

        self.stand_button = tk.Button(self.root, text="Stand", command=self.player_stand, font=('Arial', 12))
        self.stand_button.grid(row=6, column=1, padx=10, pady=10)

        self.result_label = tk.Label(self.root, font=('Arial', 14))
        self.result_label.grid(row=7, column=0, columnspan=2)

        self.restart_button = tk.Button(self.root, text="Restart", command=self.restart_game, font=('Arial', 12))
        self.restart_button.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

        # Card counting display
        self.count_label = tk.Label(self.root, text=f"Card Count: {self.game.running_count}", font=('Arial', 12))
        self.count_label.grid(row=4, column=2, padx=10, pady=10)

        self.count_advice_label = tk.Label(self.root, font=('Arial', 12))
        self.count_advice_label.grid(row=5, column=2, padx=10, pady=10)

        # Start the first game
        self.restart_game()

    def restart_game(self):
        """Restart the game and reset the display."""
        self.result_label.config(text="")
        bet = int(self.bet_entry.get() or 0)
        if bet > self.game.balance:
            self.result_label.config(text="Insufficient balance for that bet!")
            return
        self.game.start_game(bet)
        self.update_display()

        if self.game.player_has_blackjack():
            self.end_game("Blackjack! Player wins!")
        else:
            self.hit_button.config(state=tk.NORMAL)
            self.stand_button.config(state=tk.NORMAL)

    def update_display(self):
        """Update the display for both player and dealer hands and card count."""
        self.player_hand_display.config(text=f"Player: {self.game.player_hand} (Total: {self.game.calculate_hand_value(self.game.player_hand)})")
        dealer_first_card = self.game.dealer_hand[0]
        self.dealer_hand_display.config(text=f"Dealer: [{dealer_first_card}, ?]")

        # Update balance and card count display
        self.balance_label.config(text=f"Balance: ${self.game.balance}")
        self.count_label.config(text=f"Card Count: {self.game.running_count}")
        
        # Card count advice
        if self.game.running_count > 0:
            self.count_advice_label.config(text="Higher chances to win!")
        elif self.game.running_count < 0:
            self.count_advice_label.config(text="Lower chances to win!")
        else:
            self.count_advice_label.config(text="Neutral count.")

    def player_hit(self):
        """Handle the player hitting to take another card."""
        self.game.player_hit()
        self.update_display()

        if self.game.calculate_hand_value(self.game.player_hand) > 21:
            self.end_game("Player busts! Dealer wins!")

    def player_stand(self):
        """Handle the player standing to end their turn."""
        self.game.dealer_play()
        self.end_game()

    def end_game(self, message=None):
        """End the game and display the result."""
        if message is None:
            message = self.game.check_winner()
        self.result_label.config(text=message)
        self.game.update_balance(message)
        self.hit_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)

# Main part to run the game
if __name__ == "__main__":
    root = tk.Tk()
    gui = BlackjackGUI(root)
    root.mainloop()
