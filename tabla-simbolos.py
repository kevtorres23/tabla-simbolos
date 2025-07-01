codigoInput = input(str("Ingresa un código: "))
print(codigoInput)

# lista de palabras encontradas
keywordsEncontrados = []

# diccionario

# automatizar la clasificación del código que le ingresemos

formadorPalabras = ""

counter = 0

while counter < len(codigoInput):
    if ((codigoInput[counter] == " ") or (counter == (len(codigoInput) - 1) )):
        if (counter == (len(codigoInput) - 1)):
            formadorPalabras += codigoInput[counter]          
        
        keywordsEncontrados.append(formadorPalabras)
        formadorPalabras = "" # resetear el formador
    else:
        formadorPalabras += codigoInput[counter]
    counter += 1
    
print(keywordsEncontrados)