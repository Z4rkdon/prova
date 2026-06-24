class Carro:
    # método construtor
    def __init__(self, marca: str, modelo: str, placa: str, valor_diaria: float):
        self.__marca = marca
        self.__modelo = modelo
        self.__placa = placa
        self.__valor_diaria = valor_diaria
        self.__quilometragem = 0
        self.__disponivel = True

    @property
    def marca(self):
        return self.__marca

    @property
    def modelo(self):
        return self.__modelo

    @property
    def placa(self):
        return self.__placa

    @property
    def valor_diaria(self):
        return self.__valor_diaria

    @valor_diaria.setter
    def valor_diaria(self, novo_valor):
        if novo_valor > 0:
            self.__valor_diaria = novo_valor

    @property
    def quilometragem(self):
        return self.__quilometragem

    @property
    def disponivel(self):
        return self.__disponivel

    def exibir(self):
        status = "Disponível" if self.__disponivel else "Alugado"
        print("***Informações do Veículo***")
        print(f"Marca: {self.__marca}")
        print
