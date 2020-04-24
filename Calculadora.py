valores = ["operacion","val1","val2"]
operaciones= "*+-/"
numeros = "123456789"
def sumar(a,b):
	return int(a) + int(b)
def multiplicar(a,b):
	return int(a) * int(b)
def dividir(a,b):
	return int(a)/int(b)
def restar(a,b):
	return int(a) - int(b)
def separarar_caracteres(strng):
	#el uno se refiere a la posicion el la lista valores cuando se detecte el signo pasara a la siguiente posicion
	buscando_el_siguiente_parentesis = False
	lado_de_la_operacion  =  1
	posicion_parentesis_actual = "none"
	contador = -1
	for i in strng:
		contador = contador + 1 
		if i in operaciones and not(buscando_el_siguiente_parentesis):
			valores[0] = i 
			valores[1] = int(strng[0:(strng.find(i))])
			valores[2] = int(strng[(strng.find(i)+1):len(strng)])
		elif i in numeros or i == " ":
			continue
		elif i == "(":
			posicion_parentesis_actual = contador
			buscando_el_siguiente_parentesis = True
		elif i == ")":
			posicion_segundo_parentesis=contador
			valor_del_parentesis = calcular(strng[(posicion_parentesis_actual + 1):posicion_segundo_parentesis])
			operacion_actualizada = strng.replace(strng[posicion_parentesis_actual:(posicion_segundo_parentesis + 1) ],str(valor_del_parentesis))
			separarar_caracteres(operacion_actualizada)
	return valores
def operar(a):
	if not ("operacion" in a or "val1" in a or "val2" in a):
		if a[0] == "*":
			return(multiplicar(a[1],a[2]))
		elif a[0] == "+":
			return(sumar(a[1],a[2]))
		elif a[0] == "-":
			return(restar(a[1],a[2]))
		elif a[0] == "/":
			return(dividir(a[1],a[2]))

def calcular(operacion_escrita):
	j = separarar_caracteres(operacion_escrita)
	return operar(j)


while True:
	respuesta = input("Escribe la operacion basica a continuacion: ")
	print(calcular(respuesta))