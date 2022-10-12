import os,cv2

cv2_base_dir = os.path.dirname(os.path.abspath(cv2.__file__))
haar_model = os.path.join(cv2_base_dir, 'data/haarcascade_frontalface_default.xml')

#haar_model1 = os.path.join(cv2_base_dir, 'data/haarcascade_eye.xml')

facecascade = cv2.CascadeClassifier(haar_model)
#eyecascade = cv2.CascadeClassifier(haar_model1)

img3 = cv2.VideoCapture(0)
while True:
    set,img=img3.read()
    imggrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = facecascade.detectMultiScale(imggrey, 1.1, 4)
    #eye = eyecascade.detectMultiScale(imggrey, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #for (x, y, w, h) in eye:
     #   cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("img", img)
    if(cv2.waitKey(1) and 0xFF=='q'):
        break