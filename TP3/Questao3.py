maior_nota=-1
vencedor= " "


for aluno in range(5):
    nome_aluno=str(input(f"Digite o nome do {aluno+1}º aluno"))
    nota_aluno=int(input(f"Digite a nota do {aluno+1}º aluno"))

    if nota_aluno<0 or nota_aluno>100:
        print("Valor invalido")
    else:
        if nota_aluno>maior_nota:
            maior_nota=nota_aluno
            vencedor=nome_aluno

print("O vencedor é "+vencedor+ " com nota ",maior_nota)