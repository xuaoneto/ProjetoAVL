class No(object): 
    def __init__(self, val): 
        self.val = val 
        self.esquerda = None
        self.direita = None
        self.nivel = 1

class Filme:

    def __init__ (self, nome, ano, id):
        self.nome = nome
        self.ano = ano
        self.id = id

    def __str__(self):
        return f'\n nome:{self.nome}\n ano:{self.ano}\n id:{self.id}\n ----------\n ' 
          
#******* Menu
def menu():
    O = input('''
            MENU:

            (1) Inserir filme
            (2) Buscar filme pelo id
            (3) Buscar filmes pelo ano
            (4) Listar filmes em ordem alfabética
            (5) Altura da árvore
            (6) Exibir a árvore
            (7) Sair do programa.
            ''')
    return O

class ArvoreAVL(object): 

    def inserir(self, raiz, chave): 
      
        #******* Passo 1 - Executar BST normal 
        if not raiz: 
            return No(chave) 

        #******* Verifica se o ID é único
        if self.unico(raiz, chave) == False:
            print('O id que você deseja cadastrar tem que ser único!')
            return 

        elif chave.id < raiz.val.id: 
            raiz.esquerda = self.inserir(raiz.esquerda, chave) 
        else: 
            raiz.direita = self.inserir(raiz.direita, chave) 
  
        #******* Passo 2 - Atualiza o nivel 
        raiz.nivel = 1 + max(self.getnivel(raiz.esquerda), 
                           self.getnivel(raiz.direita)) 
  
        #******* Passo 3 - Pega o fator de balanceamento 
        balance = self.getBalance(raiz) 
  
        #******* Passo 4 - Se o nó estiver desequilibrado
 
        #******* Caso 1 - esquerda esquerda 
        if balance > 1 and chave.id < raiz.esquerda.val.id: 
            return self.rodardireita(raiz) 
  
        #******* Caso 2 - direita direita 
        if balance < -1 and chave.id > raiz.direita.val.id: 
            return self.rodaresquerda(raiz) 
  
        #******* Caso 3 - esquerda direita 
        if balance > 1 and chave.id > raiz.esquerda.val.id: 
            raiz.esquerda = self.rodaresquerda(raiz.esquerda) 
            return self.rodardireita(raiz) 
  
        #******* Caso 4 - direita esquerda 
        if balance < -1 and chave.id < raiz.direita.val.id: 
            raiz.direita = self.rodardireita(raiz.direita) 
            return self.rodaresquerda(raiz) 
  
        return raiz 
  
    def rodaresquerda(self, z): 
  
        y = z.direita 
        T2 = y.esquerda 
  
        #******* Executa rotação 
        y.esquerda = z 
        z.direita = T2 
  
        #******* Atualiza os niveis 
        z.nivel = 1 + max(self.getnivel(z.esquerda), 
                         self.getnivel(z.direita)) 
        y.nivel = 1 + max(self.getnivel(y.esquerda), 
                         self.getnivel(y.direita)) 
  
        #******* Retorna a nova raiz  
        return y 
  
    def rodardireita(self, z): 
  
        y = z.esquerda 
        T3 = y.direita 
  
        #******* Executa rotação
        y.direita = z 
        z.esquerda = T3 
  
        #******* Atualiza os niveis 
        z.nivel = 1 + max(self.getnivel(z.esquerda), 
                        self.getnivel(z.direita)) 
        y.nivel = 1 + max(self.getnivel(y.esquerda), 
                        self.getnivel(y.direita)) 
  
        #******* Retorna a nova raiz 
        return y 

    #******* Retorna o Nível da Árvore
    def getnivel(self, raiz): 
        if not raiz: 
            return 0
  
        return raiz.nivel 
  
    def getBalance(self, raiz): 
        if not raiz: 
            return 0
  
        return self.getnivel(raiz.esquerda) - self.getnivel(raiz.direita) 

    #******* Anda em Pre-ordem na Árvore
    def preordem(self, raiz): 
  
        if not raiz: 
            return
  
        print("{0} ".format(raiz.val), end="") 

        self.preordem(raiz.esquerda) 
        self.preordem(raiz.direita)        

    #******* Busca id
    def buscaid(self, raiz, id):

        if not raiz: 
            return
            
        if id == raiz.val.id:
            print('Filme encontrado!\n')
            print("{0} ".format(raiz.val), end="")

        self.buscaid(raiz.esquerda, id) 
        self.buscaid(raiz.direita, id)    

    #******* Busca ano
    def buscaano(self, raiz, ano):

        if not raiz: 
            return
            
        if ano == raiz.val.ano:
            print("{0} ".format(raiz.val), end="")

        self.buscaano(raiz.esquerda, ano)
        self.buscaano(raiz.direita, ano)

    #******* Verifica se o ID é único
    def unico(self, raiz, chave): 
  
        if not raiz: 
            return True

        if chave.id == raiz.val.id:
            return False

        self.unico(raiz.esquerda, chave) 
        self.unico(raiz.direita, chave)  


    #******* Transfere as iniciais de cada filme para um array
    def ordenar(self, raiz, array):

        if not raiz:     
            return array

        array.append(raiz.val.nome[0])
        self.ordenar(raiz.esquerda, array)
        self.ordenar(raiz.direita, array)
            
    #******* Pega uma letra inicial de um filme e printa o filme e suas infos
    def buscaletra(self, raiz, letra):

        if not raiz:
            return 

        if letra == raiz.val.nome[0]:
            print("{0} ".format(raiz.val), end="")

        self.buscaletra(raiz.esquerda, letra)
        self.buscaletra(raiz.direita, letra)
