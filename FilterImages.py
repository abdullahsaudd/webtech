import glob, os, shutil, csv
dest1=("D:/Diabetic_Retinopathy/Composite_Dataset_Filtered/ONE")
dest2=("D:/Diabetic_Retinopathy/Composite_Dataset_Filtered/TWO")
dest3=("D:/Diabetic_Retinopathy/Composite_Dataset_Filtered/THREE")
dest4=("D:/Diabetic_Retinopathy/Composite_Dataset_Filtered/FOUR")
dest5=("D:/Diabetic_Retinopathy/Composite_Dataset_Filtered/DEFECTFREE")
os.chdir("D:/Diabetic_Retinopathy/Composite_Dataset")
with open('D:/Diabetic_Retinopathy/Dataset/trainLabels.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',') 
	for col in readCSV:
		if col[1] == '1':
			temp = col[0]+'.jpeg'
			print(temp)
			for file in glob.glob(temp):
				shutil.copy2(temp,dest1)
		elif col[1] == '2':
			temp = col[0] + '.jpeg'
			print(temp)
			for file in glob.glob(temp): 
				shutil.copy2(temp,dest2)
		elif col[1] == '3':
			temp = col[0] + '.jpeg'
			print(temp)
			for file in glob.glob(temp):
				shutil.copy2(temp,dest3)
		elif col[1] == '4':
			temp = col[0] + '.jpeg'
			print(temp)
			for file in glob.glob(temp):
				shutil.copy2(temp,dest4)
		elif col[1] == '0':
			temp = col[0] + '.jpeg'
			print(temp)
			for file in glob.glob(temp):
				shutil.copy2(temp,dest5) 
		else:
			print("File Not Found")