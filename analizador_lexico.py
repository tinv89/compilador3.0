#analizador lexico
from unicodedata import decimal

from cv2 import cartToPolar
from clases import token,error
import re
class analizador_lexico():
    def __init__(self):
        self.lista_tokens=[]
        self.lista_errores=[]
    
    def analizar(self,contenido):
        self.lista_tokens=[]
        self.lista_errores=[]
        contenido+="$"
        indice=0 #contador
        linea=1 #indicar linea o posicion del token 
        columna=1
        buffer=""
        buffer1=""
        estado="a"
        decimal=False
        while indice<len(contenido):
            #guardar caracter evaluado
            caracter=contenido[indice]
            if estado=="a":
                #verificamos todos los signos 
                if caracter=="+" or caracter=="-" or caracter=="=" or caracter=="*" or caracter=="/" or caracter=="<" or caracter==">" or caracter==".":
                    buffer=caracter
                    columna+=1
                    self.lista_tokens.append(token("OP",buffer,linea,columna))
                    buffer=""
                    estado="a"
                elif caracter==";" or caracter=="," or caracter=="(" or caracter==")" or caracter=="[" or caracter=="]" or caracter=="{" or caracter=="}" or caracter==":":
                    buffer=caracter
                    columna+=1
                    self.lista_tokens.append(token("DEL",buffer,linea,columna))
                    buffer=""
                    estado="a"
                elif caracter=="\n":
                    columna=1
                    linea+=1
                elif caracter=="\t":
                    columna+=1
                elif caracter==" ":
                    columna+=1
                    #para verificar si es una letra
                elif re.search('[a-zA-Z]', caracter) or caracter == '_':
                    buffer=caracter
                    columna+=1
                    estado="b"
                elif caracter.isdigit():
                    buffer=caracter
                    buffer1=caracter
                    columna+=1
                    estado="c"
                elif caracter=='"':
                    buffer=caracter
                    columna+=1
                    estado="d"
                elif caracter=="'":
                    buffer=caracter
                    columna+=1
                    for i in range(32,256):
                        if str(contenido[indice+1])==str(chr(i)):
                            buffer+=contenido[indice+1]
                            columna+=1
                            if contenido[indice+2]=="'":
                                buffer+=contenido[indice+2]
                                columna+=1
                                self.lista_tokens.append(token("CAR", buffer,linea,columna))
                                buffer=""
                                estado="a"
                                indice+=2
                            else:
                                self.lista_errores.append(error("ERROR",buffer,linea,columna))
                                buffer=""
                                estado="a"
                                indice+=2  
                    buffer=""
                    estado="a"
                elif caracter=="$":
                    buffer=caracter
                    columna+=1
                    self.lista_tokens.append(token("EOF",buffer,linea,columna))
                    buffer=""
                    estado="a"
                    print("Analisis Lexico hecho correctamente")
                else:
                    self.lista_errores.append(error(caracter,"ERROR",linea,columna))
                    buffer=""
                    columna+=1

                
            elif estado=="b":
                #verficamos palabras reservadas
                if re.search('[a-zA-Z]', caracter) or caracter == '_' or re.search('\d', caracter):
                    buffer+=caracter
                    columna+=1
                    estado="b"
                else:
                    reservadas = ['assert', 'bool', 'break', 'case', 'catch', 'char', 'class', 'continue', 'default', 'do', 'double', 'else', 'enum', 'extends',
                                  'false', 'finally', 'float', 'for', 'if', 'implements', 'import', 'instanceof', 'int', 'interface', 'main', 'new', 'null', 'out',
                                  'package', 'private', 'protected', 'public', 'return', 'static', 'String', 'System', 'switch', 'this', 'throw', 'throws', 'true', 'try',
                                  'var', 'void', 'while', 'boolean', 'extends', 'print', 'println', 'include', 'for', 'while', 'do', 'switch', 'case', 'break', 'continue', 
                                  'return', 'if','else', 'struct', 'class', 'enum', 'namespace', 'const', 'static', 'virtual', 'inline', 'friend', 'template', 'typename',
                                  'typedef', 'sizeof', 'new', 'delete', 'try', 'catch', 'throw', 'const_cast', 'dynamic_cast', 'reinterpret_cast', 'static_cast', 'cin',
                                  'cout', 'cmath', 'cstdlib'] 
                    val=0
                    for reser in reservadas:
                        if buffer==reser:
                            self.lista_tokens.append(token("PR",buffer,linea,columna)) 
                            val=1

                    if val==0:
                        self.lista_tokens.append(token("ID",buffer,linea,columna))
                
                    buffer=""
                    estado="a"
                    indice-=1
            elif estado=="c":
                
                if caracter.isdigit():
                    buffer+=caracter
                    buffer1+=caracter
                    columna+=1
                    estado="c"
                elif caracter==".":
                    decimal=True
                    buffer1+=caracter
                    columna+=1
                    estado="c"
                else: 
                    if decimal==False:
                        nuevo=token("NUM",buffer,linea,columna)
                        nuevo.tipo2=1
                        self.lista_tokens.append(nuevo)
                    else: 
                        nuevo=token("NUM",buffer1,linea,columna)
                        nuevo.tipo2=2
                        self.lista_tokens.append(nuevo)
                    buffer=""
                    indice-=1
                    estado="a"
                    
            elif estado=="d":
                if caracter=='"':
                    buffer+=caracter
                    columna+=1
                    self.lista_tokens.append(token("CAD",buffer,linea,columna))
                    buffer=""
                    estado="a"
                elif caracter=="\n":
                    columna=1
                    linea+=1
                elif caracter=="'":
                    buffer+=caracter
                    columna+=1
                    self.lista_errores.append(error(buffer,"ERROR",linea,columna))
                    buffer=""
                    estado="a"
                else:
                    buffer+=caracter
                    columna+=1
                    estado="d"
           
            #para que recorra caracter es su indice
            indice+=1