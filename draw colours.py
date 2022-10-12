import cv2,numpy

mycolour=[[0,102,136,22,255,255],  #orange
          [57,76,0,100,255,255],#g
          [100,121,0,119,255,255],#b
          [133,15,171,179,255,255]]#g

mycolourvalues=[[51,153,255],     ##bgr
                [0,255,0],#g
                [255,0,0],#b
                [147,20,255]]#pink
#[  0 102 136] [ 22 255 255]
#[100 121   0] [119 255 255]
#[133  15 171] [179 255 255]
#255,192,203#rgb
mypoints=[]     ##[x,y,colorid]

def findcolor(img,mycolour,mycolourvalues):
    imghsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    count=0
    mypoint=[]
    for color in mycolour:
        lower=numpy.array(color[0:3])
        upper=numpy.array(color[3:6])
        mask=cv2.inRange(imghsv,lower,upper)
        x,y=getcontrower(mask)
        cv2.circle(imgres,(x,y),10,(mycolourvalues[count]),cv2.FILLED)
        if(x!=0 and y!=0):
            mypoint.append([x,y,count])
        count+=1
    return mypoint


def getcontrower(imgb):
    cont,hei=cv2.findContours(imgb,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0
    for cnt in cont:
        area=cv2.contourArea(cnt)
        if area>500:
            #cv2.drawContours(imgres,cnt,-1,(255,0,0),2)
            peri=cv2.arcLength(cnt,True)
            aprrox=cv2.approxPolyDP(cnt,0.02*peri,True)
            x,y,w,h=cv2.boundingRect(aprrox)
    return x+w//2,y

def draw(mypoints,mycolourvalues):
    for point in mypoints:
        cv2.circle(imgres,(point[0],point[1]),20,mycolourvalues[point[2]],cv2.FILLED)

img=cv2.VideoCapture(0)


while True:
    set,frame=img.read()
    #cv2.imshow("img",frame)
    imgres=frame.copy()

    point=findcolor(frame,mycolour,mycolourvalues)
    if(len(point)!=0):
        for pnt in point:
            mypoints.append(pnt)
    if(len(mypoints)!=0):
        draw(mypoints,mycolourvalues)
    cv2.imshow("imgr",imgres)

    if cv2.waitKey(1) & 0xFF==ord("q"):
        break