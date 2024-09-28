class Estudante:
    ### VARIAVEIS DA CLASS
    escola = "DIO"
    estado = "PE"
    
        ### CONSTRUTOR ##
    def __init__(self, nome, matricula, curso):
        ## VARIAVEIS DE INSTANCIA
        self.nome = nome
        self.curso = curso
        self.matricula = matricula

        ### FORMATANDO A SAIDA
    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.curso} - {self.escola}-{self.estado}"


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)


aluno_1 = Estudante("Guilherme", 1, "Python")
aluno_2 = Estudante("Giovanna", 2,"Analise de Dados")

Estudante.estado = "SP"
aluno_3 = Estudante("Chappie", 3, "Desenvolvimento de Sistemas")
mostrar_valores(aluno_1, aluno_2, aluno_3)
 