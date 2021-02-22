"""
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject ---> para crear un nuevo proyecto ejemplo de uso C:\jess\proyectosDjango>django-admin startproject Proyecto1
    test
    testserver
"""


superusuario = admin
correo= admin@hotmail.com
pass= 123admin


#<!-- TOKEN  --> Impide un ataque a la web por secuestro de sesion.

# {% csrf_token %} ----> dentro del form en el template contacto.html

#PARA IMPORTAR LA LIBRERIA NECESARIA PARA EL ENVIO DE MAILS utilizando SMTP
#Primero importar estas librerias en views.py
from TiendaOnline import settings
from django.core.mail import mail_admins, send_mail

#Para enviar correo de prueba desde la terminal
# python manage.py shell ---> se debe entrar desde aqui
from django.core.mail import send_mail
#Formato= send_mail('prueba de asunto','este es el mensaje','correo remitente',['correo destino'],silencio de error=false)
#Ejemplo=
send_mail('Asunto','Mensaje','jdprincesita@gmail.com',['jdprincesita@gmail.com'],fail_silently=False)

#PARA DAR ACCESO DESDE GOOGLE IR A ESTA LINEA DESDE TU CUENTA DE gmail
https://www.google.com/settings/security/lesssecureapps