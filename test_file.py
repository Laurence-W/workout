import pandas as pd
import math
import csv
import shutil

def calculate_ipf_points(gender, bodyweight):
    df = pd.read_csv("onerms_test.csv", usecols = ['Date','Squat','Bench','Deadlift'])
    totalscore = df.iloc[-1].tolist()
    if gender == "male":
        A = 310.67
        B = 857.785
        C = 53.216
        D = 147.0835
        result=(sum(totalscore[1:4]))
        ipf_points = round(500 + 100 * ((result - (A * math.log(bodyweight) - B)) / (C * math.log(bodyweight) - D)), 2)
        return ipf_points
    elif gender == "female":
        A = 125.1435
        B = 228.03
        C = 34.5246
        D = 86.8301
        result=(sum(totalscore[1:4]))
        ipf_points = round(500 + 100 * ((result - (A * math.log(bodyweight) - B)) / (C * math.log(bodyweight) - D)), 2)
        return ipf_points

#testing value assuming user correctly enters "male" gender and 100 bodyweight
def test_calculate_ipf_points_male():
    assert calculate_ipf_points("male", 100) == 221.49

#testing value assuming user correctly enters "female" gender and 60 bodyweight
def test_calculate_ipf_points_female():
    assert calculate_ipf_points("female", 60) == 528.7

#testing point values come from https://www.myfitnesscalculators.com/ipf-points


def reset_exercises():
    #function copies original exercise list over the edited version using shutil copyfile function.
    original = r'exercises.csv'
    target = r'exercises_edited.csv'

    shutil.copyfile(original, target)
    print("Exercise List has been reset to original state.")

def remove_exercise(removed_exercise):
    df = pd.read_csv("exercises_edited.csv", usecols = ['Exercise'])
    exercise_list = df['Exercise'].tolist()
    lines = list()
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

#this test removes an exercise from exercises_edited.csv, then checks if exercise has been removed
def test_remove_exervise():
    remove_exercise('Overhead Tricep Extension')
    #reset_exercises()
    df = pd.read_csv("exercises_edited.csv", usecols = ["Body Part","Exercise"])
    testreset = df.iloc[-1].tolist()
    assert testreset == ['Triceps', 'Dip'] #will only be true if Overhead Tricep Extension has been removed


#this test removes an exercise from exercises_edited.csv, then resets the csv and checks if exercise exists again
def test_reset_exercises_two():
    remove_exercise('Crunch')
    reset_exercises()
    df = pd.read_csv("exercises_edited.csv", usecols = ["Body Part","Exercise"])
    testreset = df.iloc[3].tolist()
    assert testreset == ['Abdominals', 'Crunch']
