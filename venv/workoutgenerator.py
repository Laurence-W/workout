from datetime import date
from csv import writer
import pandas as pd
import numpy as np

if __name__ == "__main__":
    days = 0
    mode = 0
    while days not in range(3,7):
        days = int(input("How many days would you like to train this week?\n\
        3  = Push, Pull, Legs\n\
        4  = Upper, Lower, Upper, Lower\n\
        5  = Upper, Lower, Push, Pull, Legs\n\
        6  = Push, Pull, Legs, Push, Pull, Legs\n\
        Your choice:"
        ))
        if days not in range(3,7):
            print("That is not a valid range. Please input an integer eg. 5")
    print(f"You have chosen to train {days} times this week")

    while mode not in range(1,4):
        mode = int(input("What difficulty level would you like for this workout?\n\
        1  = Easy\n\
        2  = Medium\n\
        3  = Hard\n\
        Your choice? "))

        if mode == 1:
            print("Easy Mode Activated.")
            #eg.start_workout(type_of_workout, intensity, number_of_exercises, workout_interval)

        elif mode == 2:
            print("Just a medium day? Alright.")
            #eg.start_workout(type_of_workout, intensity, number_of_exercises, workout_interval)

        elif mode == 3:
            print("You want a challenge? Hard Mode let's go!")
            #eg.start_workout(type_of_workout, intensity, number_of_exercises, workout_interval)

        else:
            print("That is not a valid range. Please input an integer eg. 2 for Medium")
