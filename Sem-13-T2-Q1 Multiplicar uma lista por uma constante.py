#Escreva um programa que leia uma quantidade indeterminada de números inteiros, terminada pela leitura de um número 0 (zero). Depois, leia um valor inteiro constante. O programa deve mostrar uma nova lista onde cada valor da lista original é a multiplicado pelo valor da constante.
#IMPORTANTE: Crie uma função chamada multiplica_constante() que receba a lista original e o valor da constante e retorna uma nova lista com os elementos multiplicados.

def cria_lista():
    lista = []
    while True:
        numeros = int(input())
        if numeros == 0:
            break
        lista.append(numeros)
    return lista

def multiplica_valores_de_uma_lista(multiplciador, lista):
    lista_multiplicada = []
    if (isinstance(lista, list)):
        for i in range(len(lista)):
            lista_multiplicada.append(lista[i] * multiplciador)
    return lista_multiplicada

def main():
    lista = cria_lista()
    constante = int(input())
    resultado = multiplica_valores_de_uma_lista(constante, lista)
    print(resultado)

if __name__ == "__main__":
    main()