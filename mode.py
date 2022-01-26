import csv
from collections import Counter
with open ("height-weight.csv") as f:
    reader=csv.reader(f)
    file_data=list(reader)
file_data.pop(0)
new_data=[]
for i in range(len(file_data)):
    n_numb=file_data[i][1]
    new_data.append(float(n_numb))
data=Counter(new_data)
mode_for_range={
    "50-60":0,
    "60-70":0,
    "70-80":0


}
for height,occurance in data.items():
    if 50 < float(height) < 60:
        mode_for_range["50-60"]+=occurance
    
    elif 60 < float(height) < 70:
        mode_for_range["60-70"]+=occurance
    elif 70 < float(height) < 80:
        mode_for_range["70-80"]+=occurance
moderange,modeoccurance=0,0
for range,occurance in mode_for_range.items():
    if occurance>modeoccurance:
        moderange,modeoccurance=[int(range.split("-")[0]),int(range.split("-")[1])],occurance
mode=float((moderange[0]+ moderange[1])/2)
print("mode = "+str(mode))