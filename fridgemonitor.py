#!/usr/bin/python


import smtplib
import urllib.request

url = "http://qdot-server.phas.ubc.ca:8081/webService/logger.php?action=getCurrentValue&loggable_name=ighn_temp_1k&yes_calc=0"
with urllib.request.urlopen(url) as response:
  T1kpot=response.read()
#print(float(T1kpot.decode("utf-8")))
#float(html.decode("utf-8"))
if (float(T1kpot.decode("utf-8"))>1.6):
 
 print(float(T1kpot.decode("utf-8"))>1.6)
 fromaddr = 'yourID@gmail.com'
 toaddrs  = 'yourID@gmail.com'
 msg = T1kpot#'Why,Oh why!'
 username = 'yourID@gmail.com'
 password = 'yourpwd'
 server = smtplib.SMTP('smtp.gmail.com:587')
 server.ehlo()
 server.starttls()
 server.login(username,password)
 server.sendmail(fromaddr, toaddrs, msg)
 server.quit()
 
else: 

  T1kpot=response.read()
