import cv2 , glob , numpy
def scaleRadius(img, scale) :
    x=img [ img . shape [ 0 ] / 2 , : , : ] . sum ( 1 )
    r=(x>x.mean()/10).sum()/2
    s=scale*1.0/r
    return cv2.resize(img,(0,0),fx=s,fy=s)

scale =300
for f in glob.glob("D:/Diabetic_Retinopathy/Test_Dataset/*.jpeg"):
    try:
        a=cv2.imread(f)
        a=scaleRadius(a,scale)
        a=cv2.addWeighted(a,4,cv2.GaussianBlur(a,(0,0),scale/30),-4,128)
        b=numpy.zeros(a.shape)
        cv2.circle(b,(a.shape[1]/2,a.shape[0]/2),int(scale*0.9),(1,1,1),-1,8,0)
        a=a*b+128*(1-b)
        cv2.imwrite(str(scale)+"_"+f,a)
    except:
        print (f)