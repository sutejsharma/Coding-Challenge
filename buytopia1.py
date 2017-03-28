import csv
file_read = open("Base Data.csv",'r')
A=[]
file_object2 = open("Output1.csv","w+")
fileWriter = csv.writer(file_object2)
fileWriter.writerow(["LastOpenDate","User"])
read_csv = csv.reader(file_read, delimiter=',')
for line in read_csv:
	if "7/16/2016" in line or "07-16-2016" in line:
		fileWriter.writerow([line[1],line[0]])
file_read.close()
file_object2.close()