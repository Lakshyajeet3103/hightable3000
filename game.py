from tkinter import *
import random
from PIL import Image,ImageTk
root= Tk()
root.title('Codemy.com-Card Deck')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("1000x800")
root.configure(background="red")
def resize_cards(card):
    our_card_img=Image.open(card)
    our_card_resize_image=out_card_img.resize((150,218))
    global our_card_image
    our_card_image=ImageTk.PhotoImage(our_card_resize_image)
    return r_card_image