from datetime import date
import pandas as pd
import numpy as np
import pprint
import csv
import math
import shutil

def remove_exercise():
    df = pd.read_csv("exercises_edited.csv", usecols = ['Exercise'])
#    print(df)
    exercise_list = df['Exercise'].tolist()
    pprint.pprint(exercise_list, width=100, compact=True)
    print("Here is the list of exercises you can remove, please type one exactly as displayed below, or type cancel to go back to menu")
    lines = list()
    try:
        removed_exercise= str(input("Which exercise to remove?"))
    except ValueError:
        print('Invalid Please type an exercise as above eg. Crunch, or type cancel')
    else:
        if removed_exercise in exercise_list:
            with open('exercises_edited.csv', 'r') as readFile:
                reader = csv.reader(readFile)
                for row in reader:
                    lines.append(row)
                    for field in row:
                        if field == removed_exercise:
                            lines.remove(row)
            with open('exercises_edited.csv', 'w') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerows(lines)

            print(f"You have removed {removed_exercise}.")
        elif removed_exercise == "cancel":
            pass
        else:
            print('Please type an exercise as displayed in the list, or type cancel')
            remove_exercise()
remove_exercise()

'''lines = list()
    removed_exercise= input("Which exercise to remove?")
    with open('exercises.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == removed_exercise:
                    lines.remove(row)
    with open('exercises_edited.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)

    print(f"Your new exercise list is:")

    ex = pd.read_csv('exercises_edited.csv',  header=None).groupby([0])[1].agg(list).to_dict()
    pprint.pprint(ex)'''
