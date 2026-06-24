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
        print("\n--- Informações do Veículo ---")
        print(f"Marca: {self.__marca}")
        print(f"Modelo: {self.__modelo}")
        print(f"Placa: {self.__placa}")
        print(f"Valor da Diária: R$ {self.__valor_diaria:.2f}")
        print(f"Quilometragem: {self.__quilometragem} km")
        print(f"Status: {status}")
        print("-" * 30)

    def alugar(self):
        if self.__disponivel:
            self.__disponivel = False
            print("Aluguel efetuado com sucesso!")
        else:
            print("Não foi possível alugar!")

    def devolver(self, nova_quilometragem: int):
        if not self.__disponivel and nova_quilometragem > self.__quilometragem:
            self.__quilometragem = nova_quilometragem
            self.__disponivel = True
            print("Devolução efetuada com sucesso!")
        else:
            print("Erro ao efetuar devolução")
