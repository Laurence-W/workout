import pandas as pd
import pprint
from tempfile import NamedTemporaryFile
import shutil
import csv

def showexerciselist():
    ex = pd.read_csv('/home/laurence/test/exercises.csv',  header=None).groupby([0])[1].agg(list).to_dict()
    pprint.pprint(ex)
    #for x,y in (line.rstrip().split(',') for line in f):
        #exercises.setdefault(y, []).append(x)
showexerciselist()

'''def removeexercise():
    removed_exercise = str(input("Please type out the exercise to remove:"))
    filename = '/home/laurence/test/exercises.csv'
    tempfile = NamedTemporaryFile('w+t', newline='', delete=False)

    with open(filename, 'r', newline='') as csvFile, tempfile:
        reader = csv.reader(csvFile, delimiter=',')
        writer = csv.writer(tempfile, delimiter=',')

        for row in reader:
            if not any(removed_exercise in row):
                writer.writerow(row)

    shutil.move(tempfile.name, filename)
removeexercise()'''

def removeexercise():
    removed_exercise = input("Please type out the exercise to remove:")
    with open('/home/laurence/test/exercises.csv', 'rb') as inp, open('/home/laurence/test/exercises_edited.csv', 'wb') as out:
        writer = csv.writer(out)
        for row in csv.reader(inp):
            if row[1] != removed_exercise:
                writer.writerow(row)
removeexercise()