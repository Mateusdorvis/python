lang = "Olá vamos testar"

match lang:
    case "JavaScript":
        print("olá, sou o JavaScript, posso deixar os sites mais dinâmicos e estlizados")
    case "Python":
        print("olá, sou o Python, sou uma linguagem de fácil sintaxe e posso fazer tudo.")
    case "PHP":
        print("olá, sou o PHP, posso fazer banco de dados, mas não sobrevivo sem o HTML")
    case "Java":
        print("olá, sou o Java, posso fazer app")
    case "_":
        print("Who are you? ")

v = "mateus"
v1 = v.capitalize
print(v1)
