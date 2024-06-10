
print("Calculo de NOTAS DO PRIMEIRO SEMESTRE :")
trabalho_nota_escola1 = float(input("Digite a nota do aluno do primeiro semestre : "))
trabalho_nota_escola2 = float(input("Digite a nota do aluno do segundo semestre : "))
trabalho_nota_escola3 = float(input("Digite a nota do aluno do primeiro semestre : "))
trabalho_nota_escola4 = float(input("Digite a nota do aluno do segundo semestre : "))
trabalho_nota_escola5 = float(input("Digite a nota do aluno do primeiro semestre : "))
media = (trabalho_nota_escola1 + trabalho_nota_escola2 + trabalho_nota_escola3 + trabalho_nota_escola4 + trabalho_nota_escola5) /2


def midia(nota):
    match nota:
        case nota if nota<=4:
            print(f"Reprovado, pois tirou {nota}. ")
        case nota if nota>=4.1 or nota<=7:
            print(f"Em exame, pois tirou {nota} (recuperação).")
        case nota if nota>=7.1 and nota<=10:
            print(f"Aprovado, pois tirou {nota}.")
midia(media)

#SEGUNDO SEMESTRE
trabalho_nota_escola6 = float(input("Digite a nota do aluno do primeiro semestre : "))
trabalho_nota_escola7 = float(input("Digite a nota do aluno do segundo semestre : "))
trabalho_nota_escola8 = float(input("Digite a nota do aluno do primeiro semestre : "))
trabalho_nota_escola9 = float(input("Digite a nota do aluno do segundo semestre : "))
trabalho_nota_escola10= float(input("Digite a nota do aluno do primeiro semestre : "))
notas = (trabalho_nota_escola6 + trabalho_nota_escola7 + trabalho_nota_escola8 + trabalho_nota_escola9 + trabalho_nota_escola10) /2


def media_nota(nota_do_trabalho):
    match nota_do_trabalho:
        case nota_do_trabalho if nota_do_trabalho<=4:
            print(f"Reprovado, pois tirou {nota_do_trabalho}. ")
        case nota_do_trabalho if nota_do_trabalho>=4.1 or nota_do_trabalho<=7:
            print(f"Em exame, pois tirou {nota_do_trabalho} (recuperação).")
        case nota_do_trabalho if nota>=7.1 and nota_do_trabalho<=10:
            print(f"Aprovado, pois tirou {nota_do_trabalho}.")
media_nota(notas)


