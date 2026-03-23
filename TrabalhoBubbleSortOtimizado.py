def bubble_sort_otimizado(lista: list) -> list:

    n = len(lista)
    
    for i in range(n):
        
        houve_troca = False

        for j in range(0, n - i - 1):
            

            if lista[j] > lista[j + 1]:
                
      
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                
   
                houve_troca = True
        
        if not houve_troca:
            break

    return lista

if __name__ == "__main__":
    
    numeros = [5, 3, 8, 4, 2]
    print("lista original: ", numeros)
    
    resultado = bubble_sort_otimizado(numeros.copy())
    print("lista ordenada: ", resultado)