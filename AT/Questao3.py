
def calculo_percentual(total,gasto):
    percentual_gasto=(gasto/total)*100
    return percentual_gasto

def calculo_ideal(percentual):
    valor_ideal=(percentual*renda_mensal)/100
    return valor_ideal

def diagnostico(percentual_gasto,gasto_ideal,local):
    print(f"Seus gastos totais com {local} comprometem {percentual_gasto:.2f}% de sua renda total. O máximo recomendado é de {gasto_ideal}%.")
    if percentual_gasto<=gasto_ideal:
        print("Seus gastos estão dentro da margem recomendada.")
    else:
        print(f"Portanto ,idealmente, o máximo de sua renda comprometida com moradia deveria ser de R${calculo_ideal(gasto_ideal):.2f}.")

renda_mensal=float(input("Renda mensal total: R$"))
gastos_moradia=float(input("Gastos totais com moradia: R$"))
gastos_educacao=float(input("Gastos totais com educação: R$"))
gastos_transporte=float(input("Gastos totais com transporte: R$"))

diagnostico(calculo_percentual(renda_mensal,gastos_moradia),30,"moradia")
diagnostico(calculo_percentual(renda_mensal,gastos_educacao),20,"educação")
diagnostico(calculo_percentual(renda_mensal,gastos_transporte),15,"transporte")