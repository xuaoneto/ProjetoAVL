import time
import classes


Arvore = classes.ArvoreAVL()
raiz = None


print('Inserindo dados iniciais...')

filmes = [
  [ 'Dunkirk', '2017'],
  [ 'Os 7 de Chicago', '2020'],
  [ 'Interestelar', '2014'],
  [ 'Até o ultimo homem', '2016'],
  [ 'A Origem', '2010']
]
for k in range(len(filmes)):
    nome = filmes[k][0]
    ano = filmes[k][1]
    id = 888+k

    filme = classes.Filme(nome, ano, id)
    raiz = Arvore.inserir(raiz, filme)


while True:
    menu = classes.menu()

    if menu == '1':
        nome = input('Nome do filme: ')
        ano = input('Ano do filme: ')
        id = int(input('id do filme: '))
        filme = classes.Filme(nome,ano,id)
        raiz = Arvore.inserir(raiz,filme)

    if menu == '2':
        id = int(input('Digite o id do filme: '))
        Arvore.buscaid(raiz, id)
        print()

    if menu == '3':
        ano = input('Digite o ano do filme: ')
        Arvore.buscaano(raiz, ano)
        print()
    
    if menu == '4':
        array = []
        Arvore.ordenar(raiz, array)
        array.sort()
        count = 0
        for k in array:
            count+=1
            if array.count(k) != 1:
                del (array[count])
    
        for k in range(len(array)):
            Arvore.buscaletra(raiz, array[k])
            
    if menu == '5':
        print('A altura da arvore é', Arvore.getnivel(raiz))

    if menu == '6':
        Arvore.preordem(raiz)
        
    if menu == '7':
        break

    time.sleep(2)