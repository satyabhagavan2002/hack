import cv2,numpy

#cap=cv2.imread("img_0.png")

'''cap1=cv2.cvtColor(cap,cv2.COLOR_BGR2GRAY)
cap2=cv2.GaussianBlur(cap,(7,7),0)

imgcanny=cv2.Canny(cap,50,50)
kernal=numpy.ones((5,5),numpy.uint8)

imgdoalation=cv2.dilate(imgcanny,kernal,iterations=0)


#cv2.imshow("grayimag",cap2)
cv2.imshow("real",imgdoalation)'''
''' 
cv2.imshow("image,",cap)
print(cap.shape)
imgresize=cv2.resize(cap,(1920,480))

imgcroped=cap[0:200,200:500]
cv2.imshow("croped",imgcroped)
cv2.imshow("resize",imgresize)'''


'''img=numpy.zeros((512,512,3),numpy.uint8)
#img[100:200,100:300]=255,0,0
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),5)
cv2.rectangle(img,(100,100),(250,350),(300,50,200),2)
cv2.circle(img,(200,50),40,(150,250,100),5)
cv2.putText(img,"done succesfully",(50,100),cv2.FONT_HERSHEY_COMPLEX,1,(200,300,600),3)

cv2.imshow("imgae",img)'''

'''img=cv2.imread("img_0.png")

width,height=250,350
pts1=numpy.float32([[11,219],[287,188],[154,482],[352,440]])
pts2=numpy.float32([[0,0],[width,0],[0,height],[width,height]])

matrix=cv2.getPerspectiveTransform(pts1,pts2)
imgout=cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("img",imgout)'''
'''
'img=cv2.imread("img_0.png")
img1=cv2.imread("img_1.png")
hor=numpy.hstack((img,img1))
cv2.imshow("hor",hor)
imgver=numpy.vstack((img,img1))
cv2.imshow("fjf",imgver)'''
''' def empty(a):
    pass
cv2.namedWindow("trackbars")
cv2.resizeWindow('trackbars',640,240)
cv2.createTrackbar("hue min","trackbars",0,179,empty)
cv2.createTrackbar("hue max","trackbars",179,179,empty)
cv2.createTrackbar("sat min","trackbars",0,255,empty)
cv2.createTrackbar("sat max","trackbars",255,255,empty)
cv2.createTrackbar("val min","trackbars",0,255,empty)
cv2.createTrackbar("val max","trackbars",255,255,empty)

while True:
    img = cv2.imread("car.png")
    imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("hue min", "trackbars")
    h_max = cv2.getTrackbarPos("hue max", "trackbars")
    s_min = cv2.getTrackbarPos("sat min", "trackbars")
    s_max = cv2.getTrackbarPos("sat max", "trackbars")
    val_min = cv2.getTrackbarPos("val min", "trackbars")
    val_max = cv2.getTrackbarPos("val max", "trackbars")
    print(h_min,h_max,s_min,s_max,val_min,val_max)
    lower=numpy.array([h_min,s_min,val_min])
    upper=numpy.array([h_max,s_max,val_max])

    mask=cv2.inRange(imghsv,lower,upper)
    imgr=cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow("img", img)
    cv2.imshow("hsv", imghsv)
    cv2.imshow("mask", mask)
    cv2.imshow("imgr", imgr)
    cv2.waitKey(1)'''




'''
def getcontours(img):
    cont,hier=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in cont:
        area=cv2.contourArea(cnt)

        if area>500 :
            print(area)
            cv2.drawContours(img1,cnt,-1,(255,0,0),4)
            peri=cv2.arcLength(cnt,True)
            #print(peri)
            aprox=cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(aprox))
            objc=len(aprox)
            objt=''
            if (objc==4):
                objt="REC"

            x,y,w,h=cv2.boundingRect(aprox)
            cv2.rectangle(img1,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.putText(img1,objt,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,0),2)

img=cv2.imread("shapes4.png")
img1=img.copy()
imggrey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgblur=cv2.GaussianBlur(imggrey,(7,7),1)
imgcanney=cv2.Canny(imgblur,50,50)
getcontours(imgcanney)
cv2.imshow("img",img1)
'''

import os
cv2_base_dir = os.path.dirname(os.path.abspath(cv2.__file__))
haar_model = os.path.join(cv2_base_dir, 'data/haarcascade_frontalface_default.xml')

haar_model1 = os.path.join(cv2_base_dir, 'data/haarcascade_eye.xml')

facecascade=cv2.CascadeClassifier(haar_model)
eyecascade=cv2.CascadeClassifier(haar_model1)

img=cv2.VideoCapture(0)
while True:
    img = cv2.imread("img_3.png")
    imggrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = facecascade.detectMultiScale(imggrey, 1.1, 4)
    eye = eyecascade.detectMultiScale(imggrey, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    for (x, y, w, h) in eye:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("img", img)
    cv2.waitKey(0)
'''
cap=cv2.VideoCapture(0)

mycolour=[[0,86,221,18,255,255],  #orange
          [57,76,0,100,255,255],#g
          [100,121,0,119,255,255],#b
          [133,15,171,179,255,255]]#g

mycolourvalues=[[51,153,255],     ##bgr
                [0,255,0],#g
                [255,0,0],#b
                [147,20,255]]#pink
#[  0  86 221] [ 18 255 255]
#[100 121   0] [119 255 255]
#[133  15 171] [179 255 255]
#255,192,203#rgb
mypoints=[]     ##[x,y,colorid]

def findcolour(img,mycolour,mycolourvalues):
    imghsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    count=0
    newpoints=[]
    for color in mycolour:
        lower = numpy.array(color[0:3])
        upper = numpy.array(color[3:6])
        mask = cv2.inRange(imghsv, lower, upper)
        #cv2.imshow(str(color[0]), mask)
        x,y=getcontours(mask)
        cv2.circle(imgresult,(x,y),10,mycolourvalues[count],cv2.FILLED)
        if(x!=0 and y!=0):
            newpoints.append([x,y,count])
        count+=1
    return newpoints

def getcontours(img):
    cont,hier=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0
    for cnt in cont:
        area=cv2.contourArea(cnt)

        if area>500:
            #cv2.drawContours(imgresult,cnt,-1,(255,0,0),4)
            peri=cv2.arcLength(cnt,True)
            aprox=cv2.approxPolyDP(cnt,0.02*peri,True)
            x,y,w,h=cv2.boundingRect(aprox)
    return x+w//2,y

def draw(mypoints,mycolorvalues):
    for points in mypoints:
        cv2.circle(imgresult, (points[0],points[1]), 20, mycolourvalues[points[2]], cv2.FILLED)

while True:
    set,frame=cap.read()
    imgresult=frame.copy()
    newpoint= findcolour(frame,mycolour,mycolourvalues)
    if(len(newpoint)!=0):
        for newP in newpoint:
            mypoints.append(newP)
    if(len(mypoints)!=0):
        draw(mypoints,mycolourvalues)

    cv2.imshow("cma",imgresult)
    if (cv2.waitKey(1) & 0xFF==ord('q')):
        break
'''