import glob, os, shutil, csv
dest1l=("D:/Diabetic_Retinopathy/Composite_Dataset_Filtered/ONE/LEFT")
dest1r=("D:/Diabetic_Retinopathy/Composite_Dataset_Filtered/ONE/RIGHT")
dest2l=("D:/Diabetic_Retinopathy/Composite_Dataset_Filtered/TWO/LEFT")
dest2r=("D:/Diabetic_Retinopathy/Composite_Dataset_Filtered/TWO/RIGHT")
dest3l=("D:/Diabetic_Retinopathy/Composite_Dataset_Filtered/THREE/LEFT")
dest3r=("D:/Diabetic_Retinopathy/Composite_Dataset_Filtered/THREE/RIGHT")
dest4l=("D:/Diabetic_Retinopathy/Composite_Dataset_Filtered/FOUR/LEFT")
dest4r=("D:/Diabetic_Retinopathy/Composite_Dataset_Filtered/FOUR/RIGHT")
dest0l=("D:/Diabetic_Retinopathy/Composite_Dataset_Filtered/DEFECTFREE/LEFT")
dest0r=("D:/Diabetic_Retinopathy/Composite_Dataset_Filtered/DEFECTFREE/RIGHT")
print("changing current directory...")
os.chdir("D:/Diabetic_Retinopathy/Composite_Dataset")
print("starting to read csv file...")
with open('D:/Diabetic_Retinopathy/Scripts/trainLabels.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for col in readCSV:
        fname = col[0].split("_")
        img_name = col[0] + '.jpeg'
        img_dir = fname[-1] 
#        print(img_name+"---"+img_dir)
        if col[1] == '0' and img_dir == 'left':
            for file in glob.glob(img_name):
                shutil.copy2(img_name,dest0l)
        elif col[1] == '0' and img_dir == 'right':
            for file in glob.glob(img_name):
                shutil.copy2(img_name,dest0r)
        elif col[1] == '1' and img_dir == 'left':
            for file in glob.glob(img_name):
                shutil.copy2(img_name,dest1l)
        elif col[1] == '1' and img_dir == 'right':
            for file in glob.glob(img_name):
                shutil.copy2(img_name,dest1r)
        elif col[1] == '2' and img_dir == 'left':
            for file in glob.glob(img_name):
                shutil.copy2(img_name,dest2l)
        elif col[1] == '2' and img_dir == 'right':
            for file in glob.glob(img_name):
                shutil.copy2(img_name,dest2r)
        elif col[1] == '3' and img_dir == 'left':
            for file in glob.glob(img_name):
                shutil.copy2(img_name,dest3l)
        elif col[1] == '3' and img_dir == 'right':
            for file in glob.glob(img_name):
                shutil.copy2(img_name,dest3r)
        elif col[1] == '4' and img_dir == 'left':
            for file in glob.glob(img_name):
                shutil.copy2(img_name,dest4l)
        elif col[1] == '4' and img_dir == 'right':
            for file in glob.glob(img_name):
                shutil.copy2(img_name,dest4r)
        else:
            print("Invalid Input")
print("filteration complete...")