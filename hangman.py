import random
from tkinter import *

def new_game():
    global answer, letter_list, all_chance
    words = ['banana', 'apple', 'mango', 'orange', 'cucumber',
             'watermelon', 'melon', 'coconut', 'strawberry',
             'blueberry', 'peach', 'tomato']

    answer = random.choice(words)
    letter_list = ['-' for i in answer]
    all_chance = len(letter_list) + 3

def end_game():
    new_game()
    label_word.config(text=f"{' '.join(letter_list)}")

def check_letters():
    global all_chance
    resualt.config(text=' ')
    new_letter = your_letter.get()
    if new_letter in answer:
        for indexes, letter in enumerate(answer):
            if letter == new_letter:
                letter_list[indexes] = letter
                label_word.config(text=f"{' '.join(letter_list)}")
    if (new_letter == answer) or ('-' not in letter_list):
        resualt.config(text=f'you won the game, answer is : {answer}')
        end_game()

    all_chance -= 1
    your_letter.delete(0,END)
    label_chance.config(text=f"Remaining chances : {all_chance}")
    if all_chance == 0:
        resualt.config(text=f'ops!!! you lose the game, answer is : {answer}')
        end_game()

new_game()

window = Tk()
window.title('Hangman Game')
window.geometry("300x350")

label_word = Label(window, text=f"{' '.join(letter_list)}",
                   justify="center",font=("tahoma", 20))
label_word.pack(fill="both",pady=25)

my_label = Label(window, text="Enter a letter or a word",
                 justify="center",font=("tahoma", 10))
my_label.pack(fill="both",pady=10)
your_letter = Entry(window, justify="center", font=("tahoma", 20))
your_letter.pack(fill="both",pady=5, padx= 20)

btn = Button(window, text="Submit",
             font=("tahoma", 11), command=check_letters)
btn.pack(padx=10, pady=5)

label_chance = Label(window, text=f"Remaining chances : {all_chance}",
                     justify="center",font=("tahoma", 12))
label_chance.pack(fill="both",pady=5)

resualt = Label(window,font=("tahoma", 10) , text='',
               justify=CENTER , bd=0 , bg = "systembuttonface")
resualt.pack(fill="both",pady=5)

window.mainloop()