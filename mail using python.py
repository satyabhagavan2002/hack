import smtplib
s='pinnedheartstrings@gmail.com'
r='allen.kumarmohit@gmail.com'
m='''hello
sent successfully
'''
sm=smtplib.SMTP('smtp.gmail.com',587)
sm.starttls()
sm.login(s,"kumar@mohit")
sm.sendmail(s,r,m)
print('done')