import csv

file_object = open("Base Data.csv",'r')
read_csv = csv.reader(file_object, delimiter=',')
substring=""
file_object2 = open("Output2.csv","w+")
fileWriter = csv.writer(file_object2)
fileWriter.writerow(["LastOpenDate","User","Total Revenue Generated"])

for line in read_csv:
	if "7/" in line[1]:
		# substring = substring.strip(" ")
		# substring = line[line.index('7'):line.index('$')-1]
		# #print(substring)
		substring = line[1].split('/')
		if int(substring[1])>20:
			fileWriter.writerow([line[1],line[0],line[2]])
		# new_substring = substring.split('/')
		# if int(new_substring[1])>20:
			# revenue = "$"+line.split('$')[1]
			# print (line.split(',')[0], revenue)

		
	elif "8/" in line[1]:
		# substring = substring.strip(" ")
		# substring = line[line.index('8'):line.index('$')-1]
		# #print(substring)
		substring = line[1].split('/')
		# new_substring = substring.split('/')
		if int(substring[1])<2:
			fileWriter.writerow([line[1],line[0],line[2]])
			# revenue = "$"+line.split('$')[1]
			# print (line.split(',')[0], revenue)
		
file_object.close()
file_object2.close()