from PicoBreadboard import LED,BUZZER,BUTTON
import time

#create object for various class
LED1 = LED(0) #create object for LED class, LED connected at GP0
LED2 = LED(1) #create object for LED class, LED connected at GP1
LED3 = LED(2) #create object for LED class, LED connected at GP2

BT1 = BUTTON(4) # Button connected at GP4
#buzzer = BUZZER(3) # Buzzer connected at GP8

while 1:
   if BT1.read() == 1: #button pressed
       LED1.on()   #led 1 on
       LED2.on()   #led 2 on
       LED3.on()   #led 3 on
       #buzzer.on() # buzzer on
       print("LED 1 ON")
   else :
       LED1.off()
       LED2.off()
       LED3.off()
       buzzer.off()
       print("Press Button 1")
       
   time.sleep(0.5) # delay 500ms
   

