'''
Author: César Jauregui Saavedra
Version: 1.0
Date: 28-01-2021
Email: cjaureguisaavedra@gmail.com
'''
#Importación de las librerias
import smtplib
import sys
import os.path
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from tkinter import Tk
from tkinter import Label
from tkinter import Entry 
from tkinter import Button
from tkinter import PhotoImage
from tkinter import filedialog
from tkinter import StringVar
from tkinter import Menu
from tkinter import messagebox

class Aplication:
    def __init__(self):
        #Configuración de la ventana
        self.root=Tk()
        self.root.resizable(0,0)
        self.root.title("SendFast - Envío de archivos")
        if getattr(sys, 'frozen', False) :
            self.root.iconbitmap(sys._MEIPASS + '\\logo.ico')
        else :
            self.root.iconbitmap('logo.ico')
        self.menubar=Menu(self.root,bg="grey")
        self.root.config(menu=self.menubar)
        #Creación de variables
        self.from_mail=StringVar()
        self.passw=StringVar()
        self.to_mail=StringVar()
        self.path_file=StringVar()
        
        #Creación de menú
        self.filemenu=Menu(self.menubar, tearoff=0)
        self.help=Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Programa", menu=self.filemenu)
        self.menubar.add_cascade(label="Ayuda", menu=self.help)
        self.filemenu.add_command(label="Nuevo", command=self.new_mail)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Salir", command=self.close_app)
        self.help.add_command(label="Ayuda", command=self.help_app)
        self.help.add_separator()
        self.help.add_command(label="Acerca de...", command=self.about_app)

        #Creación de etiquetas(Label), campos de texto(Entry) y botones(Button)
        self.label1=Label(text="Su correo:").grid(pady=5, row=0, column=0)
        self.label2=Label(text="Su contraseña:").grid(pady=5, row=1, column=0)
        self.label3=Label(text="Para:").grid( pady=5, row=2, column=0)
        self.label4=Label(text="Archivo:").grid(pady=5, row=3,column=0)
        self.entry1=Entry(self.root, width=40, textvariable=self.from_mail).grid(padx=5, row=0, column=1, columnspan=2)
        self.entry2=Entry(self.root, width=40, textvariable=self.passw, show="*").grid(padx=5, row=1, column=1, columnspan=2)
        self.entry3=Entry(self.root, width=40, textvariable=self.to_mail).grid(padx=5, row=2, column=1, columnspan=2)
        self.button1=Button(self.root, text="Seleccione un archivo",command=self.open_file_dialog, width=16).grid(padx=5, row=3, column=1)
        self.entry4=Entry(self.root, width=40, textvariable=self.path_file, state="readonly").grid(padx=5, row=4, column=1)
        self.button2=Button(self.root, text="Enviar",command=self.sendemail, width=40).grid(padx=10, pady=10, row=5, column=0, columnspan=4)

        #Arrancar la ventana
        self.root.mainloop()

    #Función para cerrar la aplicación preguntando antes si desea salir
    def close_app(self):
        mensaje=messagebox.askquestion("Salir","¿Desea salir de la aplicación?")
        if mensaje=="yes":
            self.root.destroy()

    #Función para limpiar los campos de texto(Entry)
    def new_mail(self):
        self.from_mail.set("")
        self.passw.set("")
        self.to_mail.set("")
        self.path_file.set("")
    
    #Función que muestra un mensaje de ayuda
    def help_app(self):
        mensaje=messagebox.showinfo("Ayuda","Para cualquier consulta, envie un correo a cjaureguisaavedra@gmail.com\nCon gusto te ayudaré :)")

    #Función que muestra un mensaje acerca de la app
    def about_app(self):
        mensaje=messagebox.showinfo("Acerca de...", "SendFast Versión 1.0\nAutor: César Jauregui Saavedra\nGithub: https://github.com/CesJauregui")

    #Función para abrir el explorador de carpetas y guarda el path del archivo
    def open_file_dialog(self):
        self.path_file.set(filedialog.askopenfilename(initialdir="/", title="Seleccione archivo"))
        return self.path_file

    #Función que carga el archivo para ser enviado
    def load_file(self, file, file_name):
        read_file = open(file,'rb')
        attach = MIMEBase('multipart','encrypted')
        attach.set_payload(read_file.read())
        read_file.close()
        encoders.encode_base64(attach)
        attach.add_header('Content-Disposition', 'attachment', filename=file_name)
        return attach

    #Función para enviar el correo adjuntando el archivo
    def sendemail(self):
        smtp_server = 'smtp.gmail.com:587'
        smtp_user = self.from_mail.get()
        smtp_pass = self.passw.get()
        email = MIMEMultipart()
        email['To'] = self.to_mail.get()
        email['From'] = smtp_user
        email['Subject'] = 'Enviado desde SendFast'
        arroba=smtp_user.count("@")
        arroba2=email['To'].count("@")
        try:
            #Evalúa si los correos cumplen con lo antes mencionado como también el path
            if arroba!=1 or arroba2!=1 or smtp_user.rfind("@")==(len(smtp_user)-1) or email['To'].rfind("@")==(len(email['To'])-1) or email['To'].find("@")==0 or smtp_user.find("@")==0 or self.path_file.get()=="" or smtp_pass=="":
                mensaje=messagebox.showerror("Aviso","No se puede enviar datos en blanco o mal escritos.\nVerifica nuevamente por favor.")
            else:
                #Si todo está correcto, el proceso sigue con el envío del correo
                email.attach(MIMEText('<p style="color:black;" >Envío Archivo adjunto</p>','html'))
                name_file = os.path.basename(os.path.normpath(self.path_file.get()))#Obtener sólo el nombre del archivo con su extensión
                email.attach(self.load_file(self.path_file.get(), name_file))
                smtp = smtplib.SMTP(smtp_server)
                smtp.starttls()
                smtp.login(smtp_user,smtp_pass)
                smtp.sendmail(smtp_user, email['To'], email.as_string())
                smtp.quit()
                mensaje=messagebox.showinfo("Aviso","Se envió el email correctamente") 
        except smtplib.SMTPAuthenticationError:
            mensaje=messagebox.showerror("Aviso","Correo o contraseña no aceptados")
        except smtplib.SMTPDataError:
            mensaje=messagebox.showerror("Aviso","Este mensaje fue bloqueado porque su contenido presenta problemas de seguridad")
aplication=Aplication()

    

   