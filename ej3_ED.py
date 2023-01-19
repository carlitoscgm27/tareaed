def crear_diccionario(cadena):
  lista= cadena.split()
  diccionario={}
  for i in lista:
    if i in diccionario:
      diccionario[i] +=1
    else:
      diccionario[i]= 1
  return diccionario

def contador_diccionario(diccionario):
  palabra= ''
  cantidad=0
  for cosa1, cosa2 in diccionario.items():
    if cosa2 > cantidad:
      cantidad = cosa2
      palabra= cosa1
  return palabra, cantidad
entrada = input('Ingrese su cadena de caracteres: ')
print(crear_diccionario(entrada))
print(contador_diccionario(crear_diccionario(entrada)))