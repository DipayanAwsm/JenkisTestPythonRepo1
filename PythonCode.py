import pandas as pd 

import argparse
import os

import datetime
#################################
fileType =".csv"
#################################
today = datetime.date.today()

year = today.year
month = today.strftime("%B")   # Full month name
day = today.strftime("%A")     # Full day name
week_number = today.isocalendar()[1]
####################################
monthFile = month+"_"+str(year)+fileType
dayFile = "week-"+str(week_number)+"_"+str(year)+fileType

####################################
# Step 1: Folder path
output = "output"
if not os.path.exists(output):
    os.makedirs(output)


# Step 2: File path inside the folder
file_pathMonth = os.path.join(output, monthFile)
file_pathDay = os.path.join(output, dayFile)



####################################
print("Year:", year)
print("Month:", month)
print("Day:", day)
print("Week Number:", week_number)
###############################
parser = argparse.ArgumentParser(description="Process some inputs.")
parser.add_argument("--inputFile", default="inputFile.csv", help="Your age")
args = parser.parse_args()


inputFileLocation = args.inputFile
print("file is written at: ",today)

df = pd.read_csv(inputFileLocation)
###########################
df.to_csv(file_pathMonth)
df.to_csv(file_pathDay)
