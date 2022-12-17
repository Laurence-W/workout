from datetime import date
from csv import writer
import pandas as pd
import numpy as np


today = date.today()
print(today)

def input_1rms():
    squat_1rm = float(input("Please enter your current Squat One-rep Max:"))
    bench_1rm = float(input("Please enter your current Bench Press One-rep Max:"))
    deadlift_1rm = float(input("Please enter your current Deadlift One-rep Max:"))
    current1rms = [today, squat_1rm, bench_1rm, deadlift_1rm]
    with open("onerms.csv", 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(current1rms)
    return current1rms
input_1rms()

def show_1rms():
    n = int(input("How many recent one-rep maxes would you like to see?"))
    df = pd.read_csv("onerms.csv", usecols = ['Date','Squat','Bench','Deadlift'])
    df['Date'] = df['Date'].astype('datetime64[ns]')
    print(df.tail(n))
show_1rms()