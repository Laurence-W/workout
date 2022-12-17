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

'''def removeexercise():
    removed_exercise = str(input("Please type out the exercise to remove:"))
    with open('/home/laurence/test/exercises.csv', 'rb') as inp, open('/home/laurence/test/exercises_edited.csv', 'wb') as out:
        writer = csv.writer(out)
        for row in csv.reader(inp):
            if row[1] != removed_exercise:
                writer.writerow(row)
removeexercise()'''

'''def d_avatar():
    filePath = "/home/laurence/test/exercises.csv"
    with open(filePath)	as csvfile:
        reader = csv.DictReader(csvfile)
        
        filePath = "/home/laurence/test/exercises_edited.csv"
        with open(filePath,'w',newline='') as csvfile:
            fieldnames = ['Body Part','Exercise']
            writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
            print("Delete an avatar")
            removed_exercise = input("Which exercise to remove?")
            
        for row in reader:
            if removed_exercise != row['Exercise']:
                writer.writerow(row) ; # write all non-matching rows
            else:
                print("Avatar Record Deleted") # nothing to write
d_avatar()'''

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

    print(f"Your new exercise lise is:")

    ex = pd.read_csv('/home/laurence/test/exercises_edited.csv',  header=None).groupby([0])[1].agg(list).to_dict()
    pprint.pprint(ex)
removeexercise()