class token:
    #clasificacion en la tabla
    def __init__(self,tipo,lexema,linea,columna):
        self.tipo=tipo
        self.lexema=lexema
        self.linea=linea
        self.columna=columna
        self.tipo2=None
#muestra en consola los tokens
    def vertoken(self):
        print("---------------------------------------------------------------------------------")
        print(self.tipo +'(' + self.lexema + ')')
        print('linea: '+ str(self.linea))
        print('columna: ' + str(self.columna))
#ver errores
class error:
    def __init__(self,caracter,tipo,linea,columna):
        self.caracter=caracter
        self.tipo=tipo
        self.linea=linea
        self.columna=columna
#muestra errores en consola
    def vererror(self):
        print("===================================================================================")
        print('caracter: '+ self.caracter)
        print('linea: '+ str(self.linea))
        print('columna: ' + str(self.columna))

