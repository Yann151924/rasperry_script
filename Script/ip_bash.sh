#!/bin/sh
#Permet d'envoyer un email
#A l'addresse concerner
#Si l'ip externe change qui est stocké dans le fichier nowipaddr

NOWIPADDR="nowipaddr"
GETIPADDR="ifconfig.me"

    if [ -f $NOWIPADDR ]
    then
       if [ `cat $NOWIPADDR` = `curl $GETIPADDR` ]
       then
           echo "Pas de changement d'IP."
       else
           curl $GETIPADDR > $NOWIPADDR
           mail -s "IP Rasperry PI" yann24.bonnau@gmail.com < $NOWIPADDR
        fi
    else
        curl $GETIPADDR >> $NOWIPADDR
    fi
