import os
import csv

acc_lst = []

for i in os.listdir('model/32/InceptionV3'):
    i.replace('.h5' , '')
    i = i.split('-')
    i = i[2]
    acc_lst.append(i)

print(acc_lst)

with open(32_inception, 'wb') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter = ',')
    for i in acc_lst:
        csvwriter.writerow(i)
