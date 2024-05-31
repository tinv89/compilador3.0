from email.mime import application
from turtle import bgcolor
from analizador_lexico import analizador_lexico
from analizador_sintactico import *
import tkinter as abrir
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext as st
from tkinter import Scrollbar as sd
import sys
from tkinter import filedialog as fd
import re as r
class aplicacion:
    
    ventana = abrir.Tk()
    tokens = [] 

    def __init__(self):
        self.scanner=analizador_lexico()

        self.agregar_menu()

        self.scrolledtext1 = st.ScrolledText(self.ventana, width=60, height=25)
        self.scrolledtext1.grid(column=0, row=0, padx=10, pady=10)

        self.scrolledtext2 = st.ScrolledText(self.ventana, width=60, height=25)
        self.scrolledtext2.grid(column=1, row=0, padx=10, pady=10)

        self.scrolledtext3 = st.ScrolledText(self.ventana, width=125, height=10)
        self.scrolledtext3.grid(column=0, row=1, padx=10, pady=10, columnspan=2)

        self.ventana.mainloop()

    def agregar_menu(self):
        menubar = abrir.Menu(self.ventana)
        self.ventana.config(menu=menubar)
        opciones1 = abrir.Menu(menubar, tearoff=0)
        opciones1.add_command(label="Abrir Archivo", command=self.abrir)
        menubar.add_cascade(label="Archivo", menu=opciones1)
        menubar.add_command(label="Compilar", command=self.compilar)
        menubar.add_command(label="Tabla", command=self.ventanaTabla)

    def abrir(self):
        nombredoc = fd.askopenfilename(initialdir="E:\\Escritorio", title="Seleccione Archivo",
                                       filetypes=(("txt files", "*.txt"), ("todos los archivos", "*.*")))

        if nombredoc != '':
            archi1 = open(nombredoc, "r", encoding="utf-8")
            contenido = archi1.read()
            contenido1=contenido.replace(' ','')
            print(contenido1)
            archi1.close()
            self.scrolledtext1.delete("1.0", abrir.END)
            self.scrolledtext1.insert("1.0", contenido)

    def compilar(self):
        set_salida("")
        cadena = self.scrolledtext1.get("1.0", abrir.END) 
        self.scanner.analizar(cadena)
        parser=analizador_sintactico()
        parser.analizar(self.scanner.lista_tokens)
        
        respuesta=""
        for token in self.scanner.lista_tokens:
            token.vertoken()
            respuesta+=token.tipo + "(" + token.lexema +") "
            if token.lexema==";":
                respuesta+="\n"

        for error in self.scanner.lista_errores:
            error.vererror() 
       
        self.scrolledtext2.delete("1.0", abrir.END) 
        self.scrolledtext2.insert("1.0",respuesta) 
        
        self.scrolledtext3.delete("1.0", abrir.END)
        self.scrolledtext3.insert("1.0",ob_salida())
        if len(self.scanner.lista_errores)>0:
            mensaje=""
            for err in self.scanner.lista_errores:
                mensaje+="Hubo un Error lexico en la linea "+ str(err.linea)+ " y en la columna "+str(err.columna)+"\n"
            self.scrolledtext3.insert("1.0",mensaje)
        if len(parser.listaerroessin)>0:
            mensaje=""
            for err in parser.listaerroessin:
                mensaje+="Hubo un " + str(err.tipo) + " en la linea " + str(err.linea)+"\n"
            self.scrolledtext3.insert("1.0",mensaje)
        

    def ventanaTabla(self):
          
        self.ventana.deiconify()
        win = abrir.Toplevel()
        win.geometry('900x250')
        win.configure(bg='#58B2E5')
        win.resizable(0,0)

        tv = ttk.Treeview(win)
        tv = ttk.Treeview(win, columns=("tipo","valor_ini","alcance"))
        tv.pack(side=abrir.TOP)

        tv.column("#0",width=200)
        tv.column("tipo",width=200, anchor=CENTER)
        tv.column("valor_ini",width=200, anchor=CENTER)
        tv.column("alcance",width=200, anchor=CENTER)

        tv.heading("#0", text="Nombre Identificador", anchor=CENTER)
        tv.heading("tipo", text="Tipo", anchor=CENTER)
        tv.heading("valor_ini", text="Valor Inicial", anchor=CENTER)
        tv.heading("alcance", text="Alcance", anchor=CENTER)

        for i in range(len(self.scanner.lista_tokens)): 
            if self.scanner.lista_tokens[i].tipo=="ID":
                nombre=self.scanner.lista_tokens[i].lexema
                identificador=self.scanner.lista_tokens[i-1].lexema
                #es para no sobreescribir el token
                indice=i+2
                asignacion=""
                print(str(i))
                print(str(indice))
                if self.scanner.lista_tokens[indice-1].lexema=="=":
                    try:
                        while self.scanner.lista_tokens[indice].lexema!=";":
                            asignacion+=str(self.scanner.lista_tokens[indice].lexema)
                            indice+=1
                    except:
                        print(indice)

                    tv.insert("",END,text=nombre, values=(identificador,asignacion,""))
        regresar = abrir.Button(win,text="Regresar",command=win.destroy)
        regresar.pack(side=abrir.TOP)
       
aplicacion1 = aplicacion()   
            

            
        