#Escreva um programa que leia uma quantidade indeterminada de números reais, terminada pela leitura de um número 0 (zero). O programa deve mostrar uma nova lista onde cada elemento é a soma dos elementos anteriores da lista original. IMPORTANTE: Crie uma função chamada soma_cumulativa() que receba a lista original e retorna uma lista com a soma cumulativa. Por exemplo:
#minha_lista = [1, 2, 3, 4, 5]
#somacumulativa(minhalista)
#[1, 3, 6, 10, 15]

def cria_lista():
    lista = []
    while True:
        numeros = int(input())
        if numeros == 0:
            break
        lista.append(numeros)
    return lista

def soma_cumulativa(lista):
    lista_cumulativa = []
    soma = 0
    if isinstance(lista, list):
        for i in range(len(lista)):
            lista_cumulativa.append(lista[i] + soma)
            soma += lista[i]
    return lista_cumulativa

def main():
    nova_lista = cria_lista()
    resultado = soma_cumulativa(nova_lista)

    print(resultado)
if __name__ == "__main__":
    main()