import tkinter as tk
import random


ASCII_CARDS = {
    '2 of Hearts': """
     _______
    |2      |
    |  ♥   |
    |       |
    |       |
    |______2|
    """,
    '3 of Hearts': """
     _______
    |3      |
    |  ♥   |
    |       |
    |       |
    |______3|
    """,
    '4 of Hearts': """
     _______
    |4      |
    |  ♥   |
    |       |
    |       |
    |______4|
    """,
    '5 of Hearts': """
     _______
    |5      |
    |  ♥   |
    |       |
    |       |
    |______5|
    """,
    '6 of Hearts': """
     _______
    |6      |
    |  ♥   |
    |       |
    |       |
    |______6|
    """,
    '7 of Hearts': """
     _______
    |7      |
    |  ♥   |
    |       |
    |       |
    |______7|
    """,
    '8 of Hearts': """
     _______
    |8      |
    |  ♥   |
    |       |
    |       |
    |______8|
    """,
    '9 of Hearts': """
     _______
    |9      |
    |  ♥   |
    |       |
    |       |
    |______9|
    """,
    '10 of Hearts': """
     _______
    |10     |
    |  ♥   |
    |       |
    |       |
    |_____10|
    """,
    'Jack of Hearts': """
     _______
    |Jack    |
    |  ♥   |
    |       |
    |       |
    |______J|
    """,
    'Queen of Hearts': """
     _______
    |Queen   |
    |  ♥   |
    |       |
    |       |
    |_____Q |
    """,
    'King of Hearts': """
     _______
    |King    |
    |  ♥   |
    |       |
    |       |
    |_____K |
    """,
    'Ace of Hearts': """
     _______
    |Ace     |
    |  ♥   |
    |       |
    |       |
    |______A|
    """,
    
    '2 of Diamonds': """
     _______
    |2      |
    |  ♦   |
    |       |
    |       |
    |______2|
    """,
    '3 of Diamonds': """
     _______
    |3      |
    |  ♦   |
    |       |
    |       |
    |______3|
    """,
    '4 of Diamonds': """
     _______
    |4      |
    |  ♦   |
    |       |
    |       |
    |______4|
    """,
    '5 of Diamonds': """
     _______
    |5      |
    |  ♦   |
    |       |
    |       |
    |______5|
    """,
    '6 of Diamonds': """
     _______
    |6      |
    |  ♦   |
    |       |
    |       |
    |______6|
    """,
    '7 of Diamonds': """
     _______
    |7      |
    |  ♦   |
    |       |
    |       |
    |______7|
    """,
    '8 of Diamonds': """
     _______
    |8      |
    |  ♦   |
    |       |
    |       |
    |______8|
    """,
    '9 of Diamonds': """
     _______
    |9      |
    |  ♦   |
    |       |
    |       |
    |______9|
    """,
    '10 of Diamonds': """
     _______
    |10     |
    |  ♦   |
    |       |
    |       |
    |_____10|
    """,
    'Jack of Diamonds': """
     _______
    |Jack    |
    |  ♦   |
    |       |
    |       |
    |______J|
    """,
    'Queen of Diamonds': """
     _______
    |Queen   |
    |  ♦   |
    |       |
    |       |
    |_____Q |
    """,
    'King of Diamonds': """
     _______
    |King    |
    |  ♦   |
    |       |
    |       |
    |_____K |
    """,
    'Ace of Diamonds': """
     _______
    |Ace     |
    |  ♦   |
    |       |
    |       |
    |______A|
    """,
    
    
    '2 of Clubs': """
     _______
    |2      |
    |  ♣   |
    |       |
    |       |
    |______2|
    """,
    '3 of Clubs': """
     _______
    |3      |
    |  ♣   |
    |       |
    |       |
    |______3|
    """,
    '4 of Clubs': """
     _______
    |4      |
    |  ♣   |
    |       |
    |       |
    |______4|
    """,
    '5 of Clubs': """
     _______
    |5      |
    |  ♣   |
    |       |
    |       |
    |______5|
    """,
    '6 of Clubs': """
     _______
    |6      |
    |  ♣   |
    |       |
    |       |
    |______6|
    """,
    '7 of Clubs': """
     _______
    |7      |
    |  ♣   |
    |       |
    |       |
    |______7|
    """,
    '8 of Clubs': """
     _______
    |8      |
    |  ♣   |
    |       |
    |       |
    |______8|
    """,
    '9 of Clubs': """
     _______
    |9      |
    |  ♣   |
    |       |
    |       |
    |______9|
    """,
    '10 of Clubs': """
     _______
    |10     |
    |  ♣   |
    |       |
    |       |
    |_____10|
    """,
    'Jack of Clubs': """
     _______
    |Jack    |
    |  ♣   |
    |       |
    |       |
    |______J|
    """,
    'Queen of Clubs': """
     _______
    |Queen   |
    |  ♣   |
    |       |
    |       |
    |_____Q |
    """,
    'King of Clubs': """
     _______
    |King    |
    |  ♣   |
    |       |
    |       |
    |_____K |
    """,
    'Ace of Clubs': """
     _______
    |Ace     |
    |  ♣   |
    |       |
    |       |
    |______A|
    """,
    
    
    '2 of Spades': """
     _______
    |2      |
    |  ♠   |
    |       |
    |       |
    |______2|
    """,
    '3 of Spades': """
     _______
    |3      |
    |  ♠   |
    |       |
    |       |
    |______3|
    """,
    '4 of Spades': """
     _______
    |4      |
    |  ♠   |
    |       |
    |       |
    |______4|
    """,
    '5 of Spades': """
     _______
    |5      |
    |  ♠   |
    |       |
    |       |
    |______5|
    """,
    '6 of Spades': """
     _______
    |6      |
    |  ♠   |
    |       |
    |       |
    |______6|
    """,
    '7 of Spades': """
     _______
    |7      |
    |  ♠   |
    |       |
    |       |
    |______7|
    """,
    '8 of Spades': """
     _______
    |8      |
    |  ♠   |
    |       |
    |       |
    |______8|
    """,
    '9 of Spades': """
     _______
    |9      |
    |  ♠   |
    |       |
    |       |
    |______9|
    """,
    '10 of Spades': """
     _______
    |10     |
    |  ♠   |
    |       |
    |       |
    |_____10|
    """,
    'Jack of Spades': """
     _______
    |Jack    |
    |  ♠   |
    |       |
    |       |
    |______J|
    """,
    'Queen of Spades': """
     _______
    |Queen   |
    |  ♠   |
    |       |
    |       |
    |_____Q |
    """,
    'King of Spades': """
     _______
    |King    |
    |  ♠   |
    |       |
    |       |
    |_____K |
    """,
    'Ace of Spades': """
     _______
    |Ace     |
    |  ♠   |
    |       |
    |       |
    |______A|
    """,
}

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
        deck = [f'{rank} of {suit}' for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']
                for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']] * self.num_decks
        random.shuffle(deck)
        return deck

    def card_value(self, card):
        """Get the numeric value of a card for Blackjack."""
        rank = card.split()[0]
        if rank in ['Jack', 'Queen', 'King']:
            return 10
        elif rank == 'Ace':
            return 11
        else:
            return int(rank)

    def deal_card(self):
        """Deal a card, and if the deck is low on cards, reshuffle it."""
        if len(self.deck) < 10:
            self.deck = self.create_deck()
        card = self.deck.pop()
        self.update_card_count(card)
        return card

    def update_card_count(self, card):
        """Update the running count for card counting (Hi-Lo system)."""
        rank = card.split()[0]
        if rank in ['2', '3', '4', '5', '6']:
            self.running_count += 1
        elif rank in ['10', 'Jack', 'Queen', 'King', 'Ace']:
            self.running_count -= 1

    def start_game(self, bet):
        """Start a new game by dealing two cards to both the player and dealer."""
        self.bet_amount = bet
        self.player_hand = [self.deal_card(), self.deal_card()]
        self.dealer_hand = [self.deal_card(), self.deal_card()]

    def calculate_hand_value(self, hand):
        """Calculate the total value of a hand, adjusting for Aces if needed."""
        total = sum(self.card_value(card) for card in hand)
        aces = hand.count('Ace of Hearts') + hand.count('Ace of Diamonds') + hand.count('Ace of Clubs') + hand.count('Ace of Spades')
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

        # Set up labels and buttons
        self.dealer_label = tk.Label(self.root, text="Dealer's Hand:", font=('Arial', 14, 'bold'), bg='red', fg='white')
        self.dealer_label.grid(row=0, column=0, padx=10, pady=10)

        self.player_label = tk.Label(self.root, text="Player's Hand:", font=('Arial', 14, 'bold'), bg='red', fg='white')
        self.player_label.grid(row=0, column=2, padx=10, pady=10)

        self.dealer_hand_display = tk.Text(self.root, height=10, width=30, font=('Courier', 12), bg='blue', fg='white')
        self.dealer_hand_display.grid(row=1, column=0, padx=10, pady=10)

        self.player_hand_display = tk.Text(self.root, height=10, width=30, font=('Courier', 12), bg='blue', fg='white')
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
        player_hand_ascii = "\n".join(ASCII_CARDS[card] for card in self.game.player_hand)
        dealer_hand_ascii = "\n".join(ASCII_CARDS[card] for card in self.game.dealer_hand) if self.game.dealer_hand else ""

        self.player_hand_display.delete(1.0, tk.END)
        self.player_hand_display.insert(tk.END, player_hand_ascii)
        self.dealer_hand_display.delete(1.0, tk.END)
        self.dealer_hand_display.insert(tk.END, f"Dealer:\n{ASCII_CARDS[self.game.dealer_hand[0]]}\n[?]")

        self.balance_label.config(text=f"Balance: ${self.game.balance}")
        self.count_label.config(text=f"Card Count: {self.game.running_count}")

        if self.game.running_count > 0:
            self.count_advice_label.config(text="Higher chances to win!")
        elif self.game.running_count < 0:
            self.count_advice_label.config(text="Lower chances to win!")
        else:
            self.count_advice_label.config(text="Neutral count.")

    def player_hit(self):
        """Handle the player's hit action."""
        self.game.player_hit()
        self.update_display()
        if self.game.calculate_hand_value(self.game.player_hand) > 21:
            self.end_game("Player busts! Dealer wins!")

    def player_stand(self):
        """Handle the player's stand action."""
        self.game.dealer_play()
        dealer_total = self.game.calculate_hand_value(self.game.dealer_hand)
        self.update_display()
        result = self.game.check_winner()
        self.end_game(result)

    def end_game(self, result):
        """End the game and update the balance."""
        self.result_label.config(text=result)
        self.game.update_balance(result)
        self.hit_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)

    def run(self):
        """Start the GUI loop."""
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    gui = BlackjackGUI(root)
    gui.run()
