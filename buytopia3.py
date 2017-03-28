import csv
file_obj = open("Base Data.csv",'r')
read_csv = csv.reader(file_obj, delimiter=',')
file_object2 = open("Output3.csv","w+")
fileWriter = csv.writer(file_object2)
fileWriter.writerow(["LastOpenDate","#OfUsers","Total Revenue Generated"])

Dates=[]
count_users = 0
total_revenue = 0
for line in read_csv:
	if line[1] not in Dates and line[1]!='Last Open Date':
		Dates.append(line[1])
		
file_obj.close()



for date in Dates:

	file_obj = open("Base Data.csv",'r')
	read_csv = csv.reader(file_obj, delimiter=',')	
	for line in read_csv:
		if date == line[1]:
			count_users=count_users+1
			dollar_amount = line[2].strip('$')
			dollar_amount = dollar_amount.replace('"','')
			dollar_amount = dollar_amount.replace('.00','')
			dollar_amount = dollar_amount.replace(',','')
			print (dollar_amount)
			total_revenue = total_revenue+int(dollar_amount)

	fileWriter.writerow([date,count_users,total_revenue])
	count_users = 0
	total_revenue = 0
	
file_obj.close()
file_object2.close()