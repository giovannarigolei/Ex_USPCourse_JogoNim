
def partida():
       n = int(input("Quantas peças?"))
       m = int(input("Limite de peças por jogada?"))
       vezPc=False
       if n%(m+1)==0:
           print()
           print("Você começa!")
           print()
       else:
           print()
           print("Computador começa!")
           print()
           vezPc=True
    
       while n>0:
             if vezPc:
                   computadorTira=computador_escolhe_jogada(n, m)
                   n=n-computadorTira
                   if computadorTira==1:
                         print()
                         print("O computador tirou uma peça.")
                   else:
                          print()
                          print("O computador tirou", computadorTira,"peças.")
                   if n == 1:
                          print("Agora resta apenas uma peça no tabuleiro.")
                          print()
                   else:
                          if n!=0:
                             print("Agora restam", n, "peças no tabuleiro.")
                             print()      
                   vezPc=False
             else:
                  jogadorTira=usuario_escolhe_jogada(n,m)
                  n=n-jogadorTira
                  if jogadorTira==1:
                          print()
                          print("Você tirou uma peça.")
                  else:
                      print()
                      print("Você tirou", jogadorTira, "peças.")
                  vezPc = True
                  if n == 1:
                          print("Agora resta apenas uma peça no tabuleiro.")
                          print()
                  else:
                     if n!=0:
                        print("Agora restam", n, "peças no tabuleiro.")
                        print()  
                       
       print("Fim do jogo! O computador ganhou!")            


def  computador_escolhe_jogada(n, m):
        computadorTira=1
        while computadorTira!=m:
              if(n-computadorTira)%(m+1) == 0:
                    return computadorTira
              else:
                    computadorTira+=1
        return computadorTira
               
def usuario_escolhe_jogada(n, m):
          jogadaValida = False
          while not jogadaValida:
                 jogadorTira = int(input('Quantas peças você vai tirar? '))
                 if jogadorTira > m or jogadorTira < 1:
                    print()
                    print('Oops! Jogada inválida! Tente de novo.')
                    print()
                 else:
                    jogadaValida = True
          return jogadorTira

                    
def campeonato():
    numeroRodada = 1
    while numeroRodada <= 3:
        print()
        print('**** Rodada', numeroRodada, '****')
        print()
        partida()
        numeroRodada += 1
    print()
    print('Placar: Você 0 X 3 Computador')     



print("Bem-vindo ao jogo NIM! Escolha:")
print()
print("1 - para jogar uma partida isolada ")
a=int(input("2 - para jogar um campeonato "))
print()

if a == 1:
       print("Você escolheu uma partida isolada!")
       print()
       partida()
       
else:
       print("Você escolheu um campeonato!")
       print()
       campeonato()
