#Escreva um programa que leia uma quantidade n, seguido da leitura de uma lista com n valores. O programa deve imprimir LISTA ORDENADA ou LISTA NÃO ORDENADA, conforme o caso. IMPORTANTE: Crie uma função chamada esta_ordenado() que recebe uma lista como parâmetro e retorne True se a lista estiver classificada em ordem crescente, e False se não for o caso. Por exemplo:
#esta_ordenado([1, 2, 2]) True
#esta_ordenado(['b', 'a']) False

def cria_lista():
    n = int(input().strip())
    lista = []
    for i in range(n):
        numeros = input().strip()
        lista.append(numeros)
    return lista

def esta_ordenada(lista):
    if (isinstance(lista, list)):
        memoria = lista[1]
        if isinstance(memoria, str):
            if memoria.isnumeric():
                lista_ordenada = sorted(lista, key=float)
            else:
                lista_ordenada = sorted(lista, key=str)
        return lista_ordenada == lista

def retorna_texto(resultado):
    if (resultado):
        print('LISTA ORDENADA')
    elif (resultado == False):
        print('LISTA NÃO ORDENADA')

def main():
    lista = cria_lista()
    resultado = esta_ordenada(lista)
    retorna_texto(resultado)

if __name__ == "__main__":
    main()