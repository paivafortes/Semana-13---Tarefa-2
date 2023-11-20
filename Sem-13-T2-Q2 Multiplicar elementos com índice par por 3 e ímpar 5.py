#Escreva um programa que leia uma lista com 100 números. Ao término da leitura o programa deve fazer a ordenação dos números lidos. Após a ordenação, crie uma lista onde os elementos de índice par são multiplicados por 3 e os elementos de índice ímpar são multiplicados com 5. DICA: Use a função a sorted() ou o método sort() para realizar a ordenação dos valores.

def cria_lista():
    lista = []
    for i in range(100):
        numeros = int(input())
        lista.append(numeros)
    lista.sort()
    return lista

def multiplica_valores_de_uma_lista(lista):

    lista_multiplicada = []
    if (isinstance(lista, list)):
        for i in range(len(lista)):
            if (i % 2 == 0):
                lista_multiplicada.append(lista[i] * 3)
            elif (i % 2 != 0):
                lista_multiplicada.append(lista[i] * 5)
    return lista_multiplicada

def main():
    lista = cria_lista()
    resultado = multiplica_valores_de_uma_lista(lista)
    print(resultado)

if __name__ == "__main__":
    main()