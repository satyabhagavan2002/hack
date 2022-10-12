from datetime import datetime
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import gtts
from playsound import playsound
def sendmail(data):
    smtp_user = 'cs207hostelproject@gmail.com'
    smtp_password = 'cs207dbms'
    server = 'smtp.gmail.com'
    port = 587
    msg = MIMEMultipart("alternative")
    msg["Subject"] = 'Why,Oh why!'
    msg["From"] = smtp_user
    msg["To"] = "cse190001038@iiti.ac.in"
    s=str(data)
    msg.attach(MIMEText('\nHey slot is avialable in your area'+s, 'plain'))
    s = smtplib.SMTP(server, port)
    s.ehlo()
    s.starttls()
    s.login(smtp_user, smtp_password)
    s.sendmail(smtp_user, "cse190001038@iiti.ac.in", msg.as_string())
    s.quit()

def solve():
    now = datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    today=str(int(day))+'-'+str(month)+'-'+str(year)
    pin="301701"
    print("Running.........")
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    url="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}".format(pin,today)
    r=requests.get(url,headers=headers)
    # print(r)
    # print(r.json()["sessions"])
    data=r.json()["sessions"]
    # print(data)
    # print(data[0])
    if len(data)>0:
        for data1 in data:
            if data1['available_capacity_dose2'] > 0 and data1['fee'] == '0' and data1['min_age_limit'] == 18:
                if data1['min_age_limit']==18:
                    # sendmail(data)
                    print(data)
                    # print('mail sent')
                    while True:
                        playsound("hola.mp3")

tts = gtts.gTTS("Slot avialable please book your slot fast", lang="en")
tts.save("hola.mp3")
def solve1():
    try:
        while True:

            # playsound("hola.mp3")
            solve()
            time.sleep(5)
    except:
            # playsound("hola.mp3")
            solve1()
solve1()