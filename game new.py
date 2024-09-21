import tkinter as tk
import random
import time

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
        if card in ['J', 'Q', 'K']:
            return 10
        elif card == 'A':
            return 11
        else:
            return int(card)

    def deal_card(self):
        """Deal a card, and if the deck is low on cards, reshuffle it."""
        if len(self.deck) < 10:
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
            total -= 10
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
            self.balance += (3 / 2) * self.bet_amount
        elif "Dealer wins" in result:
            self.balance -= self.bet_amount

class BlackjackGUI:
    def __init__(self, root, num_decks=1):
        self.game = BlackjackGame(num_decks)
        self.root = root
        self.root.title("Blackjack Game")
        self.root.configure(bg='black')

        self.show_loading_screen()

        # Create UI elements
        self.create_ui()

    def show_loading_screen(self):
        """Display a loading screen."""
        self.loading_frame = tk.Frame(self.root, bg='black')
        self.loading_frame.pack(fill=tk.BOTH, expand=True)

        loading_label = tk.Label(self.loading_frame, text="Loading...", font=('Arial', 24), bg='black', fg='white')
        loading_label.pack(pady=20)

        loading_progress = tk.Label(self.loading_frame, text="Please wait...", font=('Arial', 16), bg='black', fg='grey')
        loading_progress.pack(pady=10)

        self.root.update()
        time.sleep(2)  # Simulating loading time
        self.loading_frame.destroy()  # Remove loading screen

    def create_ui(self):
        """Create the main game UI."""
        self.dealer_label = tk.Label(self.root, text="Dealer's Hand:", font=('Arial', 14, 'bold'), bg='red', fg='white')
        self.dealer_label.grid(row=0, column=0, padx=10, pady=10)

        self.player_label = tk.Label(self.root, text="Player's Hand:", font=('Arial', 14, 'bold'), bg='red', fg='white')
        self.player_label.grid(row=0, column=2, padx=10, pady=10)

        self.dealer_hand_display = tk.Label(self.root, font=('Arial', 14), bg='blue', fg='white')
        self.dealer_hand_display.grid(row=1, column=0, padx=10, pady=10)

        self.player_hand_display = tk.Label(self.root, font=('Arial', 14), bg='blue', fg='white')
        self.player_hand_display.grid(row=1, column=2, padx=10, pady=10)

        self.balance_label = tk.Label(self.root, text=f"Balance: ${self.game.balance}", font=('Arial', 14), bg='green', fg='white')
        self.balance_label.grid(row=5, column=0, padx=10, pady=10)

        self.bet_label = tk.Label(self.root, text="Bet Amount:", font=('Arial', 12), bg='grey', fg='white')
        self.bet_label.grid(row=6, column=0, padx=10, pady=10)

        self.bet_entry = tk.Entry(self.root, font=('Arial', 12))
        self.bet_entry.grid(row=6, column=1, padx=10, pady=10)

        self.hit_button = tk.Button(self.root, text="Hit", command=self.player_hit, font=('Arial', 12), bg='gold', activebackground='orange')
        self.hit_button.grid(row=7, column=0, padx=10, pady=10)

        self.stand_button = tk.Button(self.root, text="Stand", command=self.player_stand, font=('Arial', 12), bg='gold', activebackground='orange')
        self.stand_button.grid(row=7, column=2, padx=10, pady=10)

        self.result_label = tk.Label(self.root, font=('Arial', 14), bg='black', fg='white')
        self.result_label.grid(row=7, column=1, columnspan=1)

        self.restart_button = tk.Button(self.root, text="Restart", command=self.restart_game, font=('Arial', 12), bg='gold', activebackground='orange')
        self.restart_button.grid(row=9, column=0, columnspan=3, padx=10, pady=10)

        self.count_label = tk.Label(self.root, text=f"Card Count: {self.game.running_count}", font=('Arial', 12), bg='green', fg='white')
        self.count_label.grid(row=5, column=2, padx=10, pady=10)

        self.count_advice_label = tk.Label(self.root, font=('Arial', 12), bg='beige', fg='red')
        self.count_advice_label.grid(row=6, column=2, padx=10, pady=10)

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
        self.player_hand_display.config(
            text=f"Player: {self.game.player_hand} (Total: {self.game.calculate_hand_value(self.game.player_hand)})"
        )
        dealer_first_card = self.game.dealer_hand[0]
        self.dealer_hand_display.config(text=f"Dealer: [{dealer_first_card}, ?]")

        self.balance_label.config(text=f"Balance: ${self.game.balance}")
        self.count_label.config(text=f"Card Count: {self.game.running_count}")

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
        self.dealer_reveal()

    def dealer_reveal(self):
        """Reveal dealer's hand with a delay for animation."""
        dealer_first_card = self.game.dealer_hand[0]
        self.dealer_hand_display.config(text=f"Dealer: [{dealer_first_card}, ?]")
        self.root.after(1000, self.dealer_play)

    def dealer_play(self):
        """Dealer plays their hand."""
        self.game.dealer_play()
        self.end_game()

    def end_game(self, message=None):
        """End the game and display the result."""
        if message is None:
            message = self.game.check_winner()
        self.result_label.config(text=message)
        
        # Reveal the dealer's full hand
        self.dealer_hand_display.config(text=f"Dealer: {self.game.dealer_hand} (Total: {self.game.calculate_hand_value(self.game.dealer_hand)})")

        self.game.update_balance(message)
        self.hit_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    gui = BlackjackGUI(root)
    root.mainloop()
