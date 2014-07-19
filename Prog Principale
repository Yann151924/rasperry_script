#Programme principale permettant un menu sur le piface cad

import pifacecad
import time
import os

def update_pin_text(event):
    event.chip.lcd.write(str(event.pin_num))
    choice = event.pin_num
    #Afficahge du script sysinfo fourni par Piface
    if choice == 0:
        cad.lcd.clear()
        cad.lcd.write("Menu selected")
        import subprocess
	#Lancement du programme sysinfo dans un sous processus
        p = subprocess.Popen(["/home/pi/display/sysinfo.py"])
        output, err = p.communicate()
        menu()
    #Choix pour afficher l'eheur et la datte courante
    if choice == 1:
        cad.lcd.clear()
        cad.lcd.write("Current time: \n")
        cad.lcd.write(time.ctime())
        time.sleep(5)
        menu()
    #Choix qu ipermet l'arret de la rasperry
    if choice == 2:
        cad.lcd.clear()
        cad.lcd.write("Arret...")
        os.system("sudo shutdown -h now")
    #Choix permettant d'avoir le blacklight on ou off
    if choice == 3:
        cad.lcd.backlight_on()
    if choice == 4:
        cad.lcd.backlight_off()
		
cad = pifacecad.PiFaceCAD()
cad.lcd.backlight_on()
cad.lcd.cursor_off()
cad.lcd.blink_off()
#Texte lors du demarrage
cad.lcd.set_cursor(5,0)
cad.lcd.write("Menu")
cad.lcd.set_cursor(2,1)
cad.lcd.write("Rasperry PI")
time.sleep(2)
cad.lcd.clear()
cad.lcd.write("1:Sys 2:Clock\n3:Off [4/5]:BL")
listener = pifacecad.SwitchEventListener(chip=cad)
for i in range (6):
    listener.register(i, pifacecad.IODIR_FALLING_EDGE, update_pin_text)
listener.activate()

def menu():
	cad.lcd.backlight_on()
	cad.lcd.clear()
	cad.lcd.write("1:Sys 2:Clock\n3:Off [4/5]:BL")
