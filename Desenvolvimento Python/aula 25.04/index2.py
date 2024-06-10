nota_escola1 = float(input("Digite a nota do aluno do primeiro semestre : "))
nota_escola2 = float(input("Digite a nota do aluno do segundo semestre : "))
media = (nota_escola1 + nota_escola2) /2


def midia(nota):
    match nota:
        case nota if nota<=4:
            print(f"Reprovado, pois tirou {nota}. ")
        case nota if nota>=4.1 or nota<=7:
            print(f"Em exame, pois tirou {nota} (recuperação).")
        case nota if nota>=7.1 and nota<=10:
            print(f"Aprovado, pois tirou {nota}.")
midia(media)


