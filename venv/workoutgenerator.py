from datetime import date
import pandas as pd
import numpy as np
import pprint
import csv
import math
import shutil

def generate_workout():
#define variables needed for workout generation and read exercise list from csv to dict.
    ex = pd.read_csv('exercises_edited.csv',  header=None).groupby([0])[1].agg(list).to_dict()
    upper_elements = ['Biceps', 'Triceps','Backhorizontal', 'Backtraps', 'Backvertical', 'Chest', 'Chestfly', 'Shoulders', 'Frontdelts', 'Sidedelts', 'Reardelts']
    lower_elements = ['Legsquads', 'Legshams', 'Legsglutes', 'Legscalves', 'Abdominals']
    push_elements = ['Chest', 'Chestfly', 'Shoulders', 'Frontdelts', 'Sidedelts', 'Triceps']
    pull_elements = ['Backhorizontal', 'Backtraps', 'Backvertical', 'Biceps', 'Reardelts']
    reps = [5,8,10,12,15,20]

#ensure days worked out is input validly as integer.
    while True:
        try:
            days = int(input("How many days would you like to train this week?\n\
        3  = Push, Pull, Legs\n\
        4  = Upper, Lower, Upper, Lower\n\
        5  = Upper, Lower, Push, Pull, Legs\n\
        6  = Push, Pull, Legs, Push, Pull, Legs\n\
        Your choice:"
        ))
        except ValueError:
            print("Invalid input. Please enter the number of days only eg. 4")
        else:
            if 3 <= days <= 6:
                print(f"You have chosen to train {days} times this week")
                break
            else:
                print("Number out of range. Enter a number from 3 to 6)")

#ensure difficulty mode is input validly as integer.
    while True:
        try:
            mode = int(input("What difficulty level would you like for this week?\n\
                            1  = Easy\n\
                            2  = Medium\n\
                            3  = Hard\n\
                            Your choice? "))

        except ValueError:
            print("Invalid input. Please enter a number only eg. 2")
        else:
            if mode == 1:
                print("Easy Mode Activated.")
                sets = 2
                break
            elif mode == 2:
                print("Medium Mode Activated.")
                sets = 3
                break
            elif mode == 2:
                print("Medium Mode Activated.")
                sets = 3
                break
            elif mode == 3:
                print("Hard Mode? Let's go!")
                sets = 4
                break
            else:
                print("Number out of range. Enter a number from 1 to 3.")

#define sub-functions to generate exercises for each category of day. eg push, pull, etc.
# & ex.keys() ensures that no error occurs if a user has deleted all exercises within a Body Part
    def day_upper():
        for i in upper_elements & ex.keys():
            print(f"{i}: {np.random.choice(ex[i],1,replace=False)} {sets} x {np.random.choice(reps,1,replace=False)}")

    def day_lower():
        for i in lower_elements & ex.keys():
            print(f"{i}: {np.random.choice(ex[i],1,replace=False)} {sets} x {np.random.choice(reps,1,replace=False)}")

    def day_push():
        for i in push_elements & ex.keys():
            print(f"{i}: {np.random.choice(ex[i],1,replace=False)} {sets} x {np.random.choice(reps,1,replace=False)}")

    def day_pull():
        for i in pull_elements & ex.keys():
            print(f"{i}: {np.random.choice(ex[i],1,replace=False)} {sets} x {np.random.choice(reps,1,replace=False)}")

#run sub-functions based on days input by user.
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

def input_1rms():
    while True:
        try:
            squat_1rm = float(input("Please enter your current Squat One-rep Max in kilograms:"))
        except ValueError:
            print("Invalid input. Please enter a number eg. 147.25")
        else:
            if 1 <= squat_1rm <= 1000:
                break
            else:
                print("Number out of range. Enter a number from 1 to 1000)")

    while True:
        try:
            bench_1rm = float(input("Please enter your current Bench One-rep Max in kilograms:"))
        except ValueError:
            print("Invalid input. Please enter a number eg. 147.25")
        else:
            if 1 <= bench_1rm <= 1000:
                break
            else:
                print("Number out of range. Enter a number from 1 to 1000)")

    while True:
        try:
            deadlift_1rm = float(input("Please enter your current Deadlift One-rep Max in kilograms:"))
        except ValueError:
            print("Invalid input. Please enter a number eg. 147.25")
        else:
            if 1 <= deadlift_1rm <= 1000:
                break
            else:
                print("Number out of range. Enter a number from 1 to 1000)")

    current1rms = [date.today().strftime('%Y-%m-%d'), squat_1rm, bench_1rm, deadlift_1rm]
    print(f"New one-rep max entry: {current1rms}")
    with open("onerms.csv", 'a+', newline='') as write_obj:
        csv_writer = csv.writer(write_obj)
        csv_writer.writerow(current1rms)

def show_1rms():
    df = pd.read_csv("onerms.csv", usecols = ['Date','Squat','Bench','Deadlift'])
    while True:
        try:
            n = int(input("How many recent one-rep maxes would you like to see? (Enter a number from 1 to 20)"))
        except ValueError:
            print("Invalid input. Please enter a number eg. 5")
        else:
            if 1 <= n <= 20:
                df['Date'] = df['Date'].astype('datetime64[ns]')
                print(df.tail(n))
                break
            else:
                print("Number out of range. Enter a number from 1 to 20)")
        


def calculate_ipf_points():
    df = pd.read_csv("onerms.csv", usecols = ['Date','Squat','Bench','Deadlift'])
    totalscore = df.iloc[-1].tolist()
    #accept bodyweight input as float number type only.
    try:
        bodyweight = float(input("Please enter your bodyweight in kilograms as a number (eg. 92.35)"))
    except ValueError:
        bodyweight = float(input("Invalid entry. Please enter your bodyweight in kilograms as a number (eg. 92.35)"))

    while True:
        gender = input("Please tell me your gender (Type male or female):")
        if gender.lower() == "male":
            A = 310.67
            B = 857.785
            C = 53.216
            D = 147.0835
            result=(sum(totalscore[1:4]))
            ipf_points = 500 + 100 * ((result - (A * math.log(bodyweight) - B)) / (C * math.log(bodyweight) - D))
            print(f"The IPF points score for a {bodyweight}kg male with a Squat, Bench, Deadlift total of {result}kg is {round(ipf_points, 3)}.")
            break
        elif gender.lower() == "female":
            A = 125.1435
            B = 228.03
            C = 34.5246
            D = 86.8301
            result=(sum(totalscore[1:4]))
            ipf_points = 500 + 100 * ((result - (A * math.log(bodyweight) - B)) / (C * math.log(bodyweight) - D))
            print(f"The IPF points score for a {bodyweight}kg female with a Squat, Bench, Deadlift total of {result}kg is {round(ipf_points, 3)}.")
            break
        else:
            print("Invalid entry. Please enter gender as male or female.")
            continue

def show_exercise_list():
    ex = pd.read_csv('exercises_edited.csv',  header=None).groupby([0])[1].agg(list).to_dict()
    pprint.pprint(ex)

def remove_exercise():
    df = pd.read_csv("exercises_edited.csv", usecols = ['Exercise'])
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

def reset_exercises():
    #function copies original exercise list over the edited version using shutil copyfile function.
    original = r'exercises.csv'
    target = r'exercises_edited.csv'

    shutil.copyfile(original, target)
    print("Exercise List has been reset to original state.")

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