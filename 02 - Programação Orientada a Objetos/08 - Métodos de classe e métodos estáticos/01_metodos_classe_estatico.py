class Pessoa:
    
    ###>> Atributos da classe <<<###
    def __init__(self, nome, idade, sexo,cor):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.cor = cor

    @classmethod  ###>>>INSTANCIA DA CLASS <<<##
    
    def criar_de_data_nascimento(cls, ano, mes, dia, nome,sexo,cor):
        idade = 2024 - ano
        return cls(nome, idade, sexo, cor)
    
    def __str__(cls) -> str:
        return f"nome:{cls.nome}\n - idade:{cls.idade}\n - sexo:{cls.sexo}\n - cor:{cls.cor}"



    ###FUNÇÃO UTILITARIA
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18
    
    
def mostrar_dados(*objs):
    for obj in objs:
        print(obj)

p = Pessoa.criar_de_data_nascimento(1982, 3, 21, "David","Masculino","Parda")
mostrar_dados(p)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))
