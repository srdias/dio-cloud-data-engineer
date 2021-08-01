
try:
    divisao = 10 / 10
    teste=[0,1]

    print("divisão: {}".format(divisao, teste[3]))

except ZeroDivisionError:
    print("Não é possivel realizar uma divisão por 0")
except IndexError:
    print("Erro ao acessar um indice inválido da lista")
except Exception as ex:
    print("Erro desconhecido: {}".format(ex))
else:
    print("Sem erros!!")