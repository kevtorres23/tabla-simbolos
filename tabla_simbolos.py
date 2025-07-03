tokensPorLinea = []
declaradores = ["load", "turbo"]
funciones = ["move", "shout", "check", "drift:", "change", "lap", "green", "red", "race", "listen", "id"]
parentesis = ['(', ')' , '{', '}' , '[', ']']
comentario = ["//"]

class TablaSímbolos:
    def __init__(self):
        self.table = {}
        
    def insert(self, nombre, atributos):
        if nombre in self.table:
            print(f"Error 1: El símbolo {nombre} ya está registrado en la tabla (se agregó el primero en aparecer).")
        else:
            self.table[nombre] = atributos
    
    def lookup(self, nombre):
        return self.table.get(nombre)
    
    def delete(self, nombre):
        if nombre in self.table:
            del self.table[nombre]
            return True
        else:
            print("Error 2: El símbolo", {nombre}, "no está registrado en esta tabla.")
            return False
    
    def display(self):
        print("\nTABLA DE SÍMBOLOS:")
        if not self.table:
            print("Error 3: La tabla se encuentra vacía aún.")
            return
        else:
            for nombre, atributos in self.table.items():
                print(f"Símbolo: {nombre}, Atributos: {atributos}" )
            print("----------")
        
tabla = TablaSímbolos()

def atributos(tipo, valor, alcance):
    atribs = {
        "tipo": tipo,
        "valor": valor,
        "alcance": alcance
    }
    return atribs

def leerInput(nombreArchivo):
    tokensTotales = []
    
    with open(nombreArchivo, 'r') as file:
        for line in file:
            line = line.strip()
            tokensSeparados = line.split(" ")
            
            if tokensSeparados[-1].find("\n") != -1:
                tokensSeparados[-1] = tokensSeparados[-1].replace("\n", "")
            
            tokensTotales.append(tokensSeparados)
        return tokensTotales

def clasificarTokens(lineas):
    for linea in lineas:
        if linea[0] in declaradores:
            tabla.insert(linea[1], atributos("str", linea[-1], "global"))
        elif linea[0] in funciones:
            tabla.insert(linea[0], atributos("función", "-", "global"))
        elif linea[0] in comentario:
            tabla.insert(linea[0], atributos("comentario", "-", "global"))
        else:
            print(f"Error: el símbolo {linea[0]} no fue encontrado en el léxico del lenguaje.")

tokensSeparados = leerInput("input_code.txt")
print("TOKENS SEPARADOS:\n", tokensSeparados, "\n")
clasificarTokens(tokensSeparados)

tabla.display()