from datetime import date
from csv import writer
import pandas as pd
import numpy as np
import math

today = date.today()
#print(today)

def input_1rms():
    squat_1rm = float(input("Please enter your current Squat One-rep Max:"))
    bench_1rm = float(input("Please enter your current Bench Press One-rep Max:"))
    deadlift_1rm = float(input("Please enter your current Deadlift One-rep Max:"))
    current1rms = [today, squat_1rm, bench_1rm, deadlift_1rm]
    with open("onerms.csv", 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(current1rms)
    return current1rms
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
    bodyweight = float(input("Please enter your bodyweight inkilograms as a number (eg. 92.35)"))
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
calculate_ipf_points()