#Escreva um programa que ler a nota de 50 alunos. Mostre uma lista apenas com os índices dos alunos que tem nota maior ou igual a 6 (seis).

def cria_lista():
    lista = []
    for i in range(50):
        numeros = float(input())
        numeros = f'{numeros:.1f}'
        lista.append(float(numeros))
    return lista

def mostra_notas_aprovativas(lista):

    lista_notas_aprovativas = []
    if (isinstance(lista, list)):
        for i in range(len(lista)):
            if (lista[i] >= 6):
                lista_notas_aprovativas.append(i)
    return lista_notas_aprovativas

def main():
    lista_de_notas = cria_lista()
    resultado = mostra_notas_aprovativas(lista_de_notas)
    print(resultado)

if __name__ == "__main__":
    main()