#atividade 3
#cadastro de alunos
alunos=[]
repeticoes=(int(input("Bem vindo ao sistema de notas, digite quantos alunos deseja lançar: ")))
for i in range(repeticoes):
    novoaluno=[]
    nome=str((input("digite o nome do aluno: ")))
    novoaluno.append(nome)
    idade=int((input("digite a idade do aluno: ")))
    novoaluno.append(idade)
    notafinal=float((input("digite a nota final do aluno: ")))
    novoaluno.append(notafinal)
    alunos.append(novoaluno)
    print("-------------------------")

#analise: aprovados
quantidadealunos=len(alunos)
aprovados=[]
for j in range(quantidadealunos):
    if alunos[j][2] >= 6:
        print(alunos[j][0],"está aprovado.")
        j+1
        novoaprovado=alunos[j][0]
        aprovados.append(novoaprovado)
print("os alunos aprovados são")
print(aprovados)

#analise: média da turma
total = 0
for k in range(quantidadealunos):
    total=total+alunos[k][2]
    k+1
media=total/quantidadealunos
print("a média da turma é:",media)

#analise: alunos com menos de 18 anos
alunosmenorque18=[]
for h in range(quantidadealunos):
    if alunos[h][1] < 18:
        novoalunomenor=alunos[h][0]
        alunosmenorque18.append(novoalunomenor)
print("os alunos menores de idade são")
print(alunosmenorque18)

#analise: aluno com a maior nota
notasporaluno=[]
for i in range(quantidadealunos):
    novanota=alunos[i][2]
    notasporaluno.append(novanota)

alunomnota=(notasporaluno.index(max(notasporaluno)))
print("o aluno com a maior nota foi: ", alunos[alunomnota][0])