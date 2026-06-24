import random
class Carro:
    # método construtor
    def __init__(self, marca, modelo, placa, diaria):
        self.__marca = marca
        self.__modelo = modelo
        self.__placa = placa
        self.__diaria = diaria
        self.__quilometragem = 0
        self.__disponibilidade = True
    
    def exibir(self, disponibilidade):
        if (not self.disponibilidade == True):
            print(f"!!Carro!! Marca:{self.marca}Modelo:{self.modelo}Placa:{self.placa}Valor_da_Diária:{self.diaria}Quilometragem:{self.quilometragem}Disponibilidade:{self.disponibilidade} Disponivel")
        else:
            print(f"!!Carro!! Marca:{self.marca}Modelo:{self.modelo}Placa:{self.placa}Valor_da_Diária:{self.diaria}Quilometragem:{self.quilometragem}Disponibilidade{self.disponibilidade} Indisponivel")
    

    def disponibilidade(self):
        if (self.disponibilidade == True):
             self.disponibilidade == False
            print("O carro esta totalmente disponivel")
        else:
            print("Desculpe o carro já foi alugado")

    def devolucao(self):
        if(self.disponibilidade == False):
            self.disponibilidade == True
            print("Devolução concluida com sucesso!")
        else:
            print("Erro em efetuar a devolução")

    def transferir(self, nova_diaria):
        self.__nova_diaria = nova_diaria