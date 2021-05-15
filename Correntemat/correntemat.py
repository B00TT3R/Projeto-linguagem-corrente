#fazer alguma tabela verdade, nem que seja apenas da conjunção
import sys

def conjunção(p, q):
    tabverd = []
    if p == "p" and q == "q":
        tabverd = ["V", "F", "F", "F"]
    if p == "p" and q == "-q":
        tabverd = ["F", "V", "F", "F"]
    if p == "-p" and q == "-q" or p == "-p" and q == "q":
        tabverd = ["F", "F", "F", "V"]
    return (tabverd)
while True:
    #diz que o codigo vai executar infinitamente, a menos que seja pedido para parar lá no final
    p = 0
    q = 0
    #reseta os estados de p e q
    p = input("Digite o primeiro valor (p ou -p) \n > ")
    p = p.lower()
    #pergunta o seu valor no console
    if p in ("p", "-p"):
        #checa se p é um valor válido, o .lower()transforma o valor em minusculo para a comparação
        q = input("Digite o segundo valor (q ou -q) \n > ")
        #cria q, e pergunta o seu valor no console
        if q.lower() in ("q", "-q"):
            #checa se q é um valor válido, o .lower()transforma o valor em minusculo para a comparação
            print("O resultado da tabela verdade vai ser: {}".format(conjunção(p, q)))
        else:
            #diz que o valor de q é inválido
            print("Valor {} inválido".format(q))
    else:
        #diz que o valor de p é invalido
        print("Valor {} inválido".format(p))
    aio = input("Deseja continuar? S/N \n")
    if aio.upper == "S":
        aio = 0
    if aio.upper() == "N":
        sys.exit(0)
    else:
        pass