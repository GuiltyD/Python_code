import csv

header = ['name','gender','age','hobby']
rows =[('代书豪','男','24','grogram'),
        ('周雨薇','女','24','explode'),
        ]
with open('maomaodoudou.csv','w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(header)
    f_csv.writerows(rows)
