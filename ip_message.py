#Programme permettant l'envoie d'un mail contenant l'adresse ip publique/externe de votre reseau
import smtplib 
import subprocess

#Commande permettant d'avior l'adresse IP Publique
ouput = subprocess.check_output("curl http://ipecho.net/plain", shell=True)

#Text du message
text = "L'adresse IP Externe est : " + str(ouput)

# Adresse permettant la connexion au smtp gmail  
src = "source adresse" 
password = "password" 
dest = "adresse dest" 

#Fonction permettant la connexion et l'envoie du message
def send(text): 
    mail = "To: " + dest + "\nFrom: " + src + "\nSubject: IP Externe Rasperry PI\n\n" + text 

    smtp = smtplib.SMTP('smtp.gmail.com:587') 
    smtp.ehlo() 
    smtp.starttls() 
    smtp.ehlo() 
    smtp.login(src, password) 
    smtp.sendmail(src, dest, mail) 
    smtp.close() 

send(text)
exit()
