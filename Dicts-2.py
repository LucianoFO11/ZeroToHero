#Imprima todos os alunos aprovados (nota ≥ 6).
#Mostre a média das notas da turma.
#Peça ao usuário para digitar um nome e diga se o aluno existe no dicionário.

alunos = { "Ana": 8.0, "Lucas": 5.5, "João": 9.2}

for chave,nota in alunos.items():
    if nota >= 6:
        print("o aluno:",chave,"está aprovado")

total=0 
for i in alunos.values():
    total=total+i
print("a média da turma é:",total/len(alunos))

print("Digite um nome")
nomepesquisa=input()
if nomepesquisa in alunos.keys():
    print("Este aluno está.")
else:
    print("Este aluno não está.")