import pandas as pd
import pprint
import csv
import shutil

def showexerciselist():
    ex = pd.read_csv('/home/laurence/test/exercises.csv',  header=None).groupby([0])[1].agg(list).to_dict()
    pprint.pprint(ex)
    #for x,y in (line.rstrip().split(',') for line in f):
        #exercises.setdefault(y, []).append(x)
showexerciselist()

def removeexercise():
    lines = list()
    members= input("Which exercise to remove?")
    with open('/home/laurence/test/exercises.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == members:
                    lines.remove(row)
    with open('/home/laurence/test/exercises_edited.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)

    print(f"Your new exercise list is:")

    ex = pd.read_csv('/home/laurence/test/exercises_edited.csv',  header=None).groupby([0])[1].agg(list).to_dict()
    pprint.pprint(ex)
#removeexercise()

def reset_exercises():
    original = r'/home/laurence/test/exercises.csv'
    target = r'/home/laurence/test/exercises_edited.csv'

    shutil.copyfile(original, target)
reset_exercises()