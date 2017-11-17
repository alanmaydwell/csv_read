import csv

with open('test_data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print row
        
        
#There is a csv module but doesn't seem worth it
test_data = []
with open('test_data.csv', 'r') as csvfile:
    for line_no, line in enumerate(csvfile):
            
        line_data = line.rstrip("\r\n").split(",")
        if line_no == 0:
            keys = line_data
        else:
            temp = {k:v for k,v in zip(keys,line_data)}
            test_data.append(temp)

print test_data