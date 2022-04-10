
def coletar_dados():
    valor_inicial = float(input("Valor inicial: R$"))
    rendimento = float(input("Rendimento por período (%):"))
    aporte_periodico = float(input("Aporte a cada período: R$ "))
    periodos = int(input("Total de períodos:"))

    calcular_juros(valor_inicial,rendimento,aporte_periodico,periodos)


def calcular_juros(valor,rendimento,aporte,periodo):
    for i in range(periodo):
        valor=valor+(valor*(rendimento/100))+aporte
        print(f"Após {i+1} períodos(s), o montante será de R${valor:.2f} ")

coletar_dados()