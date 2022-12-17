from datetime import date
import pandas as pd
import numpy as np
import pprint
import csv
from numpy.random import choice
#test
#if __name__ == "__main__":
ex = pd.read_csv('exercises_edited.csv',  header=None).groupby([0])[1].agg(list).to_dict()
reps = [5,8,10,12,15,20]
days = 0
mode = 0
sets = 0

def day_upper():
    print(f"Biceps: {choice(ex['biceps'],1,replace=False)} {sets} x {choice(reps,1,replace=False)}")
    print(f"Triceps: {choice(ex['triceps'],1,replace=False)} {sets} x {choice(reps,1,replace=False)}")
    print(f"Back Horizontal: {choice(ex['backhorizontal'],1,replace=False)} {sets} x {choice(reps,1,replace=False)}")
    print(f"Back traps: {choice(ex['backtraps'],1,replace=False)} {sets} x {choice(reps,1,replace=False)}")
    print(f"Back Vertical: {choice(ex['backvertical'],1,replace=False)} {sets} x {choice(reps,1,replace=False)}")
    print(f"Chest: {choice(ex['chest'],1,replace=False)} {sets} x {choice(reps,1,replace=False)}")
    print(f"Chest Fly: {choice(ex['chestfly'],1,replace=False)} {sets} x {choice(reps,1,replace=False)}")
    print(f"Shoulders Front: {choice(ex['frontdelts'],1,replace=False)} {sets} x {choice(reps,1,replace=False)}")
    print(f"Shoulders Rear: {choice(ex['reardelts'],1,replace=False)} {sets} x {choice(reps,1,replace=False)}")
    print(f"Shoulders: {choice(ex['shoulders'],1,replace=False)} {sets} x {choice(reps,1,replace=False)}")
    print(f"Shoulders Sides: {choice(ex['sidedelts'],1,replace=False)} {sets} x {choice(reps,1,replace=False)}")

def day_lower():
    print(f"Legs Quads: {choice(ex['legsquads'],1,replace=False)} {sets} x {choice(reps,1,replace=False)}")
    print(f"Legs Hams: {choice(ex['legshams'],1,replace=False)} {sets} x {choice(reps,1,replace=False)}")
    print(f"Legs Glutes: {choice(ex['legsglutes'],1,replace=False)} {sets} x {choice(reps,1,replace=False)}")
    print(f"Legs Calves: {choice(ex['legscalves'],1,replace=False)} {sets} x {choice(reps,1,replace=False)}")
    print(f"Abdominals: {choice(ex['abdominals'],1,replace=False)} {sets} x {choice(reps,1,replace=False)}")

def day_push():
    print(f"Chest: {choice(ex['chest'],1,replace=False)} {sets} x {choice(reps,1,replace=False)}")
    print(f"Chest Fly: {choice(ex['chestfly'],1,replace=False)} {sets} x {choice(reps,1,replace=False)}")
    print(f"Shoulders Front: {choice(ex['frontdelts'],1,replace=False)} {sets} x {choice(reps,1,replace=False)}")
    print(f"shoulders: {choice(ex['shoulders'],1,replace=False)} {sets} x {choice(reps,1,replace=False)}")
    print(f"Shoulders Side: {choice(ex['sidedelts'],1,replace=False)} {sets} x {choice(reps,1,replace=False)}")
    print(f"Triceps: {choice(ex['triceps'],1,replace=False)} {sets} x {choice(reps,1,replace=False)}")

def day_pull():
    print(f"Back Horizontal: {choice(ex['backhorizontal'],1,replace=False)} {sets} x {choice(reps,1,replace=False)}")
    print(f"Back Traps: {choice(ex['backtraps'],1,replace=False)} {sets} x {choice(reps,1,replace=False)}")
    print(f"Back Vertical: {choice(ex['backvertical'],1,replace=False)} {sets} x {choice(reps,1,replace=False)}")
    print(f"Biceps: {choice(ex['biceps'],1,replace=False)} {sets} x {choice(reps,1,replace=False)}")
    print(f"Shoulders Rear: {choice(ex['reardelts'],1,replace=False)} {sets} x {choice(reps,1,replace=False)}")


#ensure days worked out that week is valid
while not 3 <= days <= 6:
    days = int(input("How many days would you like to train this week?\n\
    3  = Push, Pull, Legs\n\
    4  = Upper, Lower, Upper, Lower\n\
    5  = Upper, Lower, Push, Pull, Legs\n\
    6  = Push, Pull, Legs, Push, Pull, Legs\n\
    Your choice:"
    ))
    if not 3 <= days <= 6:
        print("That is not a valid range. Please input an integer eg. 5")
print(f"You have chosen to train {days} times this week")

while not 1 <= mode <= 3:
    mode = int(input("What difficulty level would you like for this week?\n\
    1  = Easy\n\
    2  = Medium\n\
    3  = Hard\n\
    Your choice? "))

    if mode == 1:
        print("Easy Mode Activated.")
        sets = 2
        #eg.start_workout(type_of_workout, intensity, number_of_exercises, workout_interval)

    elif mode == 2:
        print("Medium Mode Activated.")
        sets = 3
        #eg.start_workout(type_of_workout, intensity, number_of_exercises, workout_interval)

    elif mode == 3:
        print("Hard Mode? Let's go!")
        sets = 4
        #eg.start_workout(type_of_workout, intensity, number_of_exercises, workout_interval)

    else:
        print("That is not a valid range. Please input an integer eg. 2 for Medium")

if days == 3:
    print("\n Day 1 Push:")
    day_push()
    print("\n Day 2  Pull:")
    day_pull()
    print("\n Day 3 Lower:")
    day_lower()
elif days == 4:
    print("\n Day 1 Upper:")
    day_upper()
    print("\n Day 2 Lower:")
    day_lower()
    print("\n Day 3 Upper:")
    day_upper()
    print("\n Day 4 Lower:")
    day_lower()
elif days == 5:
    print("\n Day 1 Upper:")
    day_upper()
    print("\n Day 2 Lower:")
    day_lower()
    print("\n Day 3 Push:")
    day_push()
    print("\n Day 4 Pull:")
    day_pull()
    print("\n Day 5 Lower:")
    day_lower()
elif days == 6:
    print("\n Day 1 Push:")
    day_push()
    print("\n Day 2 Pull:")
    day_pull()
    print("\n Day 3 Lower:")
    day_lower()
    print("\n Day 4 Push:")
    day_push()
    print("\n Day 5 Pull:")
    day_pull()
    print("\n Day 6 Lower:")
    day_lower()