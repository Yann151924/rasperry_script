#A l'extinction lancement d'un service qui affiche un message d'arret puis clean de l'ecran
import pifacecad as p
from time import sleep
cad = p.PiFaceCAD()
cad.lcd.backlight_on()
cad.lcd.cursor_off()
cad.lcd.blink_off()
#Affichage d'un message comme quoi l'arret et fini
cad.lcd.set_cursor(4,0)
cad.lcd.write("Arret")
cad.lcd.set_cursor(2,1)
cad.lcd.write("En cours ...")
#Apres deux secondes clean de l'ecran
sleep(2)
cad.lcd.backlight_off()
cad.lcd.blink_off()
cad.lcd.cursor_off()
cad.lcd.clear()
exit()
