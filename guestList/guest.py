import csv, re

with open ('/home/fahd/Desktop/guest.csv') as f:
	reader = csv.reader(f)
	with open('/home/fahd/Desktop/guest2.csv','w', newline='') as wf:
		writer = csv.writer(wf)
		count_mehndi = 0
		count_barat = 0
		count_valima = 0
		for row in reader:
			#if row[1] == 'N' and row[2] == 'N' and row[3] == 'Y':
				#print (row[0])
			if row[1]=='Y':
				count_mehndi += 1	
			if row[2] == 'Y':
				count_barat += 1
			if row[3] == 'Y':
				count_valima += 1

print ("mehndi = " + str (count_mehndi))
print ("barat = " + str (count_barat))
print ("valima = " + str (count_valima))
