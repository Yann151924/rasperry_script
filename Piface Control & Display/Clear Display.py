import pifacecad

#Nettoyage de l'ecran

cad=pifacecad.PiFaceCAD()
cad.lcd.backlight_off()
cad.lcd.blink_off()
cad.lcd.cursor_off()
cad.lcd.clear()  
