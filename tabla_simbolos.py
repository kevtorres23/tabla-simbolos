tokens = []
p_reservadas = ["move", "shout", "check", "drift", "change", "lap", "green", "red", "turbo", "race", "load", "listen", "//"]
operadores = ['+', '-', '*', '/', '=', '<', '>=', '<=']
puntuacion = ['(', ')' , '{', '}' , '[', ']', ',']

with open('input_code.txt', 'r') as file:
    a = file.readlines()
    for t in a:
        tokens = tokens + (t.split(" "))
    print(tokens)

# funcion insert(id, td) - insert(a, int) para el caso de int a


# funcion lookup(simbolo) se utiliza para buscar un nombre


# funcion lookup
 