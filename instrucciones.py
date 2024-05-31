#importacion de instrucciones y ejecutarlas
from turtle import update
from expresiones import *
from clases import error
salida=""

class inicio():
    def __init__(self,instrucciones):
        self.instrucciones=instrucciones
    def ejecutar(self,entorno):
        self.instrucciones.ejecutar(entorno)
        
class instrucciones():
    def __init__(self,instrucciones,instrucciones2):
        self.instrucciones=instrucciones
        self.instrucciones2=instrucciones2
    def ejecutar(self,entorno):
        self.instrucciones.ejecutar(entorno)
        self.instrucciones2.ejecutar(entorno)
        
class instrucciones2():
    def __init__(self,instrucciones,instrucciones2):
        self.instrucciones=instrucciones
        self.instrucciones2=instrucciones2
    def ejecutar(self,entorno):
        if self.instrucciones and self.instrucciones2:
            self.instrucciones.ejecutar(entorno)
            self.instrucciones2.ejecutar(entorno)
            
class instruccion():
    def __init__(self, instruccion):
        self.instruccion=instruccion
    def ejecutar(self,entorno):
        self.instruccion.ejecutar(entorno)
        
class declaracion():
    def __init__(self,id,exp):
        self.id=id
        self.exp=exp
    def ejecutar(self,entorno):
        valor=self.exp.get_Valor(entorno)
        entorno.update({self.id:valor})
        
class error_sin():
    def __init__(self,listaerror,linea,columna):
        self.listaerror=listaerror
        self.linea=linea
        self.columna=columna
        
    def ejecutar(self,entorno):
        self.listaerror.append(error("", "Error Sintactico",self.linea, self.columna))
        
class error_sem():
    def __init__(self,listaerror,linea,columna):
        self.listaerror=listaerror
        self.linea=linea
        self.columna=columna
        
    def ejecutar(self,entorno):
        self.listaerror.append(error("", "Error Semantico",self.linea, self.columna))
        
class println():
    def __init__(self,exp):
        self.exp=exp
        
    def ejecutar(self,entorno):
        global salida
        valor=self.exp.get_Valor(entorno)
        salida+=str(valor)+"\n"
        
def ob_salida():
    global salida
    return salida
    
def set_salida(txt):
    global salida
    salida=txt
        
class printsn():
    def __init__(self,exp):
         self.exp=exp
         
    def ejecutar(self,entorno):
        global salida
        valor=self.exp.get_Valor(entorno)
        salida+=str(valor)
        
             
         
                
                       
                        
        
                        