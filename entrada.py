from calculo import Calculo

class Entrada():
    def entradas():
        Matriz = []
        Termos = []
        dados = []
        M = []
        n = int(input("Número de variáveis do Sistema: "))
        
        for i in range(n):
            print("Entre com todos os índeces de X",i+1,":")
            linha = []
            for j in range(n):
                print("X",i+1,"= ",end="")
                t = float(input())
                linha.append(t)
            dados.append(linha)
        print("Entre com os Termos Independentes:")
        
        for i in range(n):
            print(i+1,"º Termo:",end=" ")
            t = float(input())
            Termos.append(t)

        print("\nEntre com os índices do Modelo Matemático:")
        for i in range(n):
            print("X",i+1,"= ",end="")
            t = float(input())
            M.append(t)

        for i in dados:
            Matriz.append(i)
        Calculo.funcao(Matriz,Termos,M)
