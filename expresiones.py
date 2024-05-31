#para identificar si es un arreglo si es una cadena un entero
class expresion_literal:
    def __init__(self, tipo, valor):
        self.tipo=tipo
        self.valor=valor

    def get_Valor(self,entorno):
        if self.tipo=="CAD":
            return self.valor.replace('"', '')
        elif self.tipo=="NUM":
            return int(self.valor)
        elif self.tipo=="CAR":
            return self.valor.replace("'","")
        elif self.tipo=="DEC":
            return float(self.valor)
    
class expresion_identificador:
    def __init__(self,id):
        self.id=id
    def get_Valor(self,entorno):
        return entorno.get(self.id)