def bubble_sort(lista):
    x = len(lista)

    for i in range(x):
        sorteado = False
        for j in range(0, x - i - 1):  
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                sorteado = True
        if not sorteado:  
            break
            
    return lista  


def selection_sort(lista):  
    ordenacao = len(lista)
    for i in range(ordenacao):  
        trex = i
        for j in range(i + 1, ordenacao):
            if lista[j] < lista[trex]:
                trex = j
        
        lista[i], lista[trex] = lista[trex], lista[i]
        
    return lista  



lista_bubble = [3, 5, 9, 2, 1, 0]
print("resultado:", bubble_sort(lista_bubble))  



lista_selecao = [3, 5, 9, 2, 1, 0]
print("resultado:", selection_sort(lista_selecao))