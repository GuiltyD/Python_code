import csv
with open('maomaodoudou.csv','r') as f:
    f_csv = csv.DictReader(f)
    for i in f_csv:
        print(i['name'])
        

