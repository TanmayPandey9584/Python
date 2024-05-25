import numpy as np
import tkinter as tk

choices = np.array(['rock', 'paper', 'scissor'])

def user():
    choice=input('Enter your choice :').lower()
    if choice in choices:
        return choice
    else:
        print("Wrong input")


def computerchoice():
    return np.random.choice(choices)

def winner(user,computerchoice):
    if user==computerchoice:
        return "It is a draw"
    elif (user=='rock' and computerchoice=='paper') or \
            (user=='scissor' and computerchoice=="rock") or \
            (user=="paper" and computerchoice==("scissor")):
        return "You loose, We will get'em next time"
    elif user not in choices:
        return "Wrong input"

    else:
        return "You Won"

def execute():
    print("Let the game begin")
    while True:
        choice=user()
        compchoice=computerchoice()
        print(f"you chose : {choice}")
        print(f"computer chose : {compchoice}")
        print(winner(choice,compchoice))
        repeat=input("You wanna try again? (yes/no):").lower()
        if repeat!="yes":
            print("Thank you for playing")
            break
execute()

def GUI():
    root=tk.Tk()
    