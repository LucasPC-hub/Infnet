numeroMesa = input("Digite o numero da mesa: ")
numeroPessoas = int(input("Digite o numero de pessoas: "))
if numeroPessoas<1:
    print("Valor invalido")
else:
    quatidadeProdutos = int(input("Digite a quantidade de produtos"))
    valorTotal = 0

    for produto in range(quatidadeProdutos):
        quantidade=input("Digite a quantidade: ")
        valor=input("Digite o valor: ")
        valorTotal = valorTotal + (int(quantidade)) * (int(valor))

    taxaServico=int(input("Digite o percentual do serviço de 0% a 100%"))

    if taxaServico<0 or taxaServico>100:
        print("Valor Invalido")
    else:
        valorTotal=valorTotal+(valorTotal*(taxaServico/100))

        print("Valor total da conta : ",valorTotal)

        valorIndividual = (float(valorTotal)) / (int(numeroPessoas))

        print("Cada uma das ",numeroPessoas,"da mesa ",numeroMesa," irá pagar R$",valorIndividual)
