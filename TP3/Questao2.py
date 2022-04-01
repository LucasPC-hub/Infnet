idade=int(input("Informe a idade da pessoa"))
if idade>=18:
   print("Tem obrigação de votar")
elif (idade>=16 and idade<18) or idade>=70:
   print("Não tem obrigação de votar")
elif (idade>0 and idade<16):
    print("Não tem direito ao voto")
else:
    print("Valor invalido")