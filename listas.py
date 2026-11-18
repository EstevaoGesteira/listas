fila = ["Ana","Bruno"]
fila.append("Carla") #Adicona o item no final da lista
fila.insert(0,"Diego") #Adiciona o item na posição indicada pelo indice, neste caso o 0. Obs: Indice sempre na frente do item.
fila.remove("Bruno") #Remove o item da lista
atendido = fila.pop(0) #Remove e retorna o item da lista, indicado pelo indice
fila.sort() #Ordenha a lista em ordem alfabetica
print(atendido, fila)