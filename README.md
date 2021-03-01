# SendFast 1.0
Programa sencillo de envío de archivos a cuentas de gmail usando SMTP.

1) Con PyInstaller, mediante este comando se creará el ejecutable:

    pyinstaller SendFast.py -i logo.ico --noconsole --onefile --add-data logo.ico;.
  
2) Una vez realizado el paso anterior descargar e instalar [InstallForge](https://installforge.net/) 

3) Ahora que está empaquetado el proyecto, se creará un instalador para poder distribuirlo.
  Hecha un vistazo a [crear un instalador con InstallForge](https://www.learnpyqt.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/), desliza hasta
  encontrar el apartado "Creating an installer" y sigue los pasos.

4) ¡Probar el instalador!

Nota: 

 - Para enviar los correos, el usuario que va a enviar el correo tiene que realizar estos pasos: https://docs.rocketbot.co/?p=1567. Se recomienda usar en este caso una cuenta
 que no comprometa información importante. Por ejemplo un correo que lo use poco. El destinatario no es necesario que haga este procedimiento.
 - Gmail tiene bloqueados algunos tipos de archivos. Para saber cuáles son, visita: https://support.google.com/mail/answer/6590?hl=es-419#zippy= para más información.



  
