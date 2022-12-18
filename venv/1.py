from datetime import date
import pandas as pd
import numpy as np
import pprint
import csv
import math
import shutil



squat_1rm = 100
bench_1rm = 100
deadlift_1rm = 100
current1rms = [date.today().strftime('%Y-%m-%d'), squat_1rm, bench_1rm, deadlift_1rm]
print(current1rms)