def contar(texto):
    palavras = texto.split()
    return len(palavras)

def main():
    texto = input('Digite seu texto: ')

    num_palavras = contar(texto)

    print(f'Esse texto contém {num_palavras} palavras.')

if __name__ == '__main__':
    main()
