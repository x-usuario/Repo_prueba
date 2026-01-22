# Variables y tipos de datosn en Python

#Declaracion de una variable 
my_variable = 10
# Tambien puedes reasignar el valor a una variable ya existente
my_variable = "Hola mundo"
print(my_variable)

#   Tipos de datos primitivos 
# Cadena de texto // Strings (str)
# Numero entreros // Intergers (int)
# Flotante // Floats (float)
# Blooleanos // Booleans (bool)
# NInguno // None (caso especial)

# String // cadena de texto  
# Metodos y propiedades para trabajar con datos del tipo String 
cadena = "Hola, mundo"
cadena_vacia = ""

# 1. len() : devuelce el numero de caracteres de una cadena 
print(" # 1. len() : devuelce el numero de caracteres de una cadena ")
cadena 
longitud = len(cadena)
print("El numero de caracreres en la palabra : ", cadena , " es de : ", longitud)

# 2. upper y lower : convierte la cadena a mayuskcula o monucula respectivammente 
print(" #2. upper y lower con vierte la cadena a mayuscula o minuscula ")
cadena 
mayuscula = cadena.upper()
minuscula = cadena.lower()
print("Mayuscula cadena : ", cadena , " resultado : " , mayuscula)
print("Minuscula cadena : ", cadena , " resultado : " , minuscula)

# 3. capitalize() y title() : capitalize() convierte el primer caracter en mayuscula , title() convierte la primera letra de cada palabra en mayuscula
print(" #3. capitalize() : convierte el primer caracter de la cadena de texto en mayuscula . title() : convierte la primera letra de cada palabra en mayuscula")
cadena = "Funcion de capitalize  y title, pruba de texto"
capitalize = cadena.capitalize()
title = cadena.title()
print(" Prueba con capitalize : " , capitalize)
print(" Prueba con title : ", title)

# 4. count : cuenta cuantas veces aparece una subcadena(una palabra(s)) en una una cadena (texto)
print (" #4. count cuenta cuantas veces aparace una subcadena en una cadena")
cadena = "Hola mundo"
veces = cadena.count("o")
print("Cadena utilizada : " , cadena , " letra selecionada 'o'")
print("apariciones : ", veces)

# 5. find e index : find() devulve el -1 cuando no encuentra la cadena e index() devualve un ValueError cuando no encuentra la cadena 
print("5. find e index, dan como resultado la pocicion de una subcadena en una cadena . Si la cadena no es encotrada find = -1 e index = ValueEerror")
cadena 
find_pocicion = cadena.find("mundo")
index_pocicion = cadena.index("mundo")
print("Resultado en index : " , find_pocicion)
print("Resultado index : " , index_pocicion)

# 6. replaze(nuevo, viejo) : reemplaza todas la ocurrencias(una palabra(s) ) de la cadena. 
print(" 6.  replace() : reemplaza todas la ocurrencias de la cadena")
string_ = "hola hola hola mundo.com"
new_string = string_.replace("hola" , "adios")
print("Cadena original : ", string_)
print("Cadena reemplaza : ", new_string)

# 7. strip() elimina los espacion en blanco de deracha e izquierda, lstrip() elimina los espacios en blanco de izquierda y rstrip elimina los espaciond de la derecha 
print(" 7. Elimina los espaicios en blanco de una cadena ")
espacio = "     Hola Python    " 
conteo = len(espacio)

strip = espacio.strip()
conteo1 = len(strip)

lstrip = espacio.lstrip()
conteo2 = len(lstrip)

rstrip = espacio.rstrip()
conteo3 = len(rstrip)

print(" cadena utilizada ", espacio ,  " numero de caracteres :" , conteo ) #20
print(" cadena utilizada ", strip ,  " numero de caracteres :" , conteo1 ) #11
print(" cadena utilizada ", lstrip ,  " numero de caracteres :" , conteo2 ) #15
print(" cadena utilizada ", rstrip ,  " numero de caracteres :" , conteo3 ) #16

# 8. starswith() y endswith , comprueba si la cadena empiza o termina con el prefijo o sifijo dado
print("8 .Comprube si la cadena empiza con el prefijo o termina con el sufijo dado")
cadena 
prefijo = cadena.startswith("hola")
sufijo = cadena.endswith("mundo")
print(" La cadena empiza con : " , prefijo)
print(" La cadena termina con : " , sufijo)

# 9. split() ; divide la cadena en una lista de subcadenas utilizando el separador espesificado. variable.split(separador especificado)
print(" 9. Separa la cadena en una lista de una subcadenas utilizando un separador especificado")
texto = "¡hola, mundo!"
lista = texto.split("o")
print("Cadena : ", texto ,". Lista : ", lista )

#10. join(iterable),une las cadenas en una  iterable utilizando la cadena como separador 
print("Concatena las cadeas de una iterable utilizando la cadena como separador")
texto =[ 'hola' , 'mundo','.com']
concatenar = '*'.join(texto)
print(texto , " concatenacion : ", concatenar)

print("*****************************************************************************************************************************************")
#Integers
# int // numero entero
#natural = 1
#negativo = -1
#cero = 0

#Metodos y propiedades 
#1. bit_lenth() devuelve el numero de bits necesarios para representar el numero en binario
print(" 1. bit_length devuelve la cantidad de bits  necesaria para representar un numero en binario")
num = 42
bits = num.bit_length()
print(" Numero : ", num , " bits necesarios para representacion binaria : " , bits)

#2. abs () : devuelde el valor absoluto del entero tambien puede ser utilizada con numeros fraccionario o decimal
print(" 2. abs() : devuel el valor absoluto del entero sea positivo o negativo siendo este ultimo convertido en positivo")
num_negativo = -1512.5
valor_absoluto = abs(num_negativo)
print(" Numero utilizado : ", num_negativo , " su valor absoluto es : ", valor_absoluto)

# 3. roud(), redondea el entero a un numero especificado de difitos deciales // round(variable, numero de decimales a redondear )
print(" 3. round(), redondea el numero a un numero especificado de decimales ")
num = 15.512
redondeo = round(num,2)
print(" Numero utlizado : ", num,  " numero redondeado : ", redondeo)

