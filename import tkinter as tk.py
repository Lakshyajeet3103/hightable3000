import tkinter as tk
import random


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.width = 50
        self.height = 70

    def draw(self, canvas, x, y):
        
        canvas.create_rectangle(x, y, x + self.width, y + self.height, fill='white', outline='black')
        
        canvas.create_text(x + self.width / 2, y + self.height / 2, text=f"{self.rank} {self.suit}", font=("Arial", 10))

def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    return [Card(suit, rank) for suit in suits for rank in ranks]

def animate():
    global x, current_card
    if current_card < len(deck):
        canvas.delete("all")  
        deck[current_card].draw(canvas, x, 250)
        x += 5  
        if x > 800:
            x = -50  
            current_card += 1  
        window.after(100, animate)  


window = tk.Tk()
window.title("Card Deck Animation")

canvas = tk.Canvas(window, width=800, height=600)
canvas.pack()


deck = create_deck()
x = -50  
current_card = 0  
animate()


window.mainloop()
