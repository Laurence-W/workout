from datetime import date
import pandas as pd
import numpy as np
import pprint
import csv
import math
import shutil

def generate_workout():
    upper_elements = ['Biceps', 'Triceps','Backhorizontal', 'Backtraps', 'Backvertical', 'Chest', 'Chestfly', 'Shoulders', 'Frontdelts', 'Sidedelts', 'Reardelts']
    lower_elements = ['Legsquads', 'Legshams', 'Legsglutes', 'Legscalves', 'Abdominals']
    push_elements = ['Chest', 'Chestfly', 'Shoulders', 'Frontdelts', 'Sidedelts', 'Triceps']
    pull_elements = ['Backhorizontal', 'Backtraps', 'Backvertical', 'Biceps', 'Reardelts']
    #ex = pd.read_csv('exercises_edited.csv',  header=None).groupby([0])[1].agg(list).to_dict()
    reps = [5,8,10,12,15,20]
    days = 0
    mode = 0
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

        elif mode == 2:
            print("Medium Mode Activated.")
            sets = 3

        elif mode == 3:
            print("Hard Mode? Let's go!")
            sets = 4

        else:
            print("That is not a valid range. Please input an integer eg. 2 for Medium")

    def day_upper():
        ex = pd.read_csv('exercises_edited.csv',  header=None).groupby([0])[1].agg(list).to_dict()
        for i in upper_elements:
            print(f"{i}: {np.random.choice(ex[i],1,replace=False)} {sets} x {np.random.choice(reps,1,replace=False)}")

    def day_lower():
        ex = pd.read_csv('exercises_edited.csv',  header=None).groupby([0])[1].agg(list).to_dict()
        for i in lower_elements:
            print(f"{i}: {np.random.choice(ex[i],1,replace=False)} {sets} x {np.random.choice(reps,1,replace=False)}")

    def day_push():
        ex = pd.read_csv('exercises_edited.csv',  header=None).groupby([0])[1].agg(list).to_dict()
        for i in push_elements:
            print(f"{i}: {np.random.choice(ex[i],1,replace=False)} {sets} x {np.random.choice(reps,1,replace=False)}")

    def day_pull():
        ex = pd.read_csv('exercises_edited.csv',  header=None).groupby([0])[1].agg(list).to_dict()
        for i in pull_elements:
            print(f"{i}: {np.random.choice(ex[i],1,replace=False)} {sets} x {np.random.choice(reps,1,replace=False)}")
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
#generate_workout()

def input_1rms():
    squat_1rm = float(input("Please enter your current Squat One-rep Max:"))
    bench_1rm = float(input("Please enter your current Bench Press One-rep Max:"))
    deadlift_1rm = float(input("Please enter your current Deadlift One-rep Max:"))
    current1rms = [date.today(), squat_1rm, bench_1rm, deadlift_1rm]
    print(f"New one-rep max entry: {current1rms}")
    with open("onerms.csv", 'a+', newline='') as write_obj:
        csv_writer = csv.writer(write_obj)
        csv_writer.writerow(current1rms)
    #return current1rms
#input_1rms()

def show_1rms():
    n = int(input("How many recent one-rep maxes would you like to see?"))
    df = pd.read_csv("onerms.csv", usecols = ['Date','Squat','Bench','Deadlift'])
    df['Date'] = df['Date'].astype('datetime64[ns]')
    print(df.tail(n))
#show_1rms()

def calculate_ipf_points():
    df = pd.read_csv("onerms.csv", usecols = ['Date','Squat','Bench','Deadlift'])
    totalscore = df.iloc[-1].tolist()
    bodyweight = float(input("Please enter your bodyweight in kilograms as a number (eg. 92.35)"))
    gender = input("Please tell me your gender (Type m or f):")
    if gender == "m":
        A = 310.67
        B = 857.785
        C = 53.216
        D = 147.0835
        result=(sum(totalscore[1:4]))
        print(result)
        ipf_points = 500 + 100 * ((result - (A * math.log(bodyweight) - B)) / (C * math.log(bodyweight) - D))
        print(ipf_points)
    elif gender == "f":
        A = 125.1435
        B = 228.03
        C = 34.5246
        D = 86.8301
        result=(sum(totalscore[1:4]))
        print(result)
        ipf_points = 500 + 100 * ((result - (A * math.log(bodyweight) - B)) / (C * math.log(bodyweight) - D))
        print(ipf_points)
#calculate_ipf_points()

def show_exercise_list():
    ex = pd.read_csv('exercises_edited.csv',  header=None).groupby([0])[1].agg(list).to_dict()
    pprint.pprint(ex)
#show_exercise_list()

def remove_exercise():
    lines = list()
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
    pprint.pprint(ex)
#remove_exercise()

def reset_exercises():
    original = r'exercises.csv'
    target = r'exercises_edited.csv'

    shutil.copyfile(original, target)
    print("Exercise List has been reset to original state.")
#reset_exercises()

def main_menu():
    while True:
        print("Welcome to the workout app!")
        print("Please choose what you would like to do:")
        print("[1] Generate a workout.")
        print("[2] Input my current one-rep max for Squat, Bench, and Deadlift.")
        print("[3] See some of my recent one-rep max entries.")
        print("[4] Calculate my IPF score (Powerlifting Benchmark).")
        print("[5] See the current exercise choices used for workouts.")
        print("[6] Remove an exercise I don't want.")
        print("[7] Reset the exercise list to original state.")
        print("[8] Quit the app.")

        try:
            menu_choice = int(input("Enter a value from 1 to 8."))
        except ValueError:
           print("Invalid option entry. Enter a value from 1 to 8")
           continue
        if not menu_choice in range(1,9):
            print("Invalid option entry. Enter a value from 1 to 8")
            continue
        if menu_choice == 1:
            generate_workout()
            try:
                input("Press enter to continue")
            except SyntaxError:
                pass
        if menu_choice == 2:
            input_1rms()
            try:
                input("Press enter to continue")
            except SyntaxError:
                pass
        if menu_choice == 3:
            show_1rms()
            try:
                input("Press enter to continue")
            except SyntaxError:
                pass
        if menu_choice == 4:
            calculate_ipf_points()
            try:
                input("Press enter to continue")
            except SyntaxError:
                pass
        if menu_choice == 5:
            show_exercise_list()
            try:
                input("Press enter to continue")
            except SyntaxError:
                pass
        if menu_choice == 6:
            remove_exercise()
            try:
                input("Press enter to continue")
            except SyntaxError:
                pass
        if menu_choice == 7:
            reset_exercises()
            try:
                input("Press enter to continue")
            except SyntaxError:
                pass
        if menu_choice == 8:
            exit()
        return menu_choice

menu_choice = main_menu()
while menu_choice != 8:
    menu_choice = main_menu()