def quick_sort(lista):
    izquierda = []
    derecha = []
    centro=[] 

    if len(lista) >1:
        pivote = lista[-1]
        for i in lista:
            if i<pivote:
                izquierda.append(i)
            elif i==pivote:
                    centro.append(i)
            else:
                    derecha.append(i)
        return quick_sort(izquierda) + centro + quick_sort(derecha)
    else:
        return lista

lista = [2,3,4,5,5,5,6,7,7,8,6,9,2]
print(quick_sort(lista))

lista_sin_duplicados=[]

for i in lista:
    if i not in lista_sin_duplicados:
        lista_sin_duplicados.append(i)

print(lista_sin_duplicados)
