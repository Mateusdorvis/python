class Ocean:

    def __init__(self, sea_creature_name, sea_creature_age):
        self.name = sea_creature_name
        self.age = sea_creature_age
    def __str__(self):#_str_() é usado para se tornar legível para os não programadores 
        return f"The creature type is {self.name} and the age is {self.age}"
    def __repr__(self):
        return f"Ocean ({self.name}  {self.age})"#formatar de um jeito técnico para o programador ler
    
