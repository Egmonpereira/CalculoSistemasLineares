import numpy
import pandas as pd

class Calculo():
    def funcao(Matriz,Termos):
        Deter = []
        aux = []
        temp = []
        temp1 = []
        for i in range(len(Matriz)):
            s = str(i+1)
            temp.append("X"+s+" =")
            temp1.append(" ")

        Deter.append(numpy.linalg.det(Matriz))
        if Deter[0] != 0:
            print("\nCoeficientes:")
            print(pd.DataFrame(Matriz, columns=[temp1], index=[temp]))
            temp.clear()
            temp1.clear()

            for i in range(len(Termos)):
                s = str(i+1)
                temp.append("T"+s+" =")

            print("\nTermos independentes:")
            print(pd.DataFrame(Termos, columns=[" "], index=[temp]))

            t = 0
            for i in range(len(Matriz)):
                for j in range(len(Matriz[0])):
                    if t == j:
                        aux.append(Termos)
                    else:
                        aux.append(Matriz[j])
                        
                Deter.append(numpy.linalg.det(aux))
                t = t + 1
                aux.clear()
            for i in range(8):
                print("=",end="")
                print("-",end="")
            print("=",end="")

            print("\nValores Reais:")
            for i in range(len(Matriz)):
                print("X",i+1,"=", round(Deter[i+1]/Deter[0],2))
        else:
            print('Sistema Indeterminado ou Impossível')